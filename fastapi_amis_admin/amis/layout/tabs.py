from fastapi_amis_admin.amis.constants import *
from fastapi_amis_admin.amis.data_display.icon import AIcon
from fastapi_amis_admin.amis.types import *


#  https://baidu.github.io/amis/zh-CN/components/tabs#%E5%B1%9E%E6%80%A7%E8%A1%A8
class ATabs(AmisNode):
    """
    Tabs 选项卡

    选项卡容器组件
    """

    class Item(AmisNode):
        title: Optional[Union[str, SchemaNode]] = None
        """Tab 标题，当是 SchemaNode 时，该 title 不支持 editable 为 true 的双击编辑"""

        icon: Union[str, "AIcon", None] = None
        """Tab 的图标"""

        iconPosition: Literal['left', 'right'] = 'left'
        """Tab 的图标位置"""

        tab: SerializeAsAny[Optional[SchemaNode]] = None
        """内容区"""

        hash: Optional[str] = None
        """设置以后将跟 url 的 hash 对应"""

        reload: Optional[bool] = None
        """设置以后内容每次都会重新渲染，对于 crud 的重新拉取很有用"""

        unmountOnExit: Optional[bool] = None
        """每次退出都会销毁当前 tab 栏内容"""

        className: Optional[str] = "bg-white b-l b-r b-b wrapper-md"
        """Tab 区域样式"""

        tip: Optional[str] = None
        """3.2.0及以上版本支持 Tab 提示，当开启 showTip 时生效，作为 Tab 在 hover 时的提示显示，可不配置，如不设置，tabs[x].title 作为提示显示"""

        closable: bool = False
        """是否支持删除，优先级高于组件的 closable"""

        disabled: bool = False
        """是否禁用"""

    type: str = "tabs"
    """指定为 Tabs 渲染器"""

    defaultKey: Optional[Union[str, int]] = None
    """组件初始化时激活的选项卡，hash 值或索引值，支持使用表达式 2.7.1 以上版本"""

    activeKey: Optional[Union[str, int]] = None
    """激活的选项卡，hash 值或索引值，支持使用表达式，可响应上下文数据变化"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    linksClassName: Optional[str] = None
    """Tabs 标题区的类名"""

    contentClassName: Optional[str] = None
    """Tabs 内容区的类名"""

    tabsMode: Optional[TabsModeEnum] = None
    """展示模式，取值可以是 line、card、radio、vertical、chrome、simple、strong、tiled、sidebar"""

    tabs: SerializeAsAny[Optional[List[Item]]] = None
    """tabs 内容"""

    source: Optional[str] = None
    """tabs 关联数据，关联后可以重复生成选项卡"""

    toolbar: SerializeAsAny[Optional[SchemaNode]] = None
    """tabs 中的工具栏"""

    toolbarClassName: Optional[str] = None
    """tabs 中工具栏的类名"""

    mountOnEnter: bool = True
    """只有在点中 tab 的时候才渲染"""

    unmountOnExit: bool = False
    """切换 tab 的时候销毁"""

    addable: bool = False
    """是否支持新增"""

    addBtnText: str = '增加'
    """新增按钮文案"""

    closable: bool = False
    """是否支持删除"""

    draggable: bool = False
    """是否支持拖拽"""

    showTip: bool = False
    """是否支持提示"""

    showTipClassName: str = ''
    """提示的类"""

    editable: bool = False
    """是否可编辑标签名。当 tabs[x].title 为 SchemaNode 时，双击编辑 Tab 的 title 显示空的内容"""

    scrollable: bool = True
    """是否导航支持内容溢出滚动。（属性废弃）"""

    sidePosition: Literal['left', 'right'] = 'left'
    """sidebar 模式下，标签栏位置"""

    collapseOnExceed: Optional[int] = None
    """当 tabs 超出多少个时开始折叠"""

    collapseBtnLabel: str = 'more'
    """用来设置折叠按钮的文字"""

    swipeable: bool = False
    """是否开启手势滑动切换（移动端生效）"""
