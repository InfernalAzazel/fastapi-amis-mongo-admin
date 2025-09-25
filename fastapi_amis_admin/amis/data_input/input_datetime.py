from typing import Optional, Union
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputDatetime(AFormItem):
    """
    InputDatetime 日期时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-datetime#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-datetime"
    """指明为 input-datetime 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 日期时间选择器值格式，更多格式类型请参考 文档
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期时间选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD HH:mm:ss'
    - 版本：3.4.0 版本后支持
    """

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期以及时间'
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

    embed: Optional[bool] = None
    """
    - 是否内联
    - 默认值：false
    """

    timeConstraints: Optional[dict] = None
    """
    - 请参考 input-time 里的说明
    - 默认值：true
    """

    isEndDate: Optional[dict] = None
    """
    - 如果配置为 true，会自动默认为 23:59:59 秒
    - 默认值：false
    """

    disabledDate: Optional[str] = None
    """用字符函数来控制哪些天不可以被点选"""

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持
    """
