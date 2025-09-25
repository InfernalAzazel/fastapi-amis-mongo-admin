from fastapi_amis_admin.amis.types import *


class ABreadcrumb(AmisNode):
    """
    Breadcrumb 面包屑

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/breadcrumb#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class BreadcrumbItem(AmisNode):
        label: Optional[str] = None
        """文本"""

        href: Optional[str] = None
        """链接"""

        icon: Optional[str] = None
        """图标"""

        dropdown: Optional[List] = None
        """下拉菜单，dropdown[]的每个对象都包含label、href、icon属性"""

    type: str = "breadcrumb"
    """指定为 breadcrumb 渲染器"""

    className: Optional[str] = None
    """外层类名"""

    itemClassName: Optional[str] = None
    """导航项类名"""

    separatorClassName: Optional[str] = None
    """分割符类名"""

    dropdownClassName: Optional[str] = None
    """下拉菜单类名"""

    dropdownItemClassName: Optional[str] = None
    """下拉菜单项类名"""

    separator: str = ">"
    """分隔符"""

    labelMaxLength: Optional[int] = None
    """
    - 最大展示长度
    - 默认值：16
    """

    tooltipPosition: Optional[Literal['top', 'bottom', 'left', 'right']] = None
    """
    - 浮窗提示位置
    - 默认值：'top'
    """

    source: Optional[API] = None
    "动态数据"

    items: SerializeAsAny[Optional[List[BreadcrumbItem]]] = None
    """项目"""