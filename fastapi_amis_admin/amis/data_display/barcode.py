from fastapi_amis_admin.amis.types import *


class ABarCode(AmisNode):

    type: str = "property"

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，用作变量映射"""