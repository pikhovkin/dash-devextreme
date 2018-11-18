import React, {Component} from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';

import {TreeList as DXTreeList} from 'devextreme-react';


export default class TreeList extends Component {
    constructor(props) {
        super(props);

        this.cellTemplate = this.cellTemplate.bind(this);
        this.headerCellTemplate = this.headerCellTemplate.bind(this);
        this._processCellTemplate = this._processCellTemplate.bind(this);
    }

    cellTemplate(template_id) {
        var tmpl = window[template_id];
        return function(container, options) {
            ReactDOM.render(tmpl(options), container);
        }
    }

    headerCellTemplate(template_id) {
        var tmpl = window[template_id];
        return function(container, options) {
            ReactDOM.render(tmpl(options), container);
        }
    }

    _processCellTemplate(columns) {
        for(const c in columns){
            if (columns[c].cellTemplate && typeof columns[c].cellTemplate === 'string') {
                columns[c].cellTemplate = this.cellTemplate(columns[c].cellTemplate);
            }
            if (columns[c].headerCellTemplate && typeof columns[c].headerCellTemplate === 'string') {
                columns[c].headerCellTemplate = this.headerCellTemplate(columns[c].headerCellTemplate);
            }
            if (columns[c].columns && typeof columns[c].columns === 'object') {
                this._processCellTemplate(columns[c].columns);
            }
        }
    }

    render() {
        const { columns } = this.props;

        this._processCellTemplate(columns);

        return (
            <DXTreeList
                id={this.props.id}
                dataSource={this.props.dataSource}
                columns={columns}
                keyExpr={this.props.keyExpr}
                parentIdExpr={this.props.parentIdExpr}
                showColumnHeaders={this.props.showColumnHeaders}
                showColumnLines={this.props.showColumnLines}
                showRowLines={this.props.showRowLines}
                showBorders={this.props.showBorders}
                columnWidth={this.props.columnWidth}
                columnMinWidth={this.props.columnMinWidth}
                columnAutoWidth={this.props.columnAutoWidth}
                allowColumnResizing={this.props.allowColumnResizing}
                disabled={this.props.disabled}
                columnResizingMode={this.props.columnResizingMode}
                dataStructure={this.props.dataStructure}
                scrolling={this.props.scrolling}
                paging={this.props.paging}
                pager={this.props.pager}
                sorting={this.props.sorting}
                height={this.props.height}
                width={this.props.width}
                visible={this.props.visible}
                wordWrapEnabled={this.props.wordWrapEnabled}
            />
        );
    }
}

TreeList.propTypes = {
    id: PropTypes.string,

    dataSource: PropTypes.object,
    columns: PropTypes.arrayOf(PropTypes.shape),
    keyExpr: PropTypes.string,
    parentIdExpr: PropTypes.string,
    showColumnHeaders: PropTypes.bool,
    showColumnLines: PropTypes.bool,
    showRowLines: PropTypes.bool,
    showBorders: PropTypes.bool,
    columnWidth: PropTypes.number,
    columnMinWidth: PropTypes.number,
    columnAutoWidth: PropTypes.bool,
    allowColumnResizing: PropTypes.bool,
    disabled : PropTypes.bool,
    columnResizingMode: PropTypes.oneOf(['nextColumn', 'widget']),
    dataStructure : PropTypes.oneOf(['plain', 'tree']),
    scrolling: PropTypes.object,
    paging: PropTypes.object,
    pager: PropTypes.object,
    sorting: PropTypes.object,
    height: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.func]),
    width: PropTypes.oneOfType([PropTypes.string, PropTypes.number, PropTypes.func]),
    visible: PropTypes.bool,
    wordWrapEnabled: PropTypes.bool,

    // Dash supplied props
    setProps: PropTypes.func
};

TreeList.defaultProps = {
    columnAutoWidth: true,
    allowColumnResizing: false,
    columnResizingMode: 'nextColumn',
    dataStructure: 'plain',
    disabled: false,
    visible: true,
    wordWrapEnabled: false,
};
