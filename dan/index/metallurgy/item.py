import sys
sys.path.append('index/metallurgy/classes')
from index.metallurgy.classes.Catalog import Catalog
from index.metallurgy.classes.MetallurgyData import MetallurgyData
from jinja2 import Template

def item(SITE):
    print('PATH -> index/metallurgy/item.py')
    SITE.addHeadFile('/templates/index/metallurgy/item/item.css')

    CATALOG = Catalog(SITE)
    # catalog_rows = CATALOG.getItems(SITE.section_id)

    DATA = MetallurgyData(SITE)
    # data_rows = CATALOG.getItems(SITE.item_id)

    html = open('templates/index/metallurgy/item/item.tmpl').read()
    template = Template(html)
    SITE.content += template.render(name='Item')