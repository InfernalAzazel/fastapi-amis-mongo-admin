from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AListSelect(AFormItem):
    """
    ListSelect 选择器

    ListSelect 一般用来实现选择，可以单选也可以多选，和 Radio/Checkboxs 最大的不同是在展现方面支持带图片。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/list-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "list-select"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[API] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值："value"
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    autoFill: Optional[dict] = None
    """自动填充"""

    listClassName: Optional[str] = None
    """支持配置 list div 的 CSS 类名"""


