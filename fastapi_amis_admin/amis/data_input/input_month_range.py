from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputMonthRange(AFormItem):
    """
    InputMonthRange 月份范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-month-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-month-range"
    """指明为 input-month-range 组件"""

    format: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    inputFormat: Optional[str] = None
    """
    - 日期选择器显示格式
    - 默认值：'YYYY-DD'
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期范围'
    """

    minDate: Optional[str] = None
    """限制最小日期时间"""

    maxDate: Optional[str] = None
    """限制最大日期时间"""

    minDuration: Optional[str] = None
    """限制最小跨度，如： 2days"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：1year"""

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

    embed: Optional[bool] = None
    """
    - 是否内联
    - 默认值：false
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

