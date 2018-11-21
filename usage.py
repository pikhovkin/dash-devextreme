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
            </script>
            
            <script type="text/jsx" data-presets="react">
                function dept_tree(props){
                    return <div><b id={"status_tree_" + props.data.id}>{props.value}</b><Tooltip showEvent="dxhoverstart" hideEvent="dxhoverend" target={"status_tree_" + props.data.id}><div><b>{props.data.dept}</b>:&nbsp;{props.data.director}</div></Tooltip></div>
                }
                
                function dept_table(props){
                    return <div><b id={"status_table_" + props.data.id}>{props.value}</b><Tooltip showEvent="dxhoverstart" hideEvent="dxhoverend" target={"status_table_" + props.data.id}><div><b>{props.data.dept}</b><br/>{props.data.director}</div></Tooltip></div>
                }
            </script>
        </footer>
    </body>
</html>'''


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
])

@app.callback(Output('output', 'children'), [Input('input', 'value')])
def display_output(value):
    return 'You have entered {}'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True)
