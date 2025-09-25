from typing import Optional
from fastapi_amis_admin.amis.types import AmisNode


class ALink(AmisNode):
    """
    Link 链接

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/link#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'link'
    """如果在 Table、Card 和 List 中，为"link"；在 Form 中用作静态展示，为"static-link" """

    body: Optional[str] = None
    """标签内文本"""

    href: Optional[str] = None
    """链接地址"""

    blank: Optional[bool] = None
    """是否在新标签页打开"""

    htmlTarget: Optional[str] = None
    """a 标签的 target，优先于 blank 属性"""

    title: Optional[str] = None
    """a 标签的 title"""

    disabled: Optional[bool] = None
    """禁用超链接"""

    icon: Optional[str] = None
    """超链接图标，以加强显示"""

    rightIcon: Optional[str] = None
    """右侧图标"""
