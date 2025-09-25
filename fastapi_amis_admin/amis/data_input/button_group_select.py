from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AButtonGroupSelect(AFormItem):
    """
    Button-Group-Select 按钮点选

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/button-group-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "button-group-select"

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

    btnLevel: Optional[Literal['link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 按钮样式
    - 默认值："default"
    """

    btnActiveLevel: Optional[Literal['link', 'primary', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 选中按钮样式
    - 默认值："default"
    """

    options: Optional[OptionsNode] = None
    """选项组"""


    source: Optional[Union[str, Any]] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """
    - 多选
    - 默认值：false
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值："value"
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

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""