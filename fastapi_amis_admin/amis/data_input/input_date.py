from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputDate(AFormItem):
    """
    InputDate 日期

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-date#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-date"
    """指明为 input-date 组件"""

    value: Optional[str] = None
    """默认值"""

    valueFormat: Optional[str] = None
    """
    - 日期选择器值格式，更多格式类型请参考 文档
    - 默认值：'X'
    - 版本：3.4.0 版本后支持
    """

    displayFormat: Optional[str] = None
    """
    - 日期选择器显示格式，即时间戳格式，更多格式类型请参考 文档
    - 默认值：'YYYY-MM-DD'
    - 版本：3.4.0 版本后支持
    """

    closeOnSelect: Optional[bool] = None
    """
    - 点选日期后，是否马上关闭选择框
    - 默认值：false
    """
    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'请选择日期'
    """

    shortcuts: Optional[Union[str, list[str], list[dict]]] = None
    """
    - 日期快捷键，字符串格式为预设值，对象格式支持写表达式
    - 版本：3.1.0 版本后支持表达式
    """

    minDate: Optional[str] = None
    """限制最小日期"""

    maxDate: Optional[str] = None
    """限制最大日期"""

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
    - 是否内联模式
    - 默认值：false
    """
    disabledDate: Optional[str] = None
    """用字符函数来控制哪些天不可以被点选"""

    popOverContainerSelector: Optional[str] = None
    """
    - 弹层挂载位置选择器，会通过querySelector获取
    - 版本：6.4.0 版本后支持表达式
    """

    name: Optional[str] = None
    """名称"""

    description: Optional[str] = None
    """描述"""

    format: Optional[str] = None
    """格式"""

    inputFormat: Optional[str] = None
    """输入格式"""