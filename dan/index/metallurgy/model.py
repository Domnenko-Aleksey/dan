import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData


def model(SITE):
    print('PATH -> index/metallurgy/model.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/model/model.css')
    SITE.addHeadFile('/lib/DAN/DAN.css')

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    data = MD.getAll()


    # ------- ЛИНЕЙНАЯ РЕГРЕССИЯ -------
    df = pd.DataFrame(data)

    data = df.iloc[:,1:9]
    target = df.iloc[:,10:11]

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
        tr +=       '<td>' + str(row[6]) + '</td>'
        tr +=       '<td>' + str(row[7]) + '</td>'
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