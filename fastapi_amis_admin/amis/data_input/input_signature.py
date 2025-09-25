from fastapi_amis_admin.amis.types import *


class InputSignature(AmisNode):
    """
    InputSignature 签名面板

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-signature#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    width: Optional[int] = None
    """组件宽度，最小 300"""

    height: Optional[int] = None
    """组件高度，最小 160"""

    color: Optional[str] = None
    """
    - 手写字体颜色
    - 默认值：'#000'
    """

    bgColor: Optional[str] = None
    """
    - 面板背景颜色
    - 默认值：'#EFEFEF'
    """

    clearBtnLabel: Optional[str] = None
    """
    - 清空按钮名称
    - 默认值：'清空'
    """

    undoBtnLabel: Optional[str] = None
    """
    - 撤销按钮名称
    - 默认值：'撤销'
    """

    confirmBtnLabel: Optional[str] = None
    """
    - 确认按钮名称
    - 默认值：'确认'
    """

    embed: Optional[bool] = None
    """是否内嵌"""

    embedConfirmLabel: Optional[str] = None
    """
    - 内嵌容器确认按钮名称
    - 默认值：'确认'
    """

    ebmedCancelLabel: Optional[str] = None
    """
    - 内嵌容器取消按钮名称
    - 默认值：'取消'
    """

    embedBtnIcon: Optional[str] = None
    """内嵌按钮图标"""

    embedBtnLabel: Optional[str] = None
    """
    - 内嵌按钮文案
    - 默认值：'点击签名'
    """