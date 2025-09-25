from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class ADrawer(AmisNode):
    """
    Drawer 抽屉

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/drawer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "drawer"

    title: Optional[SchemaNode] = None
    """弹出层标题"""

    body: Optional[SchemaNode] = None
    """往 Drawer 内容区加内容"""

    size: Optional[Literal['xs', 'sm','md','lg','xl']] = None
    """指定 Drawer 大小"""

    position: Optional[Literal['left', 'right', 'top', 'bottom']] = None
    """
    - 指定 Drawer 方向
    - 默认值：'right'
    """

    className: Optional[str] = None
    """Drawer 最外层容器的样式类名"""

    headerClassName: Optional[str] = None
    """Drawer 头部 区域的样式类名"""

    bodyClassName: Optional[str] = None
    """
    - Drawer body 区域的样式类名
    - 默认值：'modal-body'
    """

    footerClassName: Optional[str] = None
    """Drawer 页脚 区域的样式类名"""

    showCloseButton: Optional[bool] = None
    """
    - 是否展示关闭按钮，当值为 false 时，默认开启 closeOnOutside
    - 默认值：true
    """

    closeOnEsc: Optional[bool] = None
    """
    - 是否支持按 Esc 关闭 Drawer
    - 默认值：false
    """

    closeOnOutside: Optional[bool] = None
    """
    - 点击内容区外是否关闭 Drawer
    - 默认值：false
    """

    overlay: Optional[bool] = True
    """
    - 是否显示蒙层
    - 默认值：true
    """

    resizable: Optional[bool] = None
    """
    - 是否可通过拖拽改变 Drawer 大小
    - 默认值：false
    """

    width: Optional[Union[str, int]] = None
    """
    - 容器的宽度，在 position 为 left 或 right 时生效
    - 默认值：'500px'
    """

    height: Optional[Union[str, int]] = None
    """
    - 容器的高度，在 position 为 top 或 bottom 时生效
    - 默认值：'500px'
    """

    actions: SerializeAsAny[Optional[List[AAction]]] = None
    """可以不设置，默认只有两个按钮。"""

    data: Optional[Dict] = None
    """支持数据映射，如果不设定将默认将触发按钮的上下文中继承数据。"""