import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

def model(SITE):
    print('PATH -> index/metallurgy/model.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/model/model.css')

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    data = MD.getAll()


    # ------- ЛИНЕЙНАЯ РЕГРЕССИЯ -------
    df = pd.DataFrame(data)
    print('dataframe', df.head(7))

    data = df.iloc[:,1:9]
    target = df.iloc[:,10:11]
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
    # ------- /


    html_model = open('templates/index/metallurgy/model/model.html', 'r', encoding='utf-8').read()
    model = Template(html_model)
    render_model = model.render(tmpl_body=html_model)

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