from fastapi_amis_admin.amis.types import *


class APopOver(AmisNode):
    """
    PopOver 弹出提示

    popover 不是一个独立组件，它是嵌入到其它组件中使用的，目前可以在以下组件中配置

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/popover?page=1#%E5%B1%9E%E6%80%A7%E5%88%97%E8%A1%A8
    """
    mode: Optional[Literal['popOver', 'dialog', 'drawer']] = None
    """
    - 模式
    - 默认值：'popOver'
    """

    size: Optional[int] = None
    """当配置成 dialog 或者 drawer 的时候有用"""

    position: Optional[str] = None
    """配置弹出位置，只有 popOver 模式有用，默认是自适应"""

    offset: Optional[dict] = None
    """
    - 偏移
    - 默认值： {top: 0, left: 0}
    """

    trigger: Optional[Literal['click', 'hover']] = None
    """
    - 触发弹出的条件
    - 默认值：'click'
    """

    showIcon: Optional[bool] = None
    """是否显示图标。默认会有个放大形状的图标出现在列里面。如果配置成 false，则触发事件出现在列上就会触发弹出。"""

    title: Optional[str] = None
    """弹出框的标题"""

    body: Optional[Union[str, dict]] = None
    """弹出框的内容"""