from typing import Optional, Union
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class ARadio(AFormItem):
    """
    Radio 单选框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/radio#%E5%B1%9E%E6%80%A7%E8%A1%A8

    """

    type: str = "radio"

    option: Optional[str] = None
    """选项说明"""

    trueValue: Optional[Union[str, int, bool]] = None
    """
    - 标识真值
    - 默认值：true
    """

    falseValue: Optional[Union[str, int, bool]] = None
    """
    - 标识假值
    - 默认值：false
    """
