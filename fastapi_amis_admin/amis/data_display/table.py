from fastapi_amis_admin.amis.data_display.remark import *
from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.function.popover import APopOver
from fastapi_amis_admin.amis.other import ABadge
from fastapi_amis_admin.amis.types import *
from pydantic import SerializeAsAny


class ATable(AmisNode):
    """
    Table 表格

    表格展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "table"
    """"type" 指定为 table 渲染器"""

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """
    - 数据源, 绑定当前环境变量
    - 默认值：${items}
    """

    deferApi: Optional[API] = None
    """当行数据中有 defer 属性时，用此接口进一步加载内容"""

    affixHeader: Optional[bool] = None
    """
    - 是否固定表头
    - 默认值：true
    """

    affixFooter: Optional[bool] = None
    """
    - 是否固定表格底部工具栏
    - 默认值：false
    """

    columnsTogglable: Union[bool, str, None] = None
    """
    - 展示列显示开关, 自动即：列数量大于或等于 5 个时自动开启
    - 默认值：auto
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """
    - 外层 CSS 类名
    - 默认值：'panel-default'
    """

    tableClassName: Optional[str] = None
    """
    - 表格 CSS 类名
    - 默认值：'table-db table-striped'
    """

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：'Action.md-table-header'
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：'Action.md-table-footer'
    """

    toolbarClassName: Optional[str] = None
    """ 
    - 工具栏 CSS 类名	
    - 默认值：'Action.md-table-toolbar'
    """

    columns: SerializeAsAny[Optional[List[Union["ATableColumn", SchemaNode]]]] = None
    """用来设置列信息"""

    combineNum: Optional[int] = None
    """自动合并单元格"""

    itemActions: SerializeAsAny[Optional[List[AAction]]] = None
    """悬浮行操作按钮组"""

    itemCheckableOn: Optional[Expression] = None
    """配置当前行是否可勾选的条件，要用 表达式"""

    itemDraggableOn: Optional[Expression] = None
    """配置当前行是否可拖拽的条件，要用 表达式"""

    checkOnItemClick: Optional[bool] = None
    """
    - 点击数据行是否可以勾选当前行
    - 默认值：false
    """

    rowClassName: Optional[str] = None
    """给行添加 CSS 类名"""

    rowClassNameExpr: Optional[Template] = None
    """通过模板给行添加 CSS 类名"""

    prefixRow: Optional[list] = None
    """顶部总结行"""

    affixRow: Optional[list] = None
    """底部总结行"""

    itemBadge: SerializeAsAny[Optional["ABadge"]] = None
    """行角标配置"""

    autoFillHeight: Optional[bool] = None
    """内容区域自适应高度，可选择自适应、固定高度和最大高度"""

    resizable: Optional[bool] = None
    """
    - 列宽度是否支持调整
    - 默认值：true
    """

    selectable: Optional[bool] = None
    """
    - 支持勾选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 勾选 icon 是否为多选样式checkbox， 默认为radio	
    - 默认值：false
    """

    lazyRenderAfter: Optional[int] = None
    """
    - 用来控制从第几行开始懒渲染行，用来渲染大表格时有用
    - 默认值：100
    """

    tableLayout: Optional[Literal['auto', 'fixed']] = None
    """
    - 当配置为 fixed 时，内容将不会撑开表格，自动换行
    - 默认值：'auto'
    """

    footable: Union[bool, dict, None] = None
    """是否开启底部展示功能，适合移动端展示"""



class ATableColumn(AmisNode):
    """
    列配置属性表
    """
    type: Optional[str] = None
    """Literal['text','audio','image','link','tpl','mapping','carousel','date', 'progress','status','switch','list','json','operation','tag']"""

    label: Optional[Template] = None
    """标题文本内容"""

    name: Optional[str] = None
    """按名称关联数据"""

    width: Optional[Union[int, str]] = None
    """默认值：列宽"""

    remark: Optional[ARemarkT] = None
    """提示消息"""

    fixed: Optional[Literal['left','right']] = None
    """是否修复当前列"""

    popOver: SerializeAsAny[Optional[Union[str, 'APopOver']]] = None
    """弹出框"""

    copyable: Optional[Union[bool, dict]] = None
    """
    - 是否可复制
    - 默认值：{icon: string, content:string}
    """

    style: Optional[str] = None
    """单元格自定义样式"""

    innerStyle: Optional[str] = None
    """单元格内部组件自定义样式"""