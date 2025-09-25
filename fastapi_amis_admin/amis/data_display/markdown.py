from fastapi_amis_admin.amis.types import *


class AMarkdown(AmisNode):
    """
    Markdown 渲染

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/markdown#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "markdown"

    name: Optional[str] = None
    """名称"""

    value: Optional[str] = None
    """静态值"""

    className: Optional[str] = None
    """类名"""

    src: Optional[API] = None
    """外部地址"""

    options: Optional[dict] = None
    """
    - 有以下配置
     - html，是否支持 html 标签，默认 false
     - linkify，是否自动识别链接，默认值是 true
     - breaks，是否回车就是换行，默认 false
    """


