from fastapi_amis_admin.amis.types import *


class AUUID(AmisNode):
    """
    UUID 字段

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/uuid
    """

    type: str = "uuid"

    name: Optional[str] = None
    """字段名称"""

    length: Optional[int] = None
    """如果设置，则生成短随机数，如果未设置，则生成 UUID"""