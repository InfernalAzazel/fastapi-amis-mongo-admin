from fastapi_amis_admin.amis.constants import *
from fastapi_amis_admin.amis.types import *

class AAction(AmisNode):
    """
    Action 行为按钮

    Action 行为按钮，是触发页面行为的主要方法之一

    参考： https://baidu.github.io/amis/zh-CN/components/action?page=1#%E9%80%9A%E7%94%A8%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "action"
    """指定为 Page 渲染器"""

    actionType: Optional[str] = None
    """【必填】这是 action 最核心的配置，来指定该 action 的作用类型，支持：ajax、link、url、drawer、dialog、confirm、cancel、prev、next、copy、close"""

    label: Optional[str] = None
    """按钮文本,可用 ${xxx} 取值"""

    level: Optional[LevelEnum] = LevelEnum.default.value
    """按钮样式，支持：link、primary、secondary、info、success、warning、danger、light、dark、default"""

    size: Optional[str] = None
    """按钮大小，支持：xs、sm、md、lg"""

    icon: Optional[str] = None
    """设置图标，例如fa fa-plus"""

    iconClassName: Optional[str] = None
    """给图标上添加类名"""

    rightIcon: Optional[str] = None
    """在按钮文本右侧设置图标，例如fa fa-plus"""

    rightIconClassName: Optional[str] = None
    """给右侧图标上添加类名"""

    active: Optional[bool] = None
    """按钮是否高亮"""

    activeLevel: Optional[str] = None
    """按钮高亮时的样式，配置支持同level"""

    activeClassName: str = 'is-active'
    """给按钮高亮添加类名"""

    block: Optional[bool] = None
    """用 display:"block" 来显示按钮"""

    confirmText: Optional[Template] = None
    """当设置后，操作在开始前会询问用户。可用 ${xxx} 取值"""

    confirmTitle: Optional[Template] = None
    """确认框标题，前提是 confirmText 有内容，支持模版语法"""

    reload: Optional[str] = None

    """指定此次操作完后，需要刷新的目标组件名字（组件的name值，自己配置的），多个请用 , 号隔开"""
    tooltip: Optional[str] = None

    """鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值"""
    disabledTip: Optional[str] = None

    """被禁用后鼠标停留时弹出该段文字，也可以配置对象类型：字段为title和content。可用 ${xxx} 取值"""
    tooltipPlacement: str = 'top'

    """如果配置了tooltip或者disabledTip，指定提示信息位置，可配置top、bottom、left、right"""
    close: Optional[Union[bool, str]] = None

    """当action配置在dialog或drawer的actions中时，配置为true指定此次操作完后关闭当前dialog或drawer。当值为字符串，并且是祖先层弹框的名字的时候，会把祖先弹框关闭掉"""
    required: Optional[List[str]] = None
    """配置字符串数组，指定在form中进行操作之前，需要指定的字段名的表单项通过验证"""

    args: Union[dict, str, None] = None
    """事件参数"""
