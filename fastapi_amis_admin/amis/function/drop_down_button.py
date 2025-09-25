from fastapi_amis_admin.amis.function.button import AButton
from fastapi_amis_admin.amis.types import *


class DropDownButton(AmisNode):
    """
    DropDownButton 下拉菜单

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/dropdown-button#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "dropdown-button"
    """指定为 dropdown-button 渲染器"""

    label: Optional[str] = None
    """按钮文本"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    btnClassName: Optional[str] = None
    """按钮 CSS 类名"""

    menuClassName: Optional[str] = None
    """下拉菜单 CSS 类名"""

    block: Optional[bool] = None
    """块状样式"""

    size: Optional[Literal["xs", "sm", "md", "lg"]] = None
    """尺寸"""

    align: Optional[Literal["left", "right"]] = None
    """位置"""

    buttons: SerializeAsAny[List[AButton]] = None
    """配置下拉按钮"""

    iconOnly: Optional[bool] = None
    """只显示 icon"""

    defaultIsOpened: Optional[bool] = None
    """默认是否打开"""

    closeOnOutside: Optional[bool] = None
    """
    - 点击外侧区域是否收起
    - 默认值：true
    """

    closeOnClick: Optional[bool] = None
    """
    - 点击按钮后自动关闭下拉菜单
    - 默认值：false
    """

    trigger:  Optional[Literal['click', 'hover']] = None
    """
    - 触发方式
    - 默认值：'click'
    """

    hideCaret: Optional[bool] = None
    """
    - 隐藏下拉图标
    - 默认值：false
    """