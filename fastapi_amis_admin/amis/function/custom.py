from fastapi_amis_admin.amis.types import *


class ACustom(AmisNode):
    """
    Custom 自定义组件

    用于实现自定义组件，它解决了之前 JS SDK 和可视化编辑器中难以支持自定义组件的问题。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/custom#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "custom"
    """指定为 custom 渲染器"""

    id: Optional[str] = None
    """节点 id"""

    name: Optional[str] = None
    """节点 名称"""

    className: Optional[str] = None
    """节点 class"""

    inline: bool = False
    """
    - 默认使用 div 标签，如果 true 就使用 span 标签
    - 默认值：false
    """

    html: Optional[str] = None
    """初始化节点 html"""

    onMount: Optional[str] = None
    """
    - 节点初始化之后调的用函数
    - 默认值：Function
    """

    onUpdate: Optional[str] = None
    """
    - 数据有更新的时候调用的函数
    - 默认值：Function
    """

    onUnmount: Optional[str] = None
    """
    - 节点销毁的时候调用的函数
    - 默认值：Function
    """