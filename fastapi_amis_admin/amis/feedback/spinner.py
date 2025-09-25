from fastapi_amis_admin.amis.types import *


class Spinner(AmisNode):
    """
    Spinner 加载中

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/spinner#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "spinner"

    show: Optional[bool] = None
    """
    - 是否显示 spinner 组件
    - 默认值：true
    """

    showOn: Optional[Expression] = None
    """是否显示 spinner 组件的条件"""

    className: Optional[str] = None
    """spinner 图标父级标签的自定义 class"""

    spinnerClassName: Optional[str] = None
    """组件中 icon 所在标签的自定义 class"""

    spinnerWrapClassName: Optional[str] = None
    """作为容器使用时组件最外层标签的自定义 class"""

    size: Optional[Literal['sm', 'lg']] = None
    """组件大小"""

    icon: Optional[str] = None
    """组件图标，可以是内置图标，也可以是字体图标或者网络图片链接"""

    tip: Optional[str] = None
    """配置组件文案，例如加载中..."""

    tipPlacement: Optional[str] = None
    """
    - 配置组件 tip 相对于 icon 的位置
    - 默认值：bottom
    """

    delay: Optional[int] = None
    """
    - 配置组件显示延迟的时间（毫秒）
    - 默认值：0
    """

    overlay: Optional[bool] = None
    """
    - 配置组件显示 spinner 时是否显示遮罩层
    - 默认值：true
    """

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """作为容器使用时，被包裹的内容"""

    loadingConfig: Optional[Dict[str, Any]] = None
    """
    - 为 Spinner 指定挂载的容器
    - 开启后，会强制开启属性 overlay=true，并且 icon 会失效
    """