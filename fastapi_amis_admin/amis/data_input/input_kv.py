from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputKV(AFormItem):
    """
    InputKV 键值对

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-kv#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-kv"
    """指明为 input-kv 组件"""

    valueType: Optional[str] = None
    """
    - 值类型
    - 默认值: 'input-text'
    """

    keyPlaceholder: Optional[str] = None
    """key 的提示信息的"""
    valuePlaceholder: Optional[str] = None
    """value 的提示信息的"""

    draggable: Optional[bool] = None
    """
    - 是否可拖拽排序
    - 默认值: true
    """

    defaultValue: Optional[Union[str, int, dict]] = None
    """默认值"""

    autoParseJSON: Optional[bool] = None
    """
    - 是否自动转换 json 对象字符串
    - 默认值: true
    """

    keySchema: SerializeAsAny[Optional[SchemaNode]] = None
    """
    - 自定义 key schema
    - 版本: 3.1.0 及以上版本
    """

    valueSchema: SerializeAsAny[Optional[SchemaNode]] = None
    """
    - 自定义 value 的 schema
    - 版本: 3.1.0 及以上版本
    """