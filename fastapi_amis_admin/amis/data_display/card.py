from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class ACard(AmisNode):
    """
    Card 卡片

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/card
    """

    class Header(AmisNode):
        className: Optional[str] = None
        """头部类名"""

        title: Optional[Optional[Template]] = None
        """标题"""

        titleClassName: Optional[str] = None
        """标题类名"""

        subTitle: Optional[Template] = None
        """	副标题"""

        subTitleClassName: Optional[str] = None
        """副标题类名"""

        subTitlePlaceholder: Optional[str] = None
        """	副标题占位"""

        description: Optional[Template] = None
        """描述"""

        descriptionClassName: Optional[str] = None
        """描述类名"""

        descriptionPlaceholder: Optional[str] = None
        """描述占位"""

        avatar: Optional[Template] = None
        """图片"""

        avatarClassName: Optional[str] = None
        """
        - 图片包括层类名
        - 默认值：'pull-left thumb avatar b-3x m-r'
        """

        imageClassName: Optional[str] = None
        """图片类名"""

        avatarText: Optional[Template] = None
        """如果不配置图片，则会在图片处显示该文本"""

        avatarTextBackground: Optional[str] = None
        """设置文本背景色，它会根据数据分配一个颜色"""

        avatarTextClassName: Optional[str] = None
        """图片文本类名"""

        highlight: Optional[bool] = None
        """
        - 是否显示激活样式
        - 默认值：false
        """

        highlightClassName: Optional[str] = None
        """激活样式类名"""

        href: Optional[Template] = None
        """点击卡片跳转的链接地址"""

        blank: Optional[bool] = None
        """
        - 是否新窗口打开
        - 默认值：false
        """

    class Media(AmisNode):
        type: Optional[Literal['image', 'video']] = 'image'
        """
        - 多媒体类型
        - 默认值：'image'
        """

        url: Optional[str] = None
        """图片/视频链接"""

        position: Optional[Literal['left', 'right', 'top', 'bottom']] = None
        """
        - 多媒体位置
        - 默认值：'left'
        """

        className: Optional[str] = None
        """
        - 多媒体类名
        - 默认值：'w-44 h-28'
        """

        isLive: Optional[bool] = None
        """
        - 视频是否为直播
        - 默认值：false
        """

        autoPlay: Optional[bool] = None
        """
        - 视频是否自动播放
        - 默认值：false
        """

        poster: Union[bool, str, None] = None
        """
        - 视频封面
        - 默认值：false
        """

    type: str = "card"
    """指定为 Card 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    href: Optional[Template] = None
    """外部链接"""

    header: SerializeAsAny[Optional[Header]] = None
    """Card 头部内容设置"""

    body: Optional[list] = None
    """内容容器，主要用来放置非表单项组件"""

    bodyClassName: Optional[str] = None
    """内容区域类名"""

    actions: SerializeAsAny[Optional[List[AAction]]] = None
    """配置按钮集合"""

    actionsCount: Optional[int] = None
    """
    - 按钮集合每行个数
    - 默认值：4
    """

    itemAction: SerializeAsAny[Optional[AAction]] = None
    """点击卡片的行为"""

    media: SerializeAsAny[Optional[Media]] = None
    """Card 多媒体部内容设置"""

    secondary: Optional[Template] = None
    """次要说明"""

    toolbar: SerializeAsAny[Optional[List[AAction]]] = None
    """工具栏按钮"""

    dragging: Optional[bool] = None
    """
    - 是否显示拖拽图标
    - 默认值：false
    """

    selectable: Optional[bool] = None
    """
    - 卡片是否可选
    - 默认值：false
    """

    checkable: Optional[bool] = None
    """
    - 卡片选择按钮是否禁用
    - 默认值：true
    """

    selected: Optional[bool] = None
    """
    - 卡片选择按钮是否选中
    - 默认值：false
    """

    hideCheckToggler: Optional[bool] = None
    """
    - 卡片选择按钮是否隐藏
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 卡片是否为多选
    - 默认值：false
    """

    useCardLabel: Optional[bool] = None
    """
    - 卡片内容区的表单项 label 是否使用 Card 内部的样式
    - 默认值：true
    """