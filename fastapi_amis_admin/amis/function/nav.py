from fastapi_amis_admin.amis.other import ABadge
from fastapi_amis_admin.amis.types import *


class ANav(AmisNode):
    """
    Nav 导航

    用于展示链接导航

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Overflow(AmisNode):
        enable: Optional[bool] = None
        """
        - 是否开启响应式收纳
        - 默认值：false
        """

        overflowLabel: Optional[Union[str, dict]] = None
        """菜单触发按钮的文字"""

        overflowIndicator: Optional[str] = None
        """
        - 菜单触发按钮的图标
        - 默认值：'fa fa-ellipsis'
        """

        maxVisibleCount: Optional[int] = None

        """开启响应式收纳后导航最大可显示数量，超出此数量的导航将被收纳到下拉菜单中，默认为自动计算"""
        wrapperComponent: Optional[str] = None

        """包裹导航的外层标签名，可以使用其他标签渲染"""
        style: Optional[dict] = None
        """自定义样式"""

        overflowClassName: Optional[dict] = None
        """菜单按钮 CSS 类名"""

        overflowPopoverClassName: Optional[dict] = None
        """Popover 浮层 CSS 类名"""

    class Link(AmisNode):
        label: Optional[str] = None
        """名称"""

        to: Optional[Template] = None
        """链接地址"""

        target: Optional[str] = None
        """链接关系"""

        icon: Optional[str] = None
        """图标"""

        children: SerializeAsAny[Optional[List['ANav.Link']]] = None
        """子链接"""

        unfolded: Optional[bool] = None
        """初始是否展开"""

        active: Optional[bool] = None
        """是否高亮"""

        activeOn: Optional[Expression] = None
        """是否高亮的条件，留空将自动分析链接地址"""

        defer: Optional[bool] = None
        """标记是否为懒加载项"""

        deferApi: Optional[API] = None
        """可以不配置，如果配置优先级更高"""

        disabled: Optional[bool] = None
        """是否禁用"""

        disabledTip: Optional[str] = None
        """禁用提示信息"""

        className: Optional[str] = None
        """菜单项自定义样式"""

        mode: Optional[Literal['group', 'divider']] = None
        """菜菜单项模式，分组模式、分割线"""

        overflow: SerializeAsAny[Optional['ANav.Overflow']] = None
        """导航项响应式收纳配置"""


    class NavMatchFunc(AmisNode):
        link: SerializeAsAny[Optional[List['ANav.Link']]] = None
        """导航项对象"""

        keyword: Optional[str] = None
        """搜索关键字"""

    class SearchConfig(AmisNode):
        matchFunc: SerializeAsAny[Optional['ANav.NavMatchFunc']] = None
        """自定义匹配函数, 默认模糊匹配导航对象中的label, title 和 key 字段"""

        className: Optional[str] = None
        """搜索框外层 CSS 类名"""

        placeholder: Optional[bool] = None
        """
        - 是否开启搜索
        - 默认值：'false'
        """

        mini: Optional[bool] = None
        """
        - 是否为 mini 模式
        - 默认值：'false'
        """

        enhance: Optional[bool] = None
        """
        - 是否为增强样式
        - 默认值：'false'
        """

        clearable: Optional[bool] = None
        """
        - 是否开启搜索
        - 默认值：'false'
        """

        searchImediately: Optional[bool] = None
        """
        - 是否立即搜索
        - 默认值：'false'
        """


    type: str = "nav"
    """指定为 Nav 渲染器"""

    mode: Optional[str] = None
    """
    - 导航模式，悬浮或者内联，默认内联模式	
    - 默认值：'inline'
    """

    collapsed: Optional[bool] = None
    """控制导航是否缩起"""

    indentSize: Optional[int] = None
    """
    - 层级缩进值，仅内联模式下生效
    - 默认值：16
    """

    level: Optional[int] = None
    """控制导航最大展示层级数"""

    defaultOpenLevel: Optional[int] = None
    """控制导航最大默认展开层级"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    popupClassName: Optional[str] = None
    """当为悬浮模式时，可自定义悬浮层样式"""

    expandIcon: Optional[Union[str, dict]] = None
    """自定义展开按钮"""

    expandPosition: Optional[Literal['before', 'after']] = None
    """展开按钮位置，不设置默认在前面	"""

    stacked: Optional[bool] = None
    """
    - 设置成 false 可以以 tabs 的形式展示
    - 默认值：true
    """

    accordion: Optional[bool] = None
    """是否开启手风琴模式"""

    source: Optional[API] = None
    """可以通过变量或 API 接口动态创建导航"""

    deferApi: Optional[API] = None
    """用来延时加载选项详情的接口，可以不配置，不配置公用 source 接口"""

    itemActions: SerializeAsAny[Optional[SchemaNode]] = None
    """更多操作相关配置"""

    draggable: Optional[bool] = None
    """是否支持拖拽排序"""

    dragOnSameLevel: Optional[bool] = None
    """仅允许同层级内拖拽"""

    saveOrderApi: Optional[API] = None
    """保存排序的 api"""

    itemBadge: Optional[ABadge] = None
    """角标"""

    links: Optional[list] = None
    """链接集合"""

    overflow: SerializeAsAny[Optional[Overflow]] = None
    """响应式收纳配置"""

    searchable: Optional[bool] = None
    """
    - 是否开启搜索
    - 默认值：false
    - 版本：3.5.0
    """

    searchConfig: SerializeAsAny[Optional[SearchConfig]] = None
    """
    - 搜索配置
    - 版本：3.5.0
    """