from fastapi_amis_admin.amis.types import *


class ASearchBox(AmisNode):
    """
    Search Box 搜索框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/search-box#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "search-box"

    className: Optional[str] = None
    """外层 CSS 类名"""

    mini: Optional[bool] = None
    """是否为 mini 模式"""

    searchImediately: Optional[bool] = None
    """是否立即搜索"""

    clearAndSubmit: Optional[bool] = None
    """
    - 清空搜索框内容后立即执行搜索
    - 版本：2.8.0
    """

    disabled: Optional[bool] = None
    """
    - 是否为禁用状态
    - 默认值：false
    - 版本：6.0.0
    """

    loading: Optional[bool] = None
    """
    - 是否处于加载状态
    - 默认值：false
    - 版本：6.0.0
    """