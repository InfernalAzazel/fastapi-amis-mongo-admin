from typing import Optional
from pydantic import SerializeAsAny
from fastapi_amis_admin.amis.types import *


class AAnchorNav(AmisNode):
    """
    AnchorNav 锚点导航

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/anchor-nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Link(AmisNode):
        label: Optional[str] = None

        title: Optional[str] = None
        """区域 标题"""

        href: Optional[str] = None
        """区域 标识"""

        body: SerializeAsAny[Optional[SchemaNode]] = None
        """
        - 区域 内容区
        - 版本：6.1.0及以上版本垂直方向支持配置子节点
        """

        className: Optional[str] = None
        """区域成员 样式"""

    type: str = "anchor-nav"
    """指定为 AnchorNav 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    linkClassName: Optional[str] = None
    """导航 Dom 的类名"""

    sectionClassName: Optional[str] = None
    """锚点区域 Dom 的类名"""

    direction: Optional[Literal['vertical', 'horizontal']] = None
    """
    - 可以配置导航水平展示还是垂直展示
    - 默认值：'vertical'
    """

    active: Optional[str] = None
    """需要定位的区域"""

    links: Optional[list[Link]] = None
    """links 内容"""