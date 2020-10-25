import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
import tensorflow as tf
from tensorflow import keras
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

def dashboard(SITE):
    print('PATH -> index/metallurgy/dashboard.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/dashboard/dashboard.css')

    df = pd.read_csv('index/metallurgy/dataset.csv')
    # Сохранённая модель - для бустрого запуска без обучения на 1000 эпох
    model_file = 'index/metallurgy/model_dff.h5'

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

    print('------- ЗАГРУЖАЕМ МОДЕЛЬ -------')
    model = tf.keras.models.load_model(model_file)

    # Оцениваем модель
    loss, mae, mape = model.evaluate(X_test_n, y_test_r)
    print('LOSS, MAE, MAPE', loss, mae, mape)
    accuracy = round(100 - mape, 2)
    print('------- Точность -------', accuracy)

    # Делаем предсказание
    predicted = model.predict(x_test_n)

    print('predicted', predicted)

    predicted_html = '<h3>Предсказанная стойкость гильз</h3>'
    i = 0
    for pr in predicted:
        index = Y_test.index[i]
        value = round(pr[0], 2)

        predicted_html += '<div class="product_name_item flex_row">'
        predicted_html +=   '<span class="product_name">№ <span id="product_name_number">' + str(df.iloc[index, 1]) + '</span></span>'
        predicted_html +=   '<span class="product_name_wear"><span id="product_name_percent">' + str(value) + '</span>'
        predicted_html += '</div>'
        i += 1

    html_dashboard = open('templates/index/metallurgy/dashboard/dashboard.html', 'r', encoding='utf-8').read()
    dashboard = Template(html_dashboard)
    render_dashboard = dashboard.render(
        predicted_html = predicted_html,
        tmpl_body = html_dashboard
    )

    html_default = open('templates/index/metallurgy/default/default.html', 'r', encoding='utf-8').read()
    default = Template(html_default)

    SITE.content += default.render(
        tmpl_body = render_dashboard, 
        nav_home = 'active', 
        nav_factory = '',
        nav_database = '',
        nav_model_dff = '',
        nav_model_lr = '',
        nav_alarm = '',
        nav_help = ''
    )