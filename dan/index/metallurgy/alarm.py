from jinja2 import Template

def alarm(SITE):
    print('PATH -> index/metallurgy/alarm.py')
    SITE.addHeadFile('/templates/index/metallurgy/alarm/alarm.css')

    html = open('templates/index/metallurgy/alarm/alarm.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Alarm')