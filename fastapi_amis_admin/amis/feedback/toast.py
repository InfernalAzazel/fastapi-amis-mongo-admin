from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class AToast(AAction):
    """
    Toast 轻提示

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/toast#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ToastItem(AmisNode):
        title: SerializeAsAny[Optional[SchemaNode]] = None
        """标题"""

        body: SerializeAsAny[Optional[SchemaNode]] = None
        """内容"""

        level: Optional[Literal['info','success','error','warning']] = None
        """
        - 展示图标
        - 默认值：'info'
        """

        position: Optional[Literal['top-right','top-center','top-left','bottom-center','bottom-left','bottom-right','center']] = None
        """
        - 提示显示位置
        - 默认值：'top-center'（移动端为 'center'）
        """

        closeButton: Optional[bool] = None
        """
        - 是否展示关闭按钮
        - 默认值：false
        """

        showIcon: Optional[bool] = None
        """
        - 是否展示图标
        - 默认值：true
        """

        timeout: Optional[int] = None
        """
        - 持续时间
        - 默认值：5000（error 类型为 6000，移动端为 3000）
        """

        allowHtml: Optional[bool] = None
        """
        - 是否会被当作 HTML 片段处理
        - 默认值：true
        """

    actionType: Optional[str] = None

    items: SerializeAsAny[Optional[List[ToastItem]]] = None
    """
    - 轻提示内容
    - 默认值：[]
    """

    position: Optional[Literal['top-right','top-center','top-left','bottom-center','bottom-left','bottom-right','center']] = None
    """
    - 提示显示位置
    - 默认值：'top-center'（移动端为 'center'）
    """

    closeButton: Optional[bool] = None
    """
    - 是否展示关闭按钮
    - 默认值：false
    - 移动端不展示
    """

    showIcon: Optional[bool] = None
    """
    - 是否展示图标
    - 默认值：true
    """

    timeout: Optional[int] = None
    """
    - 持续时间
    - 默认值：5000（error 类型为 6000，移动端为 3000）
    """