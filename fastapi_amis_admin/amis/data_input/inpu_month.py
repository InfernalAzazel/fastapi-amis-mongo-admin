from typing import Optional

from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputMonthRange(AFormItem):
    """
    InputMonth 月份

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-month#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-month-range"
    """指明为 input-month-range 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 月份选择器值格式，更多格式类型请参考 moment
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 月份选择器显示格式，即时间戳格式，更多格式类型请参考 moment
    - 默认值：'YYYY-MM'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择月份'
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    popOverContainerSelector: Optional[bool] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0
    """