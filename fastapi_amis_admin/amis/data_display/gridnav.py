from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.other import ABadge
from fastapi_amis_admin.amis.types import *


class AGridNav(AmisNode):
    """
    GridNav 宫格导航

    宫格菜单导航，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service、Form或CRUD这样的，
    具有配置接口初始化数据域功能的组件，或者手动进行数据域初始化，
    然后通过source属性，获取数据链中的数据，完成菜单展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/grid-nav#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Option(AmisNode):
        icon: Optional[str] = None
        """列表项图标"""

        text: Optional[str] = None
        """列表项文案"""

        badge: Optional[ABadge] = None
        """列表项角标，详见 Badge"""

        link: Optional[str] = None
        """内部页面路径或外部跳转 URL 地址，优先级高于 clickAction"""

        blank: Optional[bool] = None
        """是否新页面打开，link 为 url 时有效"""

        clickAction: SerializeAsAny[Optional[AAction]] = None
        """列表项点击交互 详见 Action"""

    type: str = "grid-nav"

    className: Optional[str] = None
    """外层 CSS 类名"""

    itemClassName: Optional[str] = None
    """列表项 css 类名"""

    contentClassName: Optional[str] = None
    """列表项内容 css 类名"""

    value: Optional[List] = None
    """图片数组"""

    source: Optional[str] = None
    """数据源"""

    square: Optional[bool] = None
    """是否将列表项固定为正方形"""

    center: Optional[bool] = None
    """
    - 是否将列表项内容居中显示
    - 默认值：true
    """

    border: Optional[bool] = None
    """
    - 是否显示列表项边框
    - 默认值：true
    """

    gutter: Optional[int] = None
    """列表项之间的间距，默认单位为px"""

    reverse: Optional[bool] = None
    """是否调换图标和文本的位置"""

    iconRatio: Optional[int] = None
    """
    - 图标宽度占比，单位%
    - 默认值：60
    """

    direction: Optional[Literal["horizontal", "vertical"]] = None
    """
    - 列表项内容排列的方向
    - 默认值：'vertical'
    """

    columnNum: Optional[int] = None
    """
    - 列数
    - 默认值：4
    """

    options: SerializeAsAny[Optional[List[Option]]] = None
    """选项"""