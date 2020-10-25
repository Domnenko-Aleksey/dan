from jinja2 import Template

def dataset_edit(SITE):
    print('PATH -> index/metallurgy/dataset_edit.py')
    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset_edit.css')

    html = open('templates/index/metallurgy/dataset/dataset_edit.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Dataset Edit')