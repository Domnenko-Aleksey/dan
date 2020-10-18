import pandas as pd
import numpy as np
# import tensorflow as tf
# from tensorflow import keras
from keras import models
from keras import layers
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

from keras.datasets import boston_housing


def model_2(SITE):
    print('PATH -> index/metallurgy/model.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/model/model.css')
    SITE.addHeadFile('/lib/DAN/DAN.css')

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    data = MD.getAll()

    (train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()

    print('SHAPE', train_date.shape, test_data.shape)


    # Нормализация данных
    mean = train_data.mean(axis=0)
    train_data -= mean
    std = train_data.std(axis=0)
    train_data /= std

    test_data -= mean
    test_data /= std


    # Конструирование сети
    def build_model():
        model = models.Sequential()
        model.add(layers.Dense(64, activation='relu', input_shape=(train_data.shape[1],)))
        model.add(layers.Dense(64, activation='relu'))
        model.add(layers.Dense(1))
        model.compile(optomizer='rmsprop', loss='mse', metrics=['mae'])
        return model

    
    # Перекрёстная проверка по к блокам
    k = 4
    num_val_samples = len(train_data) // k
    num_epochs = 100
    all_scories = []

    for i in range(k):
        print('processing fold #', i)
        val_data = train_data[i*num_val_samples: (i + 1)*num_val_samples]
        val_targets = train_targets[i*num_val_samples: (i + 1)*num_val_samples]

        # Подготовка обучающих данных из остальных блоков
        partial_train_data = np.concatenate([
            train_data[:i*num_val_samples],
            
            ])






    return
    '''
    # ------- ПОЛНОСВЯЗНАЯ СЕТЬ -------
    df = pd.DataFrame(data)

    data = df.iloc[:,1:9]
    target = df.iloc[:,10:11]

    X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=42, test_size=0.2)

    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_n = np.array(min_max_scaler.fit_transform(X_train), dtype='float32')
    X_test_n = np.array(min_max_scaler.fit_transform(X_test), dtype='float32')

    y_train_n = np.array(y_train, dtype = 'float32')

    # Создаём модель и добавляем слои
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(100, activation="relu", input_shape=(X_train_n.shape[1],)))
    model.add(tf.keras.layers.Dense(1, activation="softmax"))

    model.compile(optimizer='rmsprop',
        loss='mse',
        metrics='accuracy'
    )

    # Запускаем модель обучения
    history = model.fit(X_train_n, y_train_n, batch_size=8, epochs=10, validation_split=0.2)

    return













    accuracy = int(model.score(X_test_n, y_test) * 100)
    print('Точность предсказаний на тестовой выборке:', accuracy, '%')
    print('PREDICT', predicted, y_test)
    print('Параметры модели', type(model.coef_), model.coef_)
    # ------- /


    # ------- График -------
    # Стандартное отклонение
    fig, ax = plt.subplots()
    plt.title('Стандартное отклонение', fontsize=16)
    plt.xlabel('Предсказаные значения', fontsize=12)
    plt.ylabel('Истинные значения', fontsize=12)
    ax.scatter(predicted.tolist(), y_test)
    ax.plot([0, 100], [0,100], color='#10ca93', label='Модель')
    legend = ax.legend(loc='upper left', fontsize='12')
    legend = ax.legend()
    fig.savefig('templates/index/metallurgy/model/images/standard_deviations.png')  # Сохраняем график  

    # Веса модели
    x = np.arange(8)
    fig, ax = plt.subplots()
    plt.bar(x, model.coef_[0])
    plt.xticks(x, ('1', '2', '3', '4', '5', '6', '7', '8'))
    plt.xlabel('№ Веса', fontsize=12)
    plt.ylabel('% Влияния', fontsize=12)
    fig.savefig('templates/index/metallurgy/model/images/weights.png')  # Сохраняем график 

    # Предсказанные и истинные значения
    # Задаем смещение равное половине ширины прямоугольника:
    pred = predicted.reshape(1, 20)[0]
    y_t = y_test.to_numpy().reshape(1, 20)[0]
    x = np.arange(20)
    fig, ax = plt.subplots()
    width = 0.3
    ax.bar(x - width/2, pred, width, label='Предсказанные значения')
    ax.bar(x + width/2, y_t, width, label='Реальные значения')
    ax.set_title('Предсказанные и истинные значени', fontsize=16)
    ax.set_xticks(x)
    plt.xlabel('% износа', fontsize=12)
    # ax.set_xticklabels(cat_par, fontsize='8')
    ax.legend()
    fig.savefig('templates/index/metallurgy/model/images/predicted.png')  # Сохраняем график 
    # ------- /


    # ------- Таблица сравнения -------
    tr = ''
    for i in range(20):
        y = float(y_test.iloc[i, 0])
        p = float(predicted[i][0])
        accuracy_item = round((1 - abs(y - p)/y)*100, 2)

        tr += '<tr><td>' + str(y_test.index[i] + 1) + '</td>'
        tr += '<td>' + str(round(predicted[i][0],2)) + '</td>'
        tr += '<td>' + str(y_test.iloc[i, 0]) + '</td>'
        tr += '<td>' + str(accuracy_item) + '%</td></tr>'
    
    predicted_table =   '<table class="table_list">'
    predicted_table +=      '<tr><th>№ гильзы</th><th>Прогноз износа</th><th>Образцовые значения</th><th>Точность прогноза</th></tr>'
    predicted_table +=      tr
    predicted_table +=  '</table>'
    # ------- /

    # ------- Таблица данных для обучения модели -------
    tr = ''
    for i in range(80):
        row = X_train.iloc[i,]
        tr +=   '<tr>'
        tr +=       '<td>' + str(X_train.index[i]) + '</td>'
        tr +=       '<td>' + str(row[0]) + '</td>'
        tr +=       '<td>' + str(row[1]) + '</td>'
        tr +=       '<td>' + str(row[2]) + '</td>'
        tr +=       '<td>' + str(row[3]) + '</td>'
        tr +=       '<td>' + str(row[4]) + '</td>'
        tr +=       '<td>' + str(row[5]) + '</td>'
        tr +=       '<td>' + str(row[7]) + '</td>'
        tr +=       '<td>' + str(y_train.iloc[i, 0]) + '</td>'
        tr +=   '<tr>'

    train_table =   '<table class="table_list">'
    train_table +=      '<tr>'
    train_table +=          '<th>№ гильзы</th>'
    train_table +=          '<th>' + MODEL.weights[1][3] + '</th>'
    train_table +=          '<th>' + MODEL.weights[2][3] + '</th>'
    train_table +=          '<th>' + MODEL.weights[3][3] + '</th>'
    train_table +=          '<th>' + MODEL.weights[4][3] + '</th>'
    train_table +=          '<th>' + MODEL.weights[5][3] + '</th>'
    train_table +=          '<th>' + MODEL.weights[6][3] + '</th>'
    train_table +=          '<th>Кол-во плавок</th>'
    train_table +=          '<th>Износ, %</th>'
    train_table +=      '</tr>'
    train_table +=      tr
    train_table +=  '</table>'
    # ------- /


    html_model = open('templates/index/metallurgy/model/model.html', 'r', encoding='utf-8').read()
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
        nav_model = 'active',
        nav_alarm = '',
        nav_help = ''
    )
    '''