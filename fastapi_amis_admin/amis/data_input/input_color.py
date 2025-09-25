from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputColor(AFormItem):
    """
    InputColor 颜色选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-color#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class PresetColor(AmisNode):
        title: Optional[str] = None
        """标题"""

        color: Optional[str] = None
        """颜色"""

    type: str = "input-color"
    """指明为 input-color 组件"""

    format: Optional[Literal['hex', 'hls', 'rgb', 'rgba']] = None
    """
    - 格式化
    - 默认值：'hex'
    """

    presetColors: Optional[list[PresetColor]] = None
    """选择器底部的默认颜色，数组内为空则不显示默认颜色"""

    allowCustomColor: Optional[bool] = None
    """
    - 为false时只能选择颜色，使用 presetColors 设定颜色选择范围
    - 默认值：true
    """

    clearable: Optional[bool] = None
    """
    - 是否显示清除按钮
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """清除后，表单项值调整成该值"""