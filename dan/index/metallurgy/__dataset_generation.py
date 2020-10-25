from jinja2 import Template
import json
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model
from index.metallurgy.classes.MetallurgyData import MetallurgyData

def dataset_generation(SITE):
    print('PATH -> index/metallurgy/dataset_generation.py')

    r = float(SITE.post['r'])/100
    MODEL = Model(SITE)
    rows = MODEL.datasetGenerator(k_rand=r)

    MD = MetallurgyData(SITE)
    rows = MD.getAll()
    tr = ''
    for row in rows:
        tr +=   '<tr>'
        tr +=       '<td>' + str(row['id']) + '</td>'
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


    answer = {'answer': 'success', 'content': out}
    return {'ajax': json.dumps(answer)}