from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class InputQuarterRange(AFormItem):
    """
    InputQuarterRange 季度范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-quarter-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-quarter-range"

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式
    - 默认值：'X'
    """

    displayFormat: Optional[str] = None
    """
    - 日期选择器显示格式
    - 默认值：'YYYY-DD'
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值："请选择季度范围"
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

    minDuration: Optional[str] = None
    """限制最小跨度，如：2quarter"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：4quarter"""

    utc: Optional[bool] = None
    """
    - 保存 UTC 值
    - 默认值：false
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
    """

    extraName: Optional[str] = None
    """是否存成两个字段"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""