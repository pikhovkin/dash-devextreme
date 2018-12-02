import dash
from dash.dependencies import Input, Output
import dash_html_components as html

import dash_devextreme as ddx


data = [
    dict(id=1, parent_id=None, dept='Sales', director='Anna'),
    dict(id=2, parent_id=1, dept='Sales 1', director='Bella'),
    dict(id=3, parent_id=1, dept='Sales 2', director='Ganna'),
    dict(id=4, parent_id=None, dept='Developers', director='Donna'),
    dict(id=5, parent_id=4, dept='Developers N', director='Elly'),
]
columns = [
    dict(caption='Department', dataField='dept', cellTemplate='dept_tree'),
    dict(caption='Director', dataField='director'),
]
columns_table = [
    dict(caption='Department', dataField='dept', cellTemplate='dept_table'),
    dict(caption='Director', dataField='director'),
]

pieDataSource = [
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

_default_index = '''<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <link rel="stylesheet" media="all" href="https://cdn3.devexpress.com/jslib/18.2.3/css/dx.common.css">
        <link rel="stylesheet" media="all" href="https://cdn3.devexpress.com/jslib/18.2.3/css/dx.light.css">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            
            <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
            
            {%scripts%}
            
            <script>
                window.Tooltip = dash_devextreme.Tooltip;
                window.Popover = dash_devextreme.Popover;
                window.TabPanel = dash_devextreme.TabPanel;
            </script>
            
            <script type="text/jsx" data-presets="react">
                function dept_tree(props){
                    return <div><b id={"status_tree_" + props.data.id}>{props.value}</b><Tooltip showEvent="dxhoverstart" hideEvent="dxhoverend" target={"status_tree_" + props.data.id}><div><b>{props.data.dept}</b>:&nbsp;{props.data.director}</div></Tooltip></div>
                }
                
                function dept_table(props){
                    return <div><b id={"status_table_" + props.data.id}>{props.value}</b><Popover showEvent="dxhoverstart" hideEvent="dxhoverend" target={"status_table_" + props.data.id} showTitle={true} title={props.data.dept} width={200}><div>{props.data.director}</div></Popover></div>
                }
                
                function tp_title(props){
                    return <b>{props.dept}</b>
                }
                
                function tp_sub_panel(props){
                    return <span>Director: <b>{props.director}</b></span>
                }
                
                function tp_panel(props){
                    return <div>
                        <div>{props.director}</div>
                        <TabPanel items={[props]} itemTitleTemplate="tp_title" itemTemplate="tp_sub_panel" />
                    </div>
                }
                
                function pie_chart(point) {
                    return `${point.argumentText}: ${point.valueText}%`;
                }
            </script>
        </footer>
    </body>
</html>'''
#

app = dash.Dash(__name__, index_string=_default_index)
app.scripts.config.serve_locally = True
app.css.config.serve_locally = True

app.layout = html.Div([
    ddx.TextBox(
        id='input',
        value='my-value',
        valueChangeEvent='input'
    ),
    html.Div(id='output'),
    ddx.TreeList(dataSource=data, columns=columns, keyExpr='id', parentIdExpr='parent_id'),
    ddx.DataGrid(dataSource=data, columns=columns_table),
    ddx.TabPanel(items=data, itemTitleTemplate='tp_title', itemTemplate='tp_panel'),
    ddx.PieChart(
        type='doughnut',
        palette='Soft Pastel',
        title='Top Internet Languages',
        dataSource=pieDataSource,
        legend=dict(horizontalAlignment='center', verticalAlignment='bottom'),
        export=dict(enabled=True),
        series=dict(
            smallValuesGrouping=dict(mode='topN', topCount=3),
            argumentField='language',
            valueField='percent',
            label=dict(
                visible=True,
                format='fixedPoint',
                customizeText='pie_chart',
                connector=dict(visible=True, width=1)
            )
        )
    )
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
