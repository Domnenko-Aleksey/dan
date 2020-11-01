import os.path
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData


def model_dff(SITE):
    print('PATH -> index/metallurgy/model_dff.py')
    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/model_dff/model_dff.css')
    SITE.addHeadFile('/templates/index/metallurgy/model_dff/model_dff.js')

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    data = MD.getAll()

    # Сохранённая модель - для бустрого запуска без обучения на 1000 эпох
    model_file = 'index/metallurgy/model_dff.h5'


    # ------- ПОЛНОСВЯЗНАЯ НЕЙРОННАЯ СЕТЬ -------
    df = pd.read_csv('index/metallurgy/dataset.csv')

    data = df.iloc[:,2:11]
    target = df.iloc[:,11:12]

    print("DATA\n", data.head())
    print("TARGET\n", target.head())

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, random_state=20, test_size=0.2)

    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_n = min_max_scaler.fit_transform(X_train)
    X_test_n = min_max_scaler.fit_transform(X_test)

    x_train_n = np.array(X_train_n, dtype = 'float32')
    x_test_n = np.array(X_test_n, dtype = 'float32')
    y_train = np.array(Y_train, dtype = 'float32')
    y_test = np.array(Y_test, dtype = 'float32')

    y_train_r = y_train.reshape(y_train.shape[0],)
    y_test_r = y_test.reshape(y_test.shape[0],)

    # Проверяем - есть ли сохранённая модель. Если есть - загружаем её, если нет - создаём и обучаем модель
    if os.path.isfile(model_file):
        print('------- ЗАГРУЖАЕМ МОДЕЛЬ -------')
        model = tf.keras.models.load_model(model_file)
        history = False
    else:
        # СОЗДАЁМ МОДЕЛЬ
        print('------- СОЗДАЁМ МОДЕЛЬ -------')
        # Поскольку мало данных, мы будем использовать очень маленькую сеть с двумя скрытыми слоями, каждый с 64 нейронами
        # Что бы избежать переобучения
        # Скалярная регрессия (мы пытаемся предсказать одно непрерывное значение)
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Dense(64, activation='relu', input_shape=(x_train_n.shape[1],)))    
        model.add(tf.keras.layers.Dense(64, activation='relu'))   
        model.add(tf.keras.layers.Dense(1))

        model.compile(optimizer='rmsprop', loss='mse', metrics=['mae', 'mape'])
        print('Свойства модели')
        print(model.summary())

        # Обучаем модель
        num_epochs = 1000
        history = model.fit(x_train_n, y_train_r, epochs=num_epochs, batch_size=1)

        # Сохраним всю модель в  HDF5 файл
        model.save(model_file)

    # Оцениваем модель
    loss, mae, mape = model.evaluate(X_test_n, y_test_r)
    print('LOSS, MAE, MAPE', loss, mae, mape)
    accuracy = round(100 - mape, 2)
    print('------- Точность -------', accuracy)

    # Делаем предсказание
    predicted = model.predict(x_test_n)
    # print('PREDICT', predicted, y_test_r)
    # ------- /


    # МОДЕЛЬ ОБУЧЕНА ЗАНОВО (есть history) - РИСУМЕМ ГРАФИКИ
    if history:
        # ------- ГРАФИКИ -------
        # Зависимость абсолютной ошибки от количества эпох
        history_mae = history.history['mae']
        fig, ax = plt.subplots()
        ax.set_title('Cредняя абсолютная ошибка', fontsize=16)
        ax.set_xlabel('Эпох', fontsize=12)
        ax.set_ylabel('Абсолютная ошибка', fontsize=12)
        ax.plot(history_mae)
        fig.savefig('templates/index/metallurgy/model_dff/images/dff_history_mae.png')

        # Зависимость точности от количества эпох
        history_acc = 100 - np.array(history.history['mape'])
        fig, ax = plt.subplots()
        ax.set_title('Точность модели', fontsize=16)
        ax.set_xlabel('Эпох', fontsize=12)
        ax.set_ylabel('Точность, %', fontsize=12)
        ax.plot(history_acc)
        fig.savefig('templates/index/metallurgy/model_dff/images/dff_history_acc.png')

        # Стандартное отклонение
        fig, ax = plt.subplots()
        ax.set_title('Стандартное отклонение', fontsize=16)
        ax.set_xlabel('Предсказаные значения', fontsize=12)
        ax.set_ylabel('Истинные значения', fontsize=12)
        ax.scatter(predicted.tolist(), Y_test, color='#3a7afe')
        ax.plot([0, 100], [0,100], color='#10ca93', label='Модель')
        legend = ax.legend(loc='upper left', fontsize='12')
        legend = ax.legend()
        fig.savefig('templates/index/metallurgy/model_dff/images/dff_standard_deviations.png') 

        # Предсказанные и истинные значения
        # Задаем смещение равное половине ширины прямоугольника:
        pred = predicted.reshape(1, 20)[0]
        y_t = Y_test.to_numpy().reshape(1, 20)[0]
        x = np.arange(20)
        fig, ax = plt.subplots()
        width = 0.3
        ax.bar(x - width/2, pred, width, label='Предсказанные значения', color='#3a7afe')
        ax.bar(x + width/2, y_t, width, label='Реальные значения', color='#ff7b06')
        ax.set_title('Предсказанные и истинные значени', fontsize=16)
        ax.set_xticks(x)
        plt.xlabel('% износа', fontsize=12)
        # ax.set_xticklabels(cat_par, fontsize='8')
        ax.legend()
        fig.savefig('templates/index/metallurgy/model_dff/images/dff_predicted.png')  # Сохраняем график 
        # ------- /

        # Гистограма износа test.
        fig, ax = plt.subplots()
        ax.hist(predicted, color='#3a7afe')
        ax.set_title('Гистограмма износа гильз - тестовая выборка', fontdict={'fontsize':16, })
        ax.set_xlabel('Износ')
        ax.set_ylabel('Количество')
        ax.figure.savefig('templates/index/metallurgy/model_dff/images/dff_hist_test.png')

        # Гистограма износа target (all).
        target_r = target.to_numpy().reshape(1, 100)[0]
        fig, ax = plt.subplots()
        ax.hist(target_r, bins=10, color='#3a7afe')
        ax.set_title('Гистограмма износа гильз - полная выборка', fontdict={'fontsize':16})
        ax.set_xlabel('Износ')
        ax.set_ylabel('Количество')
        ax.figure.savefig('templates/index/metallurgy/model_dff/images/dff_hist_target.png')

        # График температуры стали.
        steel_temperature = data['p_1'].to_numpy().reshape(1, 100)[0]
        fig, ax = plt.subplots()
        ax.plot(steel_temperature, color='#ff7b06')
        ax.grid()
        ax.set_xlim()
        ax.set_xticks([])  # Не выводить ось х
        ax.set_title('Температура стали', fontdict={'fontsize':16})
        ax.set_ylabel('Температура')
        ax.figure.savefig('templates/index/metallurgy/model_dff/images/dff_steel_temperature.png')

        # График температуры воды.
        water_temperature = data['p_2'].to_numpy().reshape(1, 100)[0]
        fig, ax = plt.subplots()
        ax.plot(water_temperature, color='#3a7afe')
        ax.grid()
        ax.set_xlim()
        ax.set_xticks([])  # Не выводить ось х
        ax.set_title('Температура воды', fontdict={'fontsize':16})
        ax.set_ylabel('Температура')
        ax.figure.savefig('templates/index/metallurgy/model_dff/images/dff_water_temperature.png')


    # ------- Таблица сравнения -------
    tr = ''
    accuracy_sum = 0

    for i in range(Y_test.shape[0]):
        y = float(Y_test.iloc[i, 0])
        p = float(predicted[i][0])
        accuracy_item = round((1 - abs(y - p)/y)*100, 2)
        accuracy_sum += accuracy_item

        index = Y_test.index[i]
        tr += '<tr><td>' + str(df.iloc[index, 1]) + '</td>'
        tr += '<td>' + str(round(predicted[i][0],2)) + '</td>'
        tr += '<td>' + str(Y_test.iloc[i, 0]) + '</td>'
        tr += '<td>' + str(accuracy_item) + '%</td></tr>'
    
    predicted_table =   '<table class="table_list table_m">'
    predicted_table +=      '<tr><th>№ гильзы</th><th>Прогноз стойкости</th><th>Истинная стойкость</th><th>Точность прогноза</th></tr>'
    predicted_table +=      tr
    predicted_table +=  '</table>'
    accuracy_tab = round(accuracy_sum/Y_test.shape[0], 2)
    # ------- /

    # ------- Таблица данных для обучения модели -------
    tr = ''
    for i in range(X_train.shape[0]):
        row = X_train.iloc[i,]
        index = Y_train.index[i]
        tr +=   '<tr>'
        tr += '<td>' + str(df.iloc[index, 1]) + '</td>'
        for j in range(X_train.shape[1]):
            tr += '<td>' + str(round(X_train.iloc[i, j], 1)) + '</td>'
        tr +=       '<td>' + str(Y_train.iloc[i, 0]) + '</td>'
        tr +=   '<tr>'

    train_table =   '<table class="table_list table_m">'
    train_table +=      '<tr>'
    train_table += '<th>Номер гильзы</th>'
    for j in range(X_train.shape[1]):
        train_table += '<th>' + X_train.columns[j] + '</th>'
    train_table +=          '<th>Стойкость</th>'
    train_table +=      '</tr>'
    train_table +=      tr
    train_table +=  '</table>'
    # ------- /


    html_model = open('templates/index/metallurgy/model_dff/model_dff.html', 'r', encoding='utf-8').read()
    model = Template(html_model)
    render_model = model.render(
        accuracy=accuracy,
        predicted_table=predicted_table,
        train_table=train_table
    )


    html_default = open('templates/index/metallurgy/default/default.html', 'r', encoding='utf-8').read()
    default = Template(html_default)

    SITE.content += default.render(
        tmpl_body = render_model, 
        nav_home = '', 
        nav_factory = '',
        nav_database = '',
        nav_model_dff = 'active',
        nav_model_lr = '',
        nav_alarm = '',
        nav_help = ''
    )