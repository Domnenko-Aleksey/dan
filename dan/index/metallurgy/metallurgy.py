from aiohttp import web
import sys
sys.path.append('index/metallurgy')
from dashboard import dashboard
from section import section
from item import item
from dataset import dataset
from dataset_generation import dataset_generation
from model_lr import model_lr
from model_dff import model_dff
from input_data import input_data
from alarm import alarm
from help_page import help_page

def metallurgy(SITE):
    print('PATH -> index/metallurgy/metallurgy.py')
    SITE.section_id = 1

    functions = {
        '': dashboard,
        'section': section,
        'item': item,
        'dataset': dataset,
        'dataset_generation': dataset_generation,
        'model_lr': model_lr,  # Линейная регрессия (lr)
        'model_dff': model_dff,  # Полносвязная сеть прямого распространения Deep Feed Forward (dff)
        'input_data': input_data,
        'alarm': alarm,
        'help': help_page
    }

    if (SITE.p[1] not in functions):
        raise web.HTTPNotFound()

    return functions[SITE.p[1]](SITE)