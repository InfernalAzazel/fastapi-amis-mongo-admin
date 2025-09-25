from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AFieldSet(AFormItem):
    type: str = 'fieldSet'
    """
    FieldSet 表单项集合
    
    FieldSet 是用于分组展示表单项的一种容器型组件，可以折叠。
    
    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/fieldset#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    className: Optional[str] = None
    """CSS 类名"""

    headingClassName: Optional[str] = None
    """标题 CSS 类名"""

    bodyClassName: Optional[str] = None
    """内容区域 CSS 类名"""

    title: SerializeAsAny[Optional[SchemaNode]] = None
    """标题"""

    body: SerializeAsAny[Optional[AFormItem]] = None
    """表单项集合"""

    mode: Optional[str] = None
    """展示默认，同 Form 中的模式"""

    collapsable: Optional[bool] = None
    """是否可折叠"""

    collapsed: Optional[bool] = None
    """默认是否折叠"""

    collapseTitle: SerializeAsAny[Optional[SchemaNode]] = None
    """收起的标题"""

    size: Optional[Literal['xs', 'sm','base', 'md', 'lg']] = None
    """大小"""