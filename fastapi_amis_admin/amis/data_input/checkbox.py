from typing import Optional, Literal, Union
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class ACheckbox(AFormItem):
    """
    Checkbox 勾选框

    用于实现勾选，功能和 Switch 类似，只是展现上不同。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/checkbox#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "checkbox"
    """指定为 checkbox 组件"""

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

    optionType: Optional[Literal['default', 'button']] = None
    """
    - 设置 option 类型
    - 默认值：'default'
    """