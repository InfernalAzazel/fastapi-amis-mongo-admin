from fastapi_amis_admin.amis.types import *


class AGrid2D(AmisNode):
    """
    Grid 2D 布局

    Grid 2D 是一种二维布局方式，它可以更直观设置组件位置。

    参考：https://baidu.github.io/amis/zh-CN/components/grid-2d
    """
    class Grids(AmisNode):
        x: Optional[int] = None
        """格子起始位置的横坐标"""

        y: Optional[int] = None
        """格子起始位置的纵坐标"""

        w: Optional[int] = None
        """格子横跨几个宽度"""

        h: Optional[int] = None
        """格子横跨几个高度"""

        width: Optional[Union[str, int]] = None
        """格子所在列的宽度，可以设置 auto"""

        height: Optional[Union[str, int]] = None
        """格子所在行的高度，可以设置 auto"""

        align: str = 'auto'
        """格子内容水平布局，选填: left/center/right/auto"""

        valign: str = 'auto'

        """格子内容垂直布局，可选填: top/bottom/middle/auto"""

    type: str = "grid-2d"

    """指定为 Grid 2D 渲染器"""

    gridClassName: Optional[str] = None
    """外层 Dom 的类名"""

    gap: Optional[Union[int, str]] = 0
    """格子间距，包括水平和垂直"""

    cols: int = 12
    """格子水平划分为几个区域"""

    rowHeight: int = 50
    """每个格子默认垂直高度"""

    rowGap: Optional[Union[int, str]] = None
    """格子垂直间距"""

    grids: SerializeAsAny[Optional[List[SchemaNode]]] = None
