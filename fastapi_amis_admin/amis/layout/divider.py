from fastapi_amis_admin.amis.types import *

class ADivider(AmisNode):
    """
    Divider 分割线

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/divider#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "divider"
    """"divider" 指定为 分割线 渲染器"""

    className: Optional[str] = None
    """	外层 Dom 的类名"""

    lineStyle: Optional[str] = None
    """分割线的样式，支持dashed和solid"""

    direction: str = "horizontal"
    """分割线的方向，支持horizontal和vertical，版本:3.5.0"""

    color: Optional[str] = None
    """分割线的颜色，版本:3.5.0"""

    rotate: Optional[int] = None
    """分割线的旋转角度，版本:3.5.0"""

    title: Optional[SchemaNode] = None
    """分割线的标题，版本:3.5.0"""

    titleClassName: Optional[str] = None
    """分割线的标题类名，版本:3.5.0"""

    titlePosition: Optional[str] = 'center'
    """分割线的标题位置，支持left、center和right，版本:3.5.0"""
