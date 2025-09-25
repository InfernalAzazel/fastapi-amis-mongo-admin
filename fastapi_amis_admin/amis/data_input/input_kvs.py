from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputKVS(AFormItem):
    """
    InputKVS 键值对象

    - 版本: 2.1.0 及以上版本

    这个组件的功能和 input-kv 类似，input-kv 的 value 值只支持一个对象，
    input-kvs 的最大不同就是 value 支持对象和数组，可以用来支持深层结构编辑。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-kvs
    """

    type: str = "input-kvs"
    """指明为 input-kvs 组件"""

    addButtonText: Optional[str] = None
    """默认的 'New field'，而是 Add 按钮的文本"""

    draggable: Optional[bool] = None

    """默认 True，是否允许拖拽排序"""
    keyItem: SerializeAsAny[Optional[SchemaNode]] = None
    """key 字段"""

    valueItems: SerializeAsAny[Optional[list[SchemaNode]]] = None
    """键的项"""