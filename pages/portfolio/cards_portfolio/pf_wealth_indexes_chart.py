import dash_bootstrap_components as dbc
import dash_daq as daq
from dash import dcc, html, callback
from dash.dependencies import Input, Output

card_graf_portfolio = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dcc.Loading(
                        [
                            dcc.Graph(id="pf-wealth-indexes"),
                            daq.BooleanSwitch(
                                id="pf-logarithmic-scale-switch",
                                on=False,
                                label="Logarithmic Y-Scale",
                                labelPosition="bottom",
                            ),
                        ],
                    )
                ],
                id="portfolio_graf_div",
            )
        ]
    ),
    class_name="mb-3",
)


@callback(Output("portfolio_graf_div", "hidden"), Input("pf-submit-button", "n_clicks"))
def hide_graf(n_clicks):
    return n_clicks == 0
