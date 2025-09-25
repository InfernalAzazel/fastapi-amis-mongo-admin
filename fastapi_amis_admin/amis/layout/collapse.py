from fastapi_amis_admin.amis.types import *


class ACollapse(AmisNode):
    """
    Collapse 折叠器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/collapse#collapse-%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'collapse'
    """指定为 collapse 渲染器	"""

    disabled: bool = False
    """禁用"""

    collapsed: bool = True
    """初始状态是否折叠"""

    key: Optional[Union[str, int]] = None
    """标识"""

    header: Optional[Union[str, SchemaNode]] = None
    """标题"""

    body: Optional[Union[str, SchemaNode]] = None
    """内容"""

    showArrow: bool = True
    """是否展示图标"""


class CollapseGroup(AmisNode):
    """
    CollapseGroup 折叠器群组件
    """

    type: str = "collapse-group"

    """指定为 collapse-group 渲染器"""

    activeKey: Union[str, int, List[Union[int, str, None]], None] = None
    """初始化激活面板的 key"""

    accordion: Optional[bool] = None
    """手风琴模式"""

    expandIcon: SerializeAsAny[Optional[SchemaNode]] = None
    """自定义切换图标"""

    expandIconPosition: Literal["left", "right"] = "left"
    """设置图标位置，可选值left | right"""

    body: SerializeAsAny[Optional[List[Union[ACollapse, SchemaNode]]]] = None

