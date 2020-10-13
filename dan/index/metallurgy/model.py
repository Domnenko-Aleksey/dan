from jinja2 import Template
import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Model import Model

def model(SITE):
    print('PATH -> index/metallurgy/model.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/model/model.css')

    MODEL = Model(SITE)
    MODEL.datasetGenerator()

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