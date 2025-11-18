from dash import dcc, html

import dash_bootstrap_components as dbc

##==================================
## Navigation bar
##==================================
download_link = html.A(
    'Download Plot Data',
    id = 'lines-download-link',
    href = '',
    style = dict(color = 'white'),
    className= 'downloadlink'
),

navbar = dbc.NavbarSimple(
    [
        dbc.Nav(
            dbc.Row(
                [
                    dbc.NavItem(dbc.NavLink('Clear Data',id='clear-data-link',href='/temp-clear')),
                    dbc.NavItem(dbc.NavLink(download_link),id='lines-dowload-nav'),
                    dbc.NavItem(dbc.NavLink('Data Table',id='lines-table-open'), style = dict(cursor = 'pointer')),
                    dbc.NavItem(dbc.NavLink('PCA/LDA', href='/pca')),
                 ],
                 align = 'center',
                 className="g-0"
            ),
        ),
    ],
    brand = '   ',
    brand_href = '/',
    expand = 'lg',
    color="primary",
    id='navBar',
    
    dark = True,
)

def get():
    return navbar
