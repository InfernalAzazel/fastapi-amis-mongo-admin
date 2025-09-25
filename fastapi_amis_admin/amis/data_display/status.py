from fastapi_amis_admin.amis.types import *


class AStatus(AmisNode):
    """
    Status 状态

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/status#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Source(BaseModel):
        label: Optional[str] = None
        """
        - 映射文本
        - 版本：2.8.0
        """

        icon: Optional[str] = None
        """
        - 映射图标
        - 版本：2.8.0
        """

        color: Optional[str] = None
        """
        - 映射状态颜色
        - 版本：2.8.0
        """

        className: Optional[str] = None
        """
        - 映射状态的独立 CSS 类名
        - 版本：2.8.0
        """

    type: str = "status"  # Specify as Status renderer

    className: Optional[str] = None
    """外层 Dom 的 CSS 类名"""

    placeholder: Optional[str] = None
    """占位文本"""

    map: Optional[Dict[str, str]] = None
    """
    - 映射图标
    - 版本：2.3.0
    """

    labelMap: Optional[Dict[str, str]] = None
    """
    - 映射文本
    - 版本：2.3.0
    """

    source: SerializeAsAny[Optional[Union[DataMapping, Source]]] = None
    """
    - 自定义映射状态，支持数据映射
    - 版本：2.8.0
    """