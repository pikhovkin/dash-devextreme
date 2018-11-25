import dash
from dash.dependencies import Input, Output
import dash_html_components as html

import dash_devextreme as ddx


external_stylesheets=[
    'https://cdn3.devexpress.com/jslib/18.2.3/css/dx.common.css',
    'https://cdn3.devexpress.com/jslib/18.2.3/css/dx.light.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    ddx.TextBox(
        id='input',
        value='my-value',
        valueChangeEvent='input'
    ),
    html.Div(id='output'),
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
