from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AEditor(AFormItem):
    """
    Editor 编辑器

    用于实现代码编辑，如果要实现富文本编辑请使用 Rich-Text。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/editor
    """

    type: str = "editor"
    """指定 editor 渲染器"""

    language: Optional[str] = None
    """编辑器高亮的语言，支持通过 ${xxx} 变量获取"""

    size: Optional[str] = None
    """编辑器高度，取值可以是 md、lg、xl、xxl"""

    allowFullscreen: Optional[bool] = None
    """是否显示全屏模式开关"""

    options: Optional[dict] = None
    """monaco 编辑器的其它配置，比如是否显示行号等，请参考这里，不过无法设置 readOnly，只读模式需要使用 disabled: true"""

    placeholder: Optional[str] = None
    """占位描述，没有值的时候展示"""