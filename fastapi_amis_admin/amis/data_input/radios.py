from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class Radios(AFormItem):
    """
    Radios 单选框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/radios#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "radios"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, Any]] = None
    """动态选项组"""

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    columnsCount: Optional[int] = None
    """
    - 选项按几列显示
    - 默认值：1
    """

    inline: Optional[bool] = None
    """
    - 是否显示为一行
    - 默认值：true
    """

    selectFirst: Optional[bool] = None
    """
    - 是否默认选中第一个
    - 默认值：false
    """

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""