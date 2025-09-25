from typing import Optional
from fastapi_amis_admin.amis.types import *


class ABadge(AmisNode):
    """
    Badge 角标

    部分组件可以设置 badge 属性来显示角标。

    - 1.2.2 及之前版本只支持头像组件

    - 1.2.3 开始支持按钮、链接、模板组件。

    参考： https://baidu.github.io/amis/zh-CN/components/badge#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    mode: str = "dot"
    """角标类型，可以是 dot/text/ribbon"""

    text: Optional[Union[int, str]]= None
    """角标文案，支持字符串和数字，在 mode='dot'下设置无效"""

    size: Optional[int] = None
    """角标大小"""

    level: Optional[str] = None
    """角标级别, 可以是 info/success/warning/danger, 设置之后角标背景颜色不同"""

    overflowCount: Optional[int] = None
    """
    - 设置封顶的数字值
    - 默认值：99
    """

    position: Optional[Literal['top-right','top-left', 'bottom-right', 'bottom-left']] = None
    """
    - 角标位置
    - 默认值：'top-right'
    """

    offset: Optional[list[int]] = None
    """
    - 角标位置，offset 相对于 position 位置进行水平、垂直偏移
    - 默认值：[0, 0]
    """

    className: Optional[str] = None
    """外层 dom 的类名"""

    animation: Optional[bool] = None
    """角标是否显示动画"""

    style: Optional[dict] = None
    """角标的自定义样式"""

    visibleOn: Optional[Expression] = None
    """控制角标的显示隐藏"""