from fastapi_amis_admin.amis.data_display.remark import *
from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.other import ABadge
from fastapi_amis_admin.amis.types import *



class ATable2(AmisNode):
    """
    Table2 表格

    表格展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
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

    sticky: Optional[bool] = None
    """
    - 是否粘性头部
    - 默认值：false
    """

    footer: SerializeAsAny[Optional[Union[str, SchemaNode]]] = None
    """表格尾部"""

    loading: Optional[bool] = None
    """表格是否加载中"""

    columnsTogglable: Optional[Union[Literal['auto'], bool]] = None
    """
    - 展示列显示开关, 自动即：列数量大于或等于 5 个时自动开启
    - 默认值：'auto'
    """

    placeholder: SerializeAsAny[Optional[Union[str, SchemaNode]]] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：暂无数据
    """

    rowSelection: SerializeAsAny[Optional["ATableSelections2"]] = None
    """行相关配置"""

    rowClassNameExpr: Optional[Union[str, Template]] = None
    """行 CSS 类名，支持模版语法"""

    expandable: SerializeAsAny[Optional["ATableExpandable2"]] = None
    """展开行配置"""

    lineHeight: Optional[Union[Literal['large', 'middle']]] = None
    """行高设置"""

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

    columns:  SerializeAsAny[Optional[List[Union["ATableColumn2", SchemaNode]]]] = None
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

    prefixRow: Optional[list] = None
    """顶部总结行"""

    affixRow: Optional[list] = None
    """底部总结行"""

    itemBadge: SerializeAsAny[Optional["ABadge"]] = None
    """行角标配置"""

    autoFillHeight: Optional[Union[bool, dict]] = None
    """内容区域自适应高度，可选择自适应、固定高度和最大高度"""

    lazyRenderAfter: Optional[int] = None
    """
    - 默认数据超过 100 条启动懒加载提升渲染性能，也可通过自定义该属性调整数值
    - 默认值：100
    """




class ATableRow2(AmisNode):
    """
    行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Optional[Literal['checkbox', 'radio']] = None
    """
    - 指定单选还是多选
    - 默认值：'checkbox'
    """

    fixed: Optional[Literal['left','right']] = None
    """选择列是否固定，只能左侧固定"""

    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """

    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""

    selections: SerializeAsAny[Optional["ATableSelections2"]] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""

    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""

    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""

    columnWidth: Optional[int] = None
    """自定义选择列列宽"""

    rowClick:  Optional[bool] = None
    """单条任意区域选中"""

class ATableSelections2(AmisNode):
    """
    展开行配置属性表

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    key: Optional[Literal['all','invert', 'none','odd', 'even']] = None
    """
    - 菜单类型，内置全选、反选、取消选择、选择奇数项、选择偶数项
    - 默认值：'all'
    """

    text: Optional[str] = None
    """自定义菜单项文本"""

class ATableExpandable2(AmisNode):
    """
    展开行配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%B1%95%E5%BC%80%E8%A1%8C%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    expandableOn: Optional[str] = None
    """指定可展开的行，要用 表达式"""

    keyField: Optional[str] = None
    """
    - 对应数据源的 key 值，默认是key，可指定为id、shortId等
    - 默认值：'key'
    """

    disableOn: Optional[str] = None
    """当前行是否可选择条件，要用 表达式"""

    selections: SerializeAsAny[Optional[ATableSelections2]] = None
    """自定义筛选菜单，内置all（全选）、invert（反选）、none（取消选择）、odd（选择奇数项）、even（选择偶数项）"""

    selectedRowKeys: Optional[Union[list[int], list[str]]] = None
    """已选择项"""

    selectedRowKeysExpr: Optional[str] = None
    """已选择项正则表达式"""

    columnWidth: Optional[int] = None
    """自定义选择列列宽"""

class ATableColumn2(AmisNode):
    """
    列配置属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table2#%E5%88%97%E9%85%8D%E7%BD%AE%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: Optional[str] = None
    """Literal['text','audio','image','link','tpl','mapping','carousel','date', 'progress','status','switch','list','json','operation','tag']"""

    label: Optional[Template] = None
    """标题文本内容"""

    name: Optional[str] = None
    """按名称关联数据"""

    fixed: Optional[Literal['left','right']] = None
    """是否修复当前列"""

    popOver: Optional[Union[bool, dict]] = None
    """弹出框"""

    quickEdit: Optional[Union[bool, dict]] = None
    """快速编辑"""

    copyable: Optional[Union[bool, dict]] = None
    """
    - 是否可复制
    - 默认值：{icon: string, content:string}
    """
    sortable: Optional[bool] = None
    """
    - 是否可排序
    - 默认值：False 
    """

    searchable: SerializeAsAny[Optional[Union[bool, SchemaNode]]] = None
    """
    - 是否快速搜索 boolean|图式
    - 默认值：False 
    """

    width: Optional[Union[int, str]] = None
    """默认值：列宽"""

    remark: Optional[ARemarkT] = None
    """提示消息"""






