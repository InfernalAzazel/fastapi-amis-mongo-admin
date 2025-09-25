from fastapi_amis_admin.amis.data_display.icon import AIcon
from fastapi_amis_admin.amis.types import *


class ATag(AmisNode):
    type: str = "tag"

    displayMode: Optional[Literal['normal', 'rounded', 'status']] = None
    """
    - 展现模式
    - 默认值：'normal'
    """

    color: Optional[Literal['active', 'inactive', 'error', 'success', 'processing', 'warning', str]] = None
    """颜色主题，提供默认主题，并支持自定义颜色值"""

    label: Optional[str] = None
    """标签内容"""

    icon: SerializeAsAny[Optional[AIcon]] = None
    """status 模式下的前置图标"""

    className: Optional[str] = None
    """自定义 CSS 样式类名"""

    style: Optional[Dict[str, Any]] = None
    """自定义样式（行内样式），优先级最高"""

    closable: Optional[bool] = None
    """
    - 是否展示关闭按钮
    - 默认值：false
    """
