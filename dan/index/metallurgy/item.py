from jinja2 import Template

def item(SITE):
    print('PATH -> index/metallurgy/item.py')
    SITE.addHeadFile('/templates/index/metallurgy/item/item.css')

    html = open('templates/index/metallurgy/item/item.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Item')