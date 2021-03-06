import os.path
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import json
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData


def model_dff_train(SITE):
    print('PATH -> index/metallurgy/model_dff_train.py')

    num_epochs = int(SITE.post['epochs'])

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    data = MD.getAll()

    # Сохранённая модель - для бустрого запуска без обучения на 1000 эпох
    model_file = 'index/metallurgy/model_dff.h5'

    # ------- ПОЛНОСВЯЗНАЯ НЕЙРОННАЯ СЕТЬ -------
    df = pd.DataFrame(data)
    # df.to_csv('metallurgy_dataset.csv', sep=',', encoding='utf-8')

    data = df.iloc[:,1:9]
    target = df.iloc[:,10:11]

    X_train, X_test, Y_train, Y_test = train_test_split(data, target, random_state=42, test_size=0.2)

    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_n = min_max_scaler.fit_transform(X_train)
    X_test_n = min_max_scaler.fit_transform(X_test)

    x_train_n = np.array(X_train_n, dtype = 'float32')
    x_test_n = np.array(X_test_n, dtype = 'float32')
    y_train = np.array(Y_train, dtype = 'float32')
    y_test = np.array(Y_test, dtype = 'float32')

    y_train_r = y_train.reshape(y_train.shape[0],)
    y_test_r = y_test.reshape(y_test.shape[0],)


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


    answer = {'answer': 'success'}
    return {'ajax': json.dumps(answer)}