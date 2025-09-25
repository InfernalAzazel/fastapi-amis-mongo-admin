from fastapi_amis_admin.amis.types import *


class AJSONSchema(AmisNode):
    """
    JSONSchema

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/json-schema#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str =  'json-schema'

    name: Optional[str] =  None
    """
    - 字段名称
    - 默认值: 'value'
    """

    label: Optional[str] = None
    """标签"""

    schema: Optional[Union[str, Dict[str, Any]]] = None
    """指定 json-schema"""
