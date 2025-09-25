from fastapi_amis_admin.amis.constants import SizeEnum
from fastapi_amis_admin.amis.types import *


# https://aisuda.bce.baidu.com/amis/zh-CN/components/wrapper#%E5%B1%9E%E6%80%A7%E8%A1%A8

class AWrapper(AmisNode):
    """
    Wrapper 包裹容器

    简单的一个包裹容器组件，相当于用 div 包含起来，最大的用处是用来配合 css 进行布局。
    """
    type: str = "wrapper"
    """指定为 Wrapper 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    size: Union[str, SizeEnum, None] = None
    """支持: xs、sm、md 和 lg"""

    style: Union[str, dict, None] = None
    """自定义样式"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """内容容器"""
