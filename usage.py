import dash
from dash.dependencies import Input, Output
import dash_html_components as html

import dash_devextreme as ddx


external_stylesheets=[
    'https://cdn3.devexpress.com/jslib/18.2.3/css/dx.common.css',
    'https://cdn3.devexpress.com/jslib/18.2.3/css/dx.light.css'
]

dataSource = [
    {'language': 'English', 'percent': 55.5},
    {'language': 'Chinese', 'percent': 4.0},
    {'language': 'Spanish', 'percent': 4.3},
    {'language': 'Japanese', 'percent': 4.9},
    {'language': 'Portuguese', 'percent': 2.3},
    {'language': 'German', 'percent': 5.6},
    {'language': 'French', 'percent': 3.8},
    {'language': 'Russian', 'percent': 6.3},
    {'language': 'Italian', 'percent': 1.6},
    {'language': 'Polish', 'percent': 1.8}
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
    ddx.PieChart(
        type='doughnut',
        palette='Soft Pastel',
        title='Top Internet Languages',
        dataSource=dataSource,
        legend=dict(horizontalAlignment='center', verticalAlignment='bottom'),
        # export=dict(enabled=True),
        series=dict(
            smallValuesGrouping=dict(mode='topN', topCount=3),
            argumentField='language',
            valueField='percent',
            label=dict(
                visible=True,
                customizeText='valueText',
                format='fixedPoint',
                connector=dict(visible=True, width=1)
            )
        )
    ),
    html.Div(['Checked', ddx.CheckBox(id='CheckedOn', value=True)]),
    html.Div(['Unchecked', ddx.CheckBox(id='CheckedOff', value=False)]),
    # html.Div(['Indeterminate', ddx.CheckBox(value=None)]),
    html.Div(['Disabled', ddx.CheckBox(value=True, disabled=True)]),
    html.Div(ddx.CheckBox(text='Check', value=True, width=80)),
    html.Div(['Switched on', ddx.Switch(id='SwitchedOn', value=False)]),
    html.Div(['Switched off', ddx.Switch(value=False)]),
    # html.Div(['Value change handling', ddx.Switch(id='handlerSwitch', value=False)]),
    html.Div(['Disabled', ddx.Switch(id='disabledSwitch', value=False, disabled=True)]),
])


@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
