from fastapi_amis_admin.amis.function.action import *
from fastapi_amis_admin.amis.types import *


class ASparkline(AmisNode):
    """
    Sparkline 走势图

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/sparkline#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "sparkline"

    name: Optional[str] = None
    """关联的变量"""

    width: Optional[int] = None
    """宽度"""

    height: Optional[int] = None
    """高度"""

    placeholder: Optional[str] = None
    """数据为空时显示的内容"""

    value: Optional[List[Union[int, float]]] = None
    """值"""

    clickAction: SerializeAsAny[Optional[AAction]] = None
    """单击时的操作"""