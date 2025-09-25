from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class AButtonGroup(AmisNode):
    """
    ButtonGroup 按钮组

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/button-group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "button-group"
    """指定为 button-group 渲染器"""

    vertical: Optional[bool] = None
    """
    - 是否使用垂直模式
    - 默认值：false
    """

    tiled: Optional[bool] = None
    """
    - 是否使用平铺模式
    - 默认值：false
    """

    btnLevel: Optional[Literal[
        'link', 'primary','secondary', 'info', 'success', 'warning', 'danger','light', 'dark', 'default']] = None
    """
    - 按钮样式
    - 默认值：'default'
    """

    btnActiveLevel: Optional[Literal[
        'link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 选中按钮样式
    - 默认值：'default'
    """

    buttons: SerializeAsAny[List[AAction]]
    """按钮"""

    className: Optional[str] = None
    """外层 Dom 的类名"""



