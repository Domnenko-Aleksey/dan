import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

def dashboard(SITE):
    print('PATH -> index/metallurgy/dashboard.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/dashboard/dashboard.css')

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
    # ------- /

    print('predicted', predicted)

    predicted_html = ''
    i = 0
    for pr in predicted:
        value = round(pr[0], 2)
        if (value < 40):
            css_class = 'wear_low'
        if (value > 39 and value < 80):
            css_class = 'wear_medium'
        if (value > 80):
            css_class = 'wear_high'
        predicted_html += '<div class="product_name_item flex_row">'
        predicted_html +=   '<span class="product_name">Изделие № <span id="product_name_number">' + str(y_test.index[i] + 1) + '</span></span>'
        predicted_html +=   '<span class="product_name_wear ' + css_class + '"><span id="product_name_percent">' + str(value) + '</span>%'
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
        nav_model = '',
        nav_alarm = '',
        nav_help = ''
    )