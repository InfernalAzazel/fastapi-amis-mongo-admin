from fastapi_amis_admin.amis.types import *


class ACalendar(AmisNode):
    """
    Calendar 日历日程

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/calendar#calendar-%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    class Schedule(AmisNode):
        startTime: str
        endTime: str
        content: Union[str, int, dict, None] = None
        className: Optional[str] = None

    type: str = "calendar"

    schedules: SerializeAsAny[Union[List[Schedule], str, None]] = None
    """日历中展示日程，可设置静态数据或从上下文中取数据，startTime 和 endTime 格式参考文档，className 参考背景色"""

    scheduleClassNames: Optional[List[str]] = None
    """
    - 日历中展示日程的颜色，参考背景色
    - 默认值：['bg-warning', 'bg-danger', 'bg-success', 'bg-info', 'bg-secondary']
    """

    scheduleAction: SerializeAsAny[Optional[SchemaNode]] = None
    """自定义日程展示"""

    largeMode: Optional[bool] = None
    """
    - 放大模式
    - 默认值：false
    """

    todayActiveStyle: Union[str, dict, None] = None
    """今日激活时的自定义样式"""
