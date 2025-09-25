from fastapi_amis_admin.amis.types import *


class AHtml(AmisNode):
    """
    HTML 渲染

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/html
    """

    type: str = "html"
    """指定为 HTML 组件"""

    html: str
    """html 当你需要在 data 字段中获取变量时，请使用 Tpl"""