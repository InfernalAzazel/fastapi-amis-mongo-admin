from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class Group(AmisNode):
    """
    Group 表单项组

    表单项，默认都是一行显示一个，Group 组件用于在一行展示多个表单项，
    会自动根据表单项数量均分宽度。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "group"

    className: Optional[str] = None
    """CSS 类名"""

    label: Optional[str] = None
    """group 的标签"""

    body: Optional[List['AFormItem']] = None
    """表单项集合"""

    mode: Optional[str] = None
    """展示默认，同 Form 中的模式"""

    gap: Optional[Literal['xs', 'sm', 'normal']] = None
    """表单项之间的间距"""

    direction: Optional[Literal['vertical', 'horizontal']] = None
    """
    - 可以配置水平展示还是垂直展示
    - 默认值：'horizontal'
    """