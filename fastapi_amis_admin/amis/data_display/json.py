from fastapi_amis_admin.amis.types import *


class AJSON(AmisNode):
    """
    JSON 展示组件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/json#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['json', 'static-json'] = 'json'
    """如果在 Table、Card 和 List 中，为'json'；在 Form 中用作静态展示，为'static-json'"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[Union[dict, str]]= None
    """json 值，如果是 string 会自动 parse"""

    source: Optional[str] = None
    """json 值，如果是 string 会自动 parse"""

    placeholder: Optional[str] = None
    """
    - 占位文本
    - 默认值：'-'
    """

    levelExpand: Optional[int] = None
    """
    - 默认展开的层级
    - 默认值：1
    """

    jsonTheme: Optional[Literal['twilight', 'eighties']] = None
    """
    - 主题
    - 默认值：'twilight'
    """

    mutable: Optional[bool] = None
    """
    - 是否可修改
    - 默认值：false
    """

    displayDataTypes: Optional[bool] = None
    """
    - 是否显示数据类型
    - 默认值：false
    """

    ellipsisThreshold: Optional[Union[int, bool]] = None
    """
    - 设置字符串的最大展示长度，点击字符串可以切换全量/部分展示方式，默认展示全量字符串
    - 默认值：false
    """