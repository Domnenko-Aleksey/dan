from jinja2 import Template

def dataset(SITE):
    print('PATH -> index/metallurgy/dataset.py')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset.css')

    html = open('templates/index/metallurgy/dataset/dataset.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Dataset')
