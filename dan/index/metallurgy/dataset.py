import pandas as pd
import numpy as np
from jinja2 import Template

def dataset(SITE):
    print('PATH -> index/metallurgy/dataset.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset.css')
    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset.js')

    df = pd.read_csv('index/metallurgy/dataset.csv')

    for i in range(df.shape[0]):
        if i == 0:
            out =   '<table class="table_list">'
            out +=      '<tr>'
            out +=          '<th>№</th>'

            for j in range(df.shape[1]):
                if j > 0:
                    out += '<th>' + df.columns[j] + '</th>'

            out += '</tr>'

        out +=   '<tr>'
        for j in range(df.shape[1]):
            out += '<td>' + str(round(df.iloc[i, j],1)) + '</td>'
        out +=   '<tr>'
    out +=  '</table>'

    html_dataset = open('templates/index/metallurgy/dataset/dataset.html', 'r', encoding='utf-8').read()
    dataset = Template(html_dataset)
    render_dataset = dataset.render(dataset_out=out)

    html_default = open('templates/index/metallurgy/default/default.html', 'r', encoding='utf-8').read()
    default = Template(html_default)

    SITE.content += default.render(
        tmpl_body = render_dataset, 
        nav_home = '', 
        nav_factory = '',
        nav_data = 'active',
        nav_model_dff = '',
        nav_model_lr = '',
        nav_alarm = '',
        nav_help = ''
    )
