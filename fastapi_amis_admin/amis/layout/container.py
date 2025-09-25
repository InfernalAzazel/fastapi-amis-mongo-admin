from fastapi_amis_admin.amis.types import *


class AContainer(AmisNode):
    """
    Container 是一种容器组件，它可以渲染其他 amis 组件。

    - 注意 Container 组件因为历史原因多了一层 div，推荐使用 wrapper 来作为容器。

    参考：https://baidu.github.io/amis/zh-CN/components/container#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'container'
    """指定为 container 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    bodyClassName: Optional[str] = None
    """容器内容区的类名"""

    wrapperComponent: Optional[str] = 'div'
    """容器标签名"""

    style: Optional[str] = None
    """自定义样式"""

    body: Optional[SchemaNode] = None
    """容器内容"""
