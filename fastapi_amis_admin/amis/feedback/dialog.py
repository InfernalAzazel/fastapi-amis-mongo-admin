from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class Dialog(AmisNode):
    """
    Dialog 对话框

    Dialog 弹框 主要由 Action 触发，主要展示一个对话框以供用户操作。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/dialog#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "dialog"

    title: SerializeAsAny[Optional[SchemaNode]] = None
    """弹出层标题"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """往 Dialog 内容区加内容"""

    size: Optional[Literal['xs', 'sm', 'md', 'lg', 'xl', 'full']] = None
    """指定 dialog 大小，支持: xs、sm、md、lg、xl、full"""

    bodyClassName: Optional[str] = None
    """
    - Dialog body 区域的样式类名
    - 默认值：'modal-body'
    """

    closeOnEsc: Optional[bool] = None
    """
    - 是否支持按 Esc 关闭 Dialog
    - 默认值：false
    """

    showCloseButton: Optional[bool] = None
    """
    - 是否显示右上角的关闭按钮
    - 默认值：true
    """

    showErrorMsg: Optional[bool] = None
    """
    - 是否在弹框左下角显示报错信息
    - 默认值：true
    """

    showLoading: Optional[bool] = None
    """
    - 是否在弹框左下角显示 loading 动画
    - 默认值：true
    """

    disabled: Optional[bool] = None
    """
    - 如果设置此属性，则该 Dialog 只读没有提交操作。
    - 默认值：false
    """

    actions: SerializeAsAny[Optional[List[AAction]]] = None
    """如果想不显示底部按钮，可以配置：[]"""

    data: Optional[Dict] = None
    """支持数据映射，如果不设定将默认将触发按钮的上下文中继承数据。"""
