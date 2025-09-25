from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class ATextarea(AFormItem):
    """
    Textarea 多行文本输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/textarea#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "textarea"

    minRows: Optional[int] = None
    """
    - 最小行数
    - 默认值：3
    """

    maxRows: Optional[int] = None
    """
    - 最大行数
    - 默认值：20
    """

    trimContents: Optional[bool] = None
    """
    - 是否去除首尾空白文本
    - 默认值：true
    """

    readOnly: Optional[bool] = None
    """
    - 是否只读
    - 默认值：false
    """

    showCounter: Optional[bool] = None
    """
    - 是否显示计数器
    - 默认值：false
    """

    maxLength: Optional[int] = None
    """限制最大字数"""

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """
    - 清除后设置此配置项给定的值
    - 默认值：""
    """