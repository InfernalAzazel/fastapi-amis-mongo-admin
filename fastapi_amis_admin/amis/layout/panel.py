from fastapi_amis_admin.amis.function.action import *
from fastapi_amis_admin.amis.types import *


class APanel(AmisNode):
    """
    Panel 面板

    可以把相关信息以面板的形式展示到一块。
    """

    type: str = "panel"
    """指定为 Panel 渲染器"""
    className: str = "panel-default"
    """外层 Dom 的类名"""

    headerClassName: str = "panel-heading"
    """header 区域的类名"""

    footerClassName: str = "panel-footer bg-light lter wrapper"
    """footer 区域的类名"""

    actionsClassName: str = "panel-footer"
    """actions 区域的类名"""

    bodyClassName: str = "panel-body"
    """body 区域的类名"""

    title: SerializeAsAny[Optional[SchemaNode]] = None
    """标题"""

    header: SerializeAsAny[Optional[SchemaNode]] = None
    """头部容器"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """内容容器"""

    footer: SerializeAsAny[Optional[SchemaNode]] = None
    """底部容器"""

    affixFooter: Optional[bool] = None
    """是否固定底部容器"""

    actions: SerializeAsAny[Optional[List["AAction"]]] = None
    """按钮区域"""
