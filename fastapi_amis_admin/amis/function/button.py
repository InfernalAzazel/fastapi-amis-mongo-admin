from fastapi_amis_admin.amis.types import *


class AButton(AmisNode):
    """
    Button 按钮

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/button#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "button"
    """指定为 button 渲染器"""

    className: Optional[str] = None
    """指定添加 button 类名"""

    url: Optional[str] = None
    """点击跳转的地址，指定此属性 button 的行为和 a 链接一致"""

    size: Optional[str] = None
    """设置按钮大小"""

    actionType: Optional[Literal['button', 'reset', 'submit', 'clear', 'url']] = None
    """
    - 设置按钮类型
    - 默认值：'button'
    """

    level: Optional[Literal['link', 'primary', 'enhance', 'secondary', 'info', 'success', 'warning', 'danger', 'light', 'dark', 'default']] = None
    """
    - 设置按钮样式
    - 默认值：'default'
    """

    tooltip: Optional[Union[str, dict]] = None
    """气泡提示内容"""

    tooltipPlacement: Optional[Literal['top', 'right', 'bottom', 'left' ]] = None
    """
    - 气泡框位置器
    - 默认值：'top'
    """

    tooltipTrigger: Optional[Literal['hover', 'focus']] = None
    """触发 tootip"""

    disabled: Optional[bool] = None
    """
    - 按钮失效状态
    - 默认值: false
    """

    disabledTip: Optional[Union[str, dict]] = None
    """按钮失效状态下的提示"""

    block: Optional[bool] = None
    """
    - 将按钮宽度调整为其父宽度的选项
    - 默认值：false
    """

    loading: Optional[bool] = None
    """
    - 显示按钮 loading 效果
    - 默认值：false
    """

    loadingOn: Optional[str] = None
    """显示按钮 loading 表达式"""
