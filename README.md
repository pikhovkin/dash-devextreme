# dash-devextreme

[![PyPI](https://img.shields.io/pypi/v/dash-devextreme.svg)](https://pypi.org/project/dash-devextreme/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dash_devextreme.svg)
[![NPM](https://img.shields.io/npm/v/dash-devextreme.svg)](https://www.npmjs.com/package/dash-devextreme)
[![PyPI - License](https://img.shields.io/pypi/l/dash-devextreme.svg)](./LICENSE)

Wrapper of [DevExtreme][] components for Plotly [Dash][]


### Installation

```bash
$ pip install dash_devextreme
```

### Usage

```python
import dash
import dash_devextreme as ddx
import dash_html_components as html


data = [
    {'id': 1, 'name': 'Sales', 'text': 'abc'},
    {'id': 2, 'parent_id': 1, 'name': 'Sales 1', 'text': 'abc'},
    {'id': 3, 'parent_id': 1, 'name': 'Sales 2', 'text': 'abc'},
    {'id': 4, 'name': 'Developers', 'text': 'abc'},
    {'id': 5, 'parent_id': 4, 'name': 'Dev 1', 'text': 'abc'},
]

app = dash.Dash('')
app.scripts.config.serve_locally = True

app.layout = html.Div(children=[
    ddx.TreeList(
        dataSource=data,
        columns=[
            {'dataField': 'name', 'width': 290},
            {'dataField': 'text'},
        ],
        keyExpr='id',
        parentIdExpr='parent_id',
        width='100%'
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
```

### Dash

Go to this link to learn about [Dash][].

See the [dash-component-boilerplate][] repo for more information.

### License

MIT

[DevExtreme]: https://js.devexpress.com/
[Dash]: https://github.com/plotly/dash
[dash-component-boilerplate]: https://github.com/plotly/dash-component-boilerplate
