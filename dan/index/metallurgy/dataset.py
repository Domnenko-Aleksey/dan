from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

def dataset(SITE):
    print('PATH -> index/metallurgy/dataset.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset.css')
    SITE.addHeadFile('/lib/DAN/DAN.css')
    SITE.addHeadFile('/lib/DAN/DAN.js')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset.js')

    MODEL = Model(SITE)
    MD = MetallurgyData(SITE)
    rows = MD.getAll()
    tr = ''
    for row in rows:
        tr +=   '<tr>'
        tr +=       '<td>' + str(row['item_id']) + '</td>'
        tr +=       '<td>' + str(row['p_1']) + '</td>'
        tr +=       '<td>' + str(row['p_2']) + '</td>'
        tr +=       '<td>' + str(row['p_3']) + '</td>'
        tr +=       '<td>' + str(row['p_4']) + '</td>'
        tr +=       '<td>' + str(row['p_5']) + '</td>'
        tr +=       '<td>' + str(row['p_6']) + '</td>'
        tr +=       '<td>' + str(row['p_7']) + '</td>'
        tr +=       '<td>' + str(row['melt']) + '</td>'
        tr +=       '<td>' + str(row['wear']) + '</td>'
        tr +=   '<tr>'

    out =   '<table class="table_list">'
    out +=      '<tr>'
    out +=          '<th>№</th>'
    out +=          '<th>' + MODEL.weights[0][3] + '</th>'
    out +=          '<th>' + MODEL.weights[1][3] + '</th>'
    out +=          '<th>' + MODEL.weights[2][3] + '</th>'
    out +=          '<th>' + MODEL.weights[3][3] + '</th>'
    out +=          '<th>' + MODEL.weights[4][3] + '</th>'
    out +=          '<th>' + MODEL.weights[5][3] + '</th>'
    out +=          '<th>' + MODEL.weights[6][3] + '</th>'
    out +=          '<th>Кол-во плавок</th>'
    out +=          '<th>Износ, %</th>'
    out +=      '</tr>'
    out +=      tr
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
        nav_model = '',
        nav_alarm = '',
        nav_help = ''
    )
