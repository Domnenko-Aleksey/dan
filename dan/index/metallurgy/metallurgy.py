from aiohttp import web
import sys
sys.path.append('index/metallurgy')
from dashboard import dashboard
from section import section
from item import item
from dataset import dataset
from dataset_edit import dataset_edit
from dataset_delete import dataset_delete
from dataset_update import dataset_update
from dataset_generation import dataset_generation
from model import model
from input_data import input_data
from alarm import alarm

def metallurgy(SITE):
    print('PATH -> index/metallurgy/metallurgy.py')
    SITE.section_id = 1

    functions = {
        '': dashboard,
        'section': section,
        'item': item,
        'dataset': dataset,
        'dataset_add': dataset_edit,
        'dataset_edit': dataset_edit,
        'dataset_update': dataset_update,
        'dataset_delete': dataset_delete,
        'dataset_generation': dataset_generation,
        'model': model,
        'input_data': input_data,
        'alarm': alarm
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    return functions[SITE.p[1]](SITE)