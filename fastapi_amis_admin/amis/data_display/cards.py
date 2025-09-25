from fastapi_amis_admin.amis.data_display.card import ACard
from fastapi_amis_admin.amis.types import *


class ACards(AmisNode):
    """
    Cards 卡片组

    卡片展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service这样的，
    具有配置接口初始化数据域功能的组件，
    或者手动进行数据域初始化，
    然后通过source属性，
    获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/cards?page=1#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "cards"
    """cards 指定为卡片组"""

    title: Optional[Optional[str]] = None
    """标题"""

    source: Optional[DataMapping] = None
    """
    - 数据源, 获取当前数据域中的变量
    - 默认值：${items}
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：'amis-grid-header'
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：'amis-grid-footer'
    """

    itemClassName: Optional[str] = None
    """
    - 卡片 CSS 类名
    - 默认值：'col-sm-4 col-md-3'
    """

    card: Optional[ACard] = None
    """配置卡片信息"""

    selectable: Optional[bool] = None
    """
    - 卡片组是否可选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 卡片组是否为多选
    - 默认值：true
    """

    checkOnItemClick: Optional[bool] = None
    """点选卡片内容是否选中卡片"""