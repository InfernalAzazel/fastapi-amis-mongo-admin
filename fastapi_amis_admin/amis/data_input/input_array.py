from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputArray(AFormItem):
    """
    InputArray 数组输入框

    InputArray 是一种简化的 Combo，用于输入多个某种类型的表单项，提交的时将以数组的形式提交。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-array#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-array"
    """指明为array组件"""
    items: SerializeAsAny[Optional[Union[AFormItem, SchemaNode]]] = None
    """配置单项表单类型"""
    addable: Optional[bool] = None
    """是否可新增"""
    removable: Optional[bool] = None
    """是否可删除"""
    draggable: Optional[bool] = None
    """是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段"""
    draggableTip: Optional[str] = None
    """
    - 可拖拽的提示文字，
    - 默认值：'可通过拖动每行中的【交换】按钮进行顺序调整'
    """
    addButtonText: Optional[str] = None
    """
    - 新增按钮文字
    - 默认值：'新增'
    """
    minLength: Optional[int] = None
    """限制最小长度"""
    maxLength: Optional[int] = None
    """限制最大长度"""
    scaffold: Optional[Any] = None
    """新增成员时的默认值，一般根据items的数据类型指定需要的默认值"""