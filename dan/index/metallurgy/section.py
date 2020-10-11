import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Catalog import Catalog
from jinja2 import Template

def section(SITE):
    print('PATH -> index/metallurgy/section.py')
    SITE.addHeadFile('/templates/index/metallurgy/section/section.css')

    CATALOG = Catalog(SITE)
    rows = CATALOG.getItems(SITE.section_id)

    tr_row = ''
    if (rows):
        i = 1
        for row in rows:
            print(row)
            tr_row +=  f'''<tr>
                <td>{ i }</td>
                <td><a href="/system/catalog/item/edit/{ row['id'] }">{ row['name'] }</a></td>
            </tr>'''
            i += 1

    table_out = '<table>' + tr_row + '</table>'



    html = open('templates/index/metallurgy/section/section.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name=table_out)