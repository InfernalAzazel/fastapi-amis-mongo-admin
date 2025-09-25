from fastapi_amis_admin.amis.types import *


class ATooltipWrapper(AmisNode):
    """
    TooltipWrapper 文字提示容器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/tooltip#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "tooltip-wrapper"
    """指定为文字提示容器组件"""

    title: Optional[Optional[str]] = None
    """文字提示标题"""

    content: Optional[str] = None
    """文字提示内容, 兼容之前的 tooltip 属性"""

    placement: Optional[Literal['top', 'left', 'right', 'bottom']] = None
    """
    - 文字提示浮层出现位置
    - 默认值：'top'
    """

    tooltipTheme: Optional[Literal["light", "dark"]] = None
    """
    - 主题样式
    - 默认值：'light'
    """

    offset: Optional[list[int]] = None
    """
    - 文字提示浮层位置相对偏移量，单位 px
    - 默认值：[0, 0]
    """

    showArrow: Optional[bool] = None
    """
    - 是否展示浮层指向箭头
    - 默认值：true
    """

    enterable: Optional[bool] = None
    """
    - 是否鼠标可以移入到浮层中
    - 默认值：true
    """

    disabled: Optional[bool] = None
    """
    - 是否禁用浮层提示
    - 默认值：false
    """

    trigger: Union[Literal['hover','click', 'focus'], list[Literal['hover','click', 'focus']]] = None
    """
    - 浮层触发方式，支持数组写法["hover", "click"]
    - 默认值：'hover'
    """

    mouseEnterDelay: Optional[int] = None
    """
    - 浮层延迟展示时间，单位 ms
    - 默认值：0
    """

    mouseLeaveDelay: Optional[int] = None
    """
    - 浮层延迟隐藏时间，单位 ms
    - 默认值：300
    """

    rootClose: Optional[bool] = None
    """
    - 是否点击非内容区域关闭提示
    - 默认值：true
    """

    inline: Optional[bool] = None
    """
    - 内容区是否内联显示
    - 默认值：false
    """

    wrapperComponent: Optional[str] = None
    """
    - 容器标签名
    - 默认值：'div' | 'span'
    """

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """内容容器"""

    style: Optional[Union[str, dict]] = None
    """内容区自定义样式"""

    tooltipStyle:  Optional[Union[str, dict]] = None
    """浮层自定义样式"""

    className: Optional[str] = None
    """内容区类名"""

    tooltipClassName: Optional[str] = None
    """文字提示浮层类名"""













