from fastapi_amis_admin.amis.data_input.form import AForm
from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class ACRUD(AmisNode):
    """
    CRUD 增删改查

    CRUD，即增删改查组件，主要用来展现数据列表，并支持各类【增】【删】【改】【查】等操作。

    注意 CRUD 所需的数据必须放 items 中，因此如果只是想显示表格类型的数据没有分页，请使用 Table。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/crud#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(BaseAmisModel):
        fetchFailed: Optional[str] = None
        """获取失败时提示"""

        saveOrderFailed: Optional[str] = None
        """保存顺序失败提示"""

        saveOrderSuccess: Optional[str] = None
        """保存顺序成功提示"""

        quickSaveFailed: Optional[str] = None
        """快速保存失败提示"""

        quickSaveSuccess: Optional[str] = None
        """快速保存成功提示"""

    type: str ='crud'

    mode: Optional[Literal['table', 'cards', 'list']] = None
    """
    - 模式
    - 默认值：'table'
    """

    title: Optional[str] = None
    """
    - 可设置成空，当设置成空时，没有标题栏
    - 默认值：""
    """

    className: Optional[str] = None
    """表格外层 Dom 的类名"""

    api: Optional[API] = None
    """CRUD 用来获取列表数据的 api。"""

    deferApi: Optional[API] = None
    """当行数据中有 defer 属性时，用此接口进一步加载内容"""

    loadDataOnce: Optional[bool] = None
    """是否一次性加载所有数据（前端分页）"""

    loadDataOnceFetchOnFilter: Optional[bool] = None
    """
    - 在开启 loadDataOnce 时，filter 时是否去重新请求 api
    - 默认值：true
    """

    source: Optional[str] = None
    """数据映射接口返回某字段的值，不设置会默认使用接口返回的${items}或者${rows}，也可以设置成上层数据源的内容"""

    filter: SerializeAsAny[Optional[Union[SchemaNode, AForm]]] = None
    """设置过滤器，当该表单提交后，会把数据带给当前 mode 刷新列表"""

    filterTogglable: Optional[Union[bool, Dict[str, str]]] = None
    """
    - 是否可显隐过滤器
    - 类型：boolean | {label: string; icon: string; activeLabel: string; activeIcon?: stirng;}
    - 默认值：false
    """

    filterDefaultVisible: Optional[bool] = None
    """
    - 设置过滤器默认是否可见。
    - 默认值：true
    """

    initFetch: Optional[bool] = None
    """
    - 是否初始化的时候拉取数据
    - 默认值：true
    """

    interval: Optional[int] = None
    """
    - 刷新时间(最低 1000)
    - 默认值：3000
    """

    silentPolling: Optional[bool] = None
    """
    - 配置刷新时是否隐藏加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[str] = None
    """通过表达式来配置停止刷新的条件"""

    stopAutoRefreshWhenModalIsOpen: Optional[bool] = None
    """
    - 当有弹框时关闭自动刷新
    - 默认值：false
    """

    syncLocation: Optional[bool] = None
    """
    - 是否将过滤条件的参数同步到地址栏
    - 默认值：true
    """

    draggable: Optional[bool] = None
    """
    - 是否可通过拖拽排序
    - 默认值：false
    """

    resizable: Optional[bool] = None
    """
    - 是否可以调整列宽度
    - 默认值：true
    """

    itemDraggableOn: Optional[bool] = None
    """用表达式来配置是否可拖拽排序"""

    saveOrderApi: Optional[API] = None
    """保存排序的 api。"""

    quickSaveApi: Optional[API] = None
    """快速编辑后用来批量保存的 API。"""

    quickSaveItemApi: Optional[API] = None
    """快速编辑配置成及时保存时使用的 API。"""

    bulkActions: SerializeAsAny[Optional[List[AAction]]] = None
    """批量操作列表"""

    messages: SerializeAsAny[Optional[Messages]] = None
    """覆盖消息提示"""

    primaryField: Optional[str] = None
    """
    - 设置 ID 字段名。
    - 默认值："id"
    """

    perPage: Optional[int] = None
    """
    - 设置一页显示多少条数据。
    - 默认值：10
    """

    orderBy: Optional[str] = None
    """默认排序字段"""

    orderDir: Optional[str] = None
    """排序方向"""

    defaultParams: Optional[Dict[str, Any]] = None
    """设置默认 filter 默认参数"""

    pageField: Optional[str] = None
    """
    - 设置分页页码字段名。
    - 默认值："page"
    """

    perPageField: Optional[str] = None
    """
    - 设置分页一页显示的多少条数据的字段名。
    - 默认值："perPage"
    """

    pageDirectionField: Optional[str] = None
    """
    - 分页方向字段名
    - 默认值："pageDir"
    """

    perPageAvailable: Optional[List[int]] = None
    """
    - 设置一页显示多少条数据下拉框可选条数。
    - 默认值：[5, 10, 20, 50, 100]
    """

    orderField: Optional[str] = None
    """设置用来确定位置的字段名"""

    hideQuickSaveBtn: Optional[bool] = None
    """
    - 隐藏顶部快速保存提示
    - 默认值：false
    """

    autoJumpToTopOnPagerChange: Optional[bool] = None
    """
    - 当切分页的时候，是否自动跳顶部。
    - 默认值：false
    """

    syncResponse2Query: Optional[bool] = None
    """
    - 将返回数据同步到过滤器上。
    - 默认值：true
    """

    keepItemSelectionOnPageChange: Optional[bool] = None
    """
    - 保留条目选择
    - 默认值：true
    """

    labelTpl: Optional[str] = None
    """单条描述模板"""

    maxKeepItemSelectionLength: Optional[int] = None
    """限制最大勾选数"""

    maxItemSelectionLength: Optional[int] = None
    """限制当前页的最大勾选数"""

    headerToolbar: Optional[List[str]] = None
    """
    - 顶部工具栏配置
    - 默认值：['bulkActions', 'pagination']
    """

    footerToolbar: Optional[List[str]] = None
    """
    - 底部工具栏配置
    - 默认值：['statistics', 'pagination']
    """

    alwaysShowPagination: Optional[bool] = None
    """
    - 是否总是显示分页
    - 默认值：false
    """

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

    autoGenerateFilter: Optional[Union[Dict[str, Any], bool]] = None
    """是否开启查询区域"""

    resetPageAfterAjaxItemAction: Optional[bool] = None
    """
    - 单条数据 ajax 操作后是否重置页码为第一页
    - 默认值：false
    """

    autoFillHeight: Optional[Union[bool, Dict[str, int]]] = None
    """
    - 内容区域自适应高度
    - 类型：boolean 丨 {height: number}
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 是否可以自动获取上层的数据并映射到表格行数据上
    - 默认值：true
    """

    matchFunc: Optional[str] = None
    """自定义匹配函数"""

    parsePrimitiveQuery: Optional[Any] = None
    """
    - 是否开启 Query 信息转换
    - 默认值：true
    """

    itemAction: SerializeAsAny[Optional[AAction]] = None
    """点击一行后实现自定义动作，支持所有配置在操作中"""
