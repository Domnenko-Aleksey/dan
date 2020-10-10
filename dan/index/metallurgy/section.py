from jinja2 import Template

def section(SITE):
    print('PATH -> index/metallurgy/section.py')
    SITE.addHeadFile('/templates/index/metallurgy/section/section.css')

    html = open('templates/index/metallurgy/section/section.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Section')