import random
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

class Model:
    def __init__(self, SITE):
        self.db = SITE.db
        # Допустимые значения и эталонные веса для датасета
        # Срок службы кристализаторов до 15 – 25 тыс. тонн выплавляемой стали и 200, 300, 350, 1200 плавок
        self.weights = [
            [1560, 1590, 0.17, 'Температура стали, °C'],  # Температуры входящей стали 1560 - 1590 / 1539 - температура затвердевания чистого железа
            [30, 35, 0.1, 'Tемпература воды, °C'],  # Температуры охлаждающей воды 30 - 35 / на входе 15 - 25, на выходе 40 - 45
            [45, 90, 0.05, 'Частота качания, n/мин.'],  # Частота качания 45 - 90 в минуту
            [2.0, 2.4, 0.18, 'Скорость движения, м/мин.'],  # Скорость движения  1.2 - 1.6 или 2,0 - 2,4 м/мин.
            [0.8, 1, 0.08, 'Эффективная длинна, m'],  # Эффективная длина гильзы, м
            [2500, 14400, 0.27, 'Площадь сечения, мм'],  # Площадь сечения гильзы, мм2
            [0.8, 1.2, 0.15, 'Нормализованная конусность']  # Нормализованная конусность - уточнить у металлургов
        ]


    # Математическая модель для формирования датасета
    # Добавляем случайность как в коэффициенты, так и в итог
    def datasetGenerator(self, item_id=False, k_rand=0):  # rand - относительная единица отклонения
        # Параметры, наборы: ['минимальное значение', 'максимальное значение', 'нормализованный вес']
        # k_rand = 0.2  # Коэффициент случаности в весах, 0 - нет случайности

        melt = 400  # Среднее количество плавок до износа гильзы

        # Удаляем старые данные и обновляем auto_increment до 0
        self.deleteData()

        dataset = []
        tr = ''
        for n in range(100):
            values = []
            i = 0
            k_s = 0  # Сумма приведённых коэффициентов для одной плавки
            for w in self.weights:
                value = w[0] + (w[1] - w[0])*random.random()
                if i < 3:
                    values.append(round(value))
                else:
                    values.append(round(value, 1))

                # Коэффициент случайных значений
                r_min = w[2]*(1 - k_rand)
                r_max = w[2]*(1 + k_rand)
                rnd = random.uniform(r_min, r_max)   
                # Рассчитываем коэффициент влияния веса
                k = value/((w[0] + w[1])/2)*rnd
                k_s += k
                i += 1

            n_melt_min = round(0.2*melt)
            n_melt_max = round(0.8*melt)
            n_melt = random.randint(n_melt_min, n_melt_max)  # Количество плавок для гильзы
            wear = ((n_melt*k_s)/melt)*100

            values.append(n_melt)
            values.append(round(k_s, 4))
            values.append(round(wear, 2))
            dataset.append(values)

            self.insertData(values)


    # Добавляем данные (№ + датасет) в MySQL
    def insertData(self, data):
        sql =   "INSERT INTO com_metallurgy_data SET " 
        sql +=  "p_1 = %s, p_2 = %s, p_3 = %s, p_4 = %s, p_5 = %s, p_6 = %s, p_7 = %s, melt = %s, k = %s, wear = %s"
        return self.db.execute(sql, data)

    
    # Удаляем данные и вновь обновляем autoincrement до 0
    def deleteData(self):
        sql = "DELETE FROM com_metallurgy_data"
        self.db.execute(sql)

        sql = "ALTER TABLE com_metallurgy_data AUTO_INCREMENT=0;"
        self.db.execute(sql)


        '''
        # Создание датафрейма
        df = pd.DataFrame(dataset)
        print('dataframe', df.head(7))

        data = df.iloc[:,0:8]
        target = df.iloc[:,9:10]
        print('data, target', data.head(), target.head())

        X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42, test_size=0.2)

        min_max_scaler = preprocessing.MinMaxScaler()
        X_train_n = min_max_scaler.fit_transform(X_train)
        X_test_n = min_max_scaler.fit_transform(X_test)

        linear_regression = LinearRegression()  # normalize - False
        model = linear_regression.fit(X_train_n, y_train)
        predicted = model.predict(X_test_n)

        accuracy = int(model.score(X_test_n, y_test) * 100)
        print('Точность предсказаний на тестовой выборке:', accuracy, '%')
        print('PREDICT', predicted, y_test)
        print('Параметры модели', model.coef_)
        '''





        '''
        X_train_n = min_max_scaler.fit_transform(X_train)
        X_test_n = min_max_scaler.fit_transform(X_test)

        print('Нормализованные значения')
        print(X_train_n)

        linear_regression = LinearRegression()
        model_l = linear_regression.fit(X_train_n, y_train)
        predicted = model_l.predict(X_test_n)

        accuracy = int(model_l.score(X_test_n, y_test) * 100)
        print('Точность предсказаний на тестовой выборке:', accuracy, '%')

        print('PREDICT', predicted, y_train)


        # Нейронная сеть
        model_n = tf.keras.models.Sequential()
        model_n.add(tf.keras.layers.Dense(100, activation="relu", input_shape=(100,100)))
        model_n.add(tf.keras.layers.Dense(10, activation="softmax"))

        # Компилируем модель
        model_n.compile(optimizer="adam",
                        loss="mean_squared_error",
                        metrics=["accuracy"])

        X_train_r = X_train.reshape(X_train.shape[0], 8)
        print('Train:', X_train_r.shape)

        model_n.fit(X_train_r, y_test, batch_size=25, epochs=10, validation_split=0.2)

        # Проверка модели на тестовой выборке
        model_n.evaluate(X_test, y_test)
        '''