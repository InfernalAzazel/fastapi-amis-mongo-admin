from fastapi_amis_admin.amis.types import *


class ADate(AmisNode):
    """
    Date 日期时间

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/date?page=1#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['date', 'static-date'] = "date"
    """如果在 Table、Card 和 List 中，为"date"；在 Form 中用作静态展示，为"static-date"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的日期数值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    placeholder: Optional[str] = None
    """
    - 占位内容
    - 默认值：'-'
    """

    displayFormat: Optional[str] = None
    """
    - 展示格式, 更多格式类型请参考 文档，版本号 3.4.0 及以上支持
    - 默认值：'YYYY-MM-DD'
    """

    valueFormat: Optional[str] = None
    """
    - 数据格式，默认为时间戳。更多格式类型请参考 文档
    - 默认值：'X'
    """

    fromNow: Optional[bool] = None
    """
    - 是否显示相对当前的时间描述，比如: 11 小时前、3 天前、1 年前等，fromNow 为 true 时，format 不生效。
    - 默认值：false
    """

    updateFrequency: Optional[int] = None
    """
    - 更新频率， 默认为 1 分钟
    - 默认值：60000
    """

    displayTimeZone: Optional[str] = None
    """设置日期展示时区，可设置清单参考：https://gist.github.com/diogocapela/12c6617fc87607d11fd62d2a4f42b02a"""