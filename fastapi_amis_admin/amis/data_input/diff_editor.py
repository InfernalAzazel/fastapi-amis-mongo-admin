from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ADiffEditor(AFormItem):
    """
    DiffEditor 对比编辑器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/diff-editor#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "diff-editor"
    """指明为 diff-editor 组件"""

    language: Optional[str] = None
    """编辑器高亮的语言，可选 支持的语言"""

    diffValue: Optional[Template] = None
    """左侧值"""