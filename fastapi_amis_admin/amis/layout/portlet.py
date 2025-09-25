from fastapi_amis_admin.amis.data_display.icon import AIcon
from fastapi_amis_admin.amis.types import *


# https://aisuda.bce.baidu.com/amis/zh-CN/components/portlet#%E5%B1%9E%E6%80%A7%E8%A1%A8
class APortlet(AmisNode):
    """
    Portlet 门户栏目

    门户栏目组件
    """

    class Item(AmisNode):
        title: Optional[str] = None
        """	Tab 标题"""

        icon: Union[str, "AIcon", None] = None
        """Tab 的图标"""

        tab: SerializeAsAny[Optional[SchemaNode]] = None
        """内容区"""

        toolbar: SerializeAsAny[Optional[SchemaNode]] = None
        """tabs 中的工具栏，随 tab 切换而变化"""

        reload: Optional[bool] = None
        """设置以后内容每次都会重新渲染，对于 crud 的重新拉取很有用"""

        unmountOnExit: Optional[bool] = None
        """每次退出都会销毁当前 tab 栏内容"""

        className: str = "bg-white b-l b-r b-b wrapper-md"
        """Tab 区域样式"""

    type: str = "portlet"

    className: Optional[str] = None
    """	外层 Dom 的类名"""

    tabsClassName: Optional[str] = None
    """Tabs Dom 的类名"""

    contentClassName: Optional[str] = None
    """Tabs content Dom 的类名"""

    tabs: SerializeAsAny[Optional[List[Item]]] = None
    """tabs 内容"""

    source: Optional[Any] = None
    """tabs 关联数据，关联后可以重复生成选项卡"""

    style: Union[str, dict, None] = None
    """自定义样式"""

    description: Optional[Template] = None
    """标题右侧信息"""

    hideHeader: Optional[bool] = None
    """隐藏头部"""

    divider: bool = False
    """去掉分隔线"""

    mountOnEnter: bool = False
    """只有在点中 tab 的时候才渲染"""

    unmountOnExit: bool = False
    """切换 tab 的时候销毁"""

    scrollable: bool = False
    """是否导航支持内容溢出滚动，vertical和chrome模式下不支持该属性；chrome模式默认压缩标签"""
