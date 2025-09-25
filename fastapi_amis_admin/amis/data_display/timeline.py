from fastapi_amis_admin.amis.types import *


class ATimeline(AmisNode):
    """
    Timeline 时间轴

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/timeline#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class TimelineItem(AmisNode):
        time: Optional[str] = None
        """节点时间"""

        title: SerializeAsAny[Optional[Union[str, 'SchemaNode']]] = None
        """节点标题"""

        detail: Optional[str] = None
        """节点详细描述（折叠）"""

        detailCollapsedText: Optional[str] = "展开"
        """详细内容折叠时按钮文案"""

        detailExpandedText: Optional[str] = "折叠"
        """详细内容展开时按钮文案"""

        color: Optional[Union[str, Literal['info', 'success', 'warning', 'danger']]] = None
        """
        - 时间轴节点颜色
        - 默认值：'#DADBDD'
        """

        icon: Optional[str] = None
        """icon 名，支持 fontawesome v4 或使用 url（优先级高于 color）"""

        iconClassName: Optional[str] = None
        """
        节点图标的 CSS 类名
        - 优先级高于统一配置的 iconClassName
        - 3.4.0 版本支持
        """

        timeClassName: Optional[str] = None
        """
        节点时间的 CSS 类名
        - 优先级高于统一配置的 timeClassName
        - 3.4.0 版本支持
        """

        titleClassName: Optional[str] = None
        """
        节点标题的 CSS 类名
        - 优先级高于统一配置的 titleClassName
        - 3.4.0 版本支持
        """

        detailClassName: Optional[str] = None
        """
        节点详情的 CSS 类名
        - 优先级高于统一配置的 detailClassName
        - 3.4.0 版本支持
        """

    type: Optional[str] = "timeline"


    items: Optional[List[TimelineItem]] = []
    """配置节点数据"""

    source: Optional[Union[str, Dict]] = None
    """数据源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    mode: Optional[str] = "right"
    """
    指定文字相对于时间轴的位置
    - 仅 direction=vertical 时支持
    """

    direction: Optional[str] = None
    """
    - 时间轴方向
    - 默认值：'vertical'
    """

    reverse: Optional[bool] = None
    """
    根据时间倒序显示
    - 默认值：false
    """

    iconClassName: Optional[str] = None
    """
    统一配置的节点图标 CSS 类名
    - 3.4.0 版本支持
    """

    timeClassName: Optional[str] = None
    """
    统一配置的节点时间 CSS 类名
    - 3.4.0 版本支持
    """

    titleClassName: Optional[str] = None
    """
    统一配置的节点标题 CSS 类名
    - 3.4.0 版本支持
    """

    detailClassName: Optional[str] = None
    """
    统一配置的节点详情 CSS 类名
    - 3.4.0 版本支持
    """