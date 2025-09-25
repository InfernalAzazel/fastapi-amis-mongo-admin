from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ATransfer(AFormItem):
    """
    Transfer 穿梭器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/transfer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class PaginationConfig(BaseModel):
        className: Optional[str] = None
        """分页控件 CSS 类名"""

        enable: Optional[bool] = None
        """是否开启分页"""

        layout: Optional[Union[str, List[str]]] = None
        """
        - 分页结构布局
        - 默认值：["pager"]
        """

        perPageAvailable: Optional[List[int]] = None
        """
        - 指定每页可以显示多少条
        - 默认值：[10, 20, 50, 100]
        """

        maxButtons: Optional[int] = None
        """
        - 最多显示多少个分页按钮
        - 默认值：5
        """

        popOverContainerSelector: Optional[str] = None
        """切换每页条数的控件挂载点"""

    type: Literal["transfer", "transfer-picker", "tabs-transfer", "tabs-transfer-picker"] = "transfer"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimeter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    searchApi: Optional[API] = None
    """接口检索"""

    resultListModeFollowSelect: Optional[bool] = None
    """
    - 结果面板跟随模式
    - 默认值：false
    """

    statistics: Optional[bool] = None
    """
    - 是否显示统计数据
    - 默认值：true
    """

    selectTitle: Optional[str] = None
    """
    - 左侧的标题文字
    - 默认值："请选择"
    """

    resultTitle: Optional[str] = None
    """
    - 右侧结果的标题文字
    - 默认值："当前选择"
    """

    sortable: Optional[bool] = None
    """
    - 结果可以进行拖拽排序
    - 默认值：false
    """

    selectMode: Optional[str] = None
    """
    - 选择模式
    - 默认值：list
    """

    searchResultMode: Optional[str] = None
    """搜索结果展示形式"""

    searchable: Optional[bool] = None
    """
    - 左侧列表搜索功能
    - 默认值：false
    """

    searchPlaceholder: Optional[str] = None
    """左侧列表搜索框提示"""

    columns: Optional[List[Dict[str, Any]]] = None
    """展示哪些列"""

    leftOptions: Optional[List[Dict[str, Any]]] = None
    """左边的选项集"""

    leftMode: Optional[str] = None
    """左边的选择形式"""

    rightMode: Optional[str] = None
    """右边的选择形式"""

    resultSearchable: Optional[bool] = None
    """
    - 结果列表的检索功能
    - 默认值：false
    """

    resultSearchPlaceholder: Optional[str] = None
    """右侧列表搜索框提示"""

    menuTpl: SerializeAsAny[Optional[Union[str, SchemaNode]]] = None
    """自定义选项展示"""

    valueTpl: SerializeAsAny[Optional[Union[str, SchemaNode]]] = None
    """自定义值的展示"""

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度
    - 默认值：38
    """

    virtualThreshold: Optional[int] = None
    """
    - 虚拟渲染的阈值
    - 默认值：100
    """

    pagination: SerializeAsAny[Optional[PaginationConfig]] = None
    """分页配置"""

