from fastapi_amis_admin.amis.types import *


class AColor(AmisNode):
    type: Literal["color", "static-color"] = "color"
    """如果在 Table、Card 和 List 中，为"color"；在 Form 中用作静态展示，为"static-color"""

    className: Optional[str] = None
    """外层 CSS 类名 """

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    defaultColor: Optional[str] = None
    """默认颜色值"""

    showValue: Optional[bool] = None
    """
    - 是否显示右边的颜色值
    - 默认值：true
    """

    popOverContainerSelector: Optional[bool] = None
    """弹层挂载位置选择器，会通过querySelector获取，版本 6.4.2"""
