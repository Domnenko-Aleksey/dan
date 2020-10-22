from jinja2 import Template

def help_page(SITE):
    print('PATH -> index/metallurgy/hel_page.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/help/help.css')
    
    html_help = open('templates/index/metallurgy/help/help.html', 'r', encoding='utf-8').read()
    help = Template(html_help)
    render_help = help.render(tmpl_body=html_help)

    html_default = open('templates/index/metallurgy/default/default.html', 'r', encoding='utf-8').read()
    default = Template(html_default)

    SITE.content += default.render(
        tmpl_body = render_help, 
        nav_home = '', 
        nav_factory = '',
        nav_database = '',
        nav_model_dff = '',
        nav_model_lr = '',
        nav_alarm = '',
        nav_help = 'active'
    )