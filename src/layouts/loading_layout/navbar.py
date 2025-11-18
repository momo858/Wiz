from dash import dcc, html

import dash_bootstrap_components as dbc

##==================================
## Navigation bar
##==================================
navbar = dbc.NavbarSimple(
    [
        dbc.Nav(
            dbc.Row(
                [
                    # Navigation
                    dbc.NavItem(dbc.NavLink('Lines', href='/')),
                    dbc.NavItem(dbc.NavLink('PCA/LDA', href='/pca')),
                 ],
                 align="center",
                 className="g-0",
            ),
        fill = True
        ),
    ],
    brand='  ',
    brand_href="#",
    color="primary",
    id='navBar',
    
    dark = True,
)

def get():
    return navbar
