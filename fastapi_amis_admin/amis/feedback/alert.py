from fastapi_amis_admin.amis.types import *


class AAlert(AmisNode):
    """
    Alert 提示

    用来做文字特殊提示，分为四类：提示类、成功类、警告类和危险类。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/alert#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "alert"

    title: Optional[str] = None
    """alert 标题"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    level: Optional[Literal['info', 'success', 'warning', 'danger']] = None
    """
    - 级别
    - 默认值：'info'
    """

    body: SerializeAsAny[Optional[Union[List[SchemaNode], SchemaNode]]] = None
    """显示内容"""

    showCloseButton: Optional[bool] = None
    """
    - 是否显示关闭按钮
    - 默认值：false
    """

    closeButtonClassName: Optional[str] = None
    """关闭按钮的 CSS 类名"""

    showIcon: Optional[bool] = None
    """
    - 是否显示 icon
    - 默认值：false
    """

    icon: Optional[str] = None
    """自定义 icon"""

    iconClassName: Optional[str] = None
    """icon 的 CSS 类名"""

    actions: SerializeAsAny[Optional[Union[List[SchemaNode], SchemaNode]]] = None
    """
    - 操作区域
    - 版本：3.6.0
    """