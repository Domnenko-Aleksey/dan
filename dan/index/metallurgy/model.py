from jinja2 import Template

def model(SITE):
    print('PATH -> index/metallurgy/model.py')
    SITE.addHeadFile('/templates/index/metallurgy/model/model.css')

    html = open('templates/index/metallurgy/model/model.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Model')