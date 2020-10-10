from jinja2 import Template

def dashboard(SITE):
    print('PATH -> index/metallurgy/dashboard.py')
    SITE.addHeadFile('/templates/index/metallurgy/dashboard/dashboard.css')

    html = open('templates/index/metallurgy/dashboard/dashboard.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Dashboard')