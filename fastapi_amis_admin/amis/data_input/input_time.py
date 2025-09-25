from typing import Optional, Dict
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputTime(AFormItem):
    """
    InputTime 时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-time#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-time"

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 时间选择器值格式
    - 默认值：X
    - 3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 时间选择器显示格式
    - 默认值：HH:mm
    - 3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择时间"
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    timeConstraints: Optional[Dict[str, bool]] = None
    """
    - 时间约束
    - 默认值：true
    """

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""