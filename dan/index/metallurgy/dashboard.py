from jinja2 import Template

def dashboard(SITE):
    print('PATH -> index/metallurgy/dashboard.py')
    SITE.addHeadFile('/templates/index/metallurgy/default/default.css')
    SITE.addHeadFile('/templates/index/metallurgy/dashboard/dashboard.css')

    html_dashboard = open('templates/index/metallurgy/dashboard/dashboard.html', 'r', encoding='utf-8').read()
    dashboard = Template(html_dashboard)
    render_dashboard = dashboard.render(tmpl_body=html_dashboard)

    html_default = open('templates/index/metallurgy/default/default.html', 'r', encoding='utf-8').read()
    default = Template(html_default)

    SITE.content += default.render(
        tmpl_body = render_dashboard, 
        nav_home = 'active', 
        nav_factory = '',
        nav_database = '',
        nav_model = '',
        nav_alarm = '',
        nav_help = ''
    )