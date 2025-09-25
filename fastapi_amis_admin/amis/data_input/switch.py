from typing import Optional, Union, Literal
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class ASwitch(AFormItem):
    """
    Switch 开关

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/switch#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "switch"

    option: Optional[str] = None
    """选项说明"""

    onText: Optional[Union[str, dict, list]] = None
    """开启时开关显示的内容"""

    offText: Optional[Union[str, dict, list]] = None
    """关闭时开关显示的内容"""

    trueValue: Optional[Union[bool, str, int]] = None
    """
    - 标识真值
    - 默认值：true
    """

    falseValue: Optional[Union[bool, str, int]] = None
    """
    - 标识假值
    - 默认值：false
    """

    size: Optional[Literal['sm', 'md']] = None
    """
    - 开关大小
    - 默认值：'md'
    """

    loading: Optional[bool] = None
    """
    - 是否处于加载状态
    - 默认值：false
    """