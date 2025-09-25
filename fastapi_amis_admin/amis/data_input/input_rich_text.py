from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputRichText(AFormItem):
    """
    InputRichText 富文本编辑器

    目前富文本编辑器基于两个库：froala 和 tinymce，默认使用 tinymce。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-rich-text#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-rich-text"

    saveAsUbb: Optional[bool] = None
    """是否保存为 ubb 格式"""

    receiver: Optional[API] = None
    """默认的图片保存 API"""

    videoReceiver: Optional[API] = None
    """默认的视频保存 API，仅支持 froala 编辑器"""

    fileField: Optional[str] = None
    """上传文件时的字段名"""

    size: Optional[Literal['md', 'lg']] = None
    """框的大小"""

    options: Optional[Dict[str, Any]] = None
    """需要参考 tinymce 或 froala 的文档"""

    buttons: Optional[List[str]] = None
    """froala 专用，配置显示的按钮"""

    vendor: Optional[Literal['froala']] = None
    """只需要加一行 "vendor": "froala" 配置就行，froala 是付费产品，需要设置 richTextToken 才能去掉水印"""