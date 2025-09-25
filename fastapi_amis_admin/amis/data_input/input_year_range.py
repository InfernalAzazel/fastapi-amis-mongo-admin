from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputYearRange(AFormItem):

    """
    InputYearRange 年份范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-year-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "input-year-range"

    valueFormat: Optional[str] = None
    """
    - 年份选择器值格式
    - 默认值：X
    - 版本：3.4.0
    """

    displayFormat: Optional[str] = None
    """
    - 年份选择器显示格式
    - 默认值：'YYYY'
    - 版本：3.4.0
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择年份范围'
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

    minDuration: Optional[str] = None
    """限制最小跨度，如：2year"""

    maxDuration: Optional[str] = None
    """限制最大跨度，如：4year"""

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
    - 版本：2.2.0
    """

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器 - 版本：6.4.0"""

