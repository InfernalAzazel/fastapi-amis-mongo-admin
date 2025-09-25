from typing import Union, Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputDatetimeRange(AFormItem):
    """
    InputDatetimeRange 日期时间范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-datetime-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-datetime-range"
    """指明为 input-datetime-range 组件"""

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期时间选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期范围'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期时间快捷键
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    utc: Optional[bool] = None
    """
    - 保存 utc 值
    - 默认值：false
    """

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：true
    """

    animation: Optional[bool] = None
    """
    - 是否启用游标动画
    - 默认值：false
    - 版本：2.2.0
    """

    extraName: Optional[str] = None
    """
    - 是否存成两个字段
    - 版本：3.3.0
    """

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """