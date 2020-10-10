from jinja2 import Template

def dataset_generation(SITE):
    print('PATH -> index/metallurgy/dataset_generation.py')

    SITE.addHeadFile('/templates/index/metallurgy/dataset/dataset_generation.css')

    html = open('templates/index/metallurgy/dataset/dataset_generation.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Dataset Generation')