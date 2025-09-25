from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputTimeRange(AFormItem):
    """
    InputTimeRange 时间范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-time-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-time-range"

    valueFormat: Optional[str] = None
    """
    - 时间范围选择器值格式
    - 默认值：HH:mm
    - 3.4.0
    """

    displayFormat: Optional[str] = None
    """
    - 时间范围选择器显示格式
    - 默认值：HH:mm
    - 3.4.0
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择时间范围"
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    embed: Optional[bool] = None
    """
    - 是否内联模式
    - 默认值：false
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：true
    - 2.2.0
    """

    extraName: Optional[str] = None
    """是否存成两个字段 - 3.3.0"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器 - 6.4.0"""
