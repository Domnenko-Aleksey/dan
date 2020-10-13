from jinja2 import Template
import json
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model

def dataset_generation(SITE):
    print('PATH -> index/metallurgy/dataset_generation.py')

    r = float(SITE.post['r'])/100
    MODEL = Model(SITE)
    out = MODEL.datasetGenerator(k_rand=r)

    answer = {'answer': 'success', 'content': out}
    return {'ajax': json.dumps(answer)}