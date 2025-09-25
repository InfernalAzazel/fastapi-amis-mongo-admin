from typing import Optional
from pydantic import SerializeAsAny
from fastapi_amis_admin.amis.data_input.form import AForm
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputSubForm(AFormItem):
    """
    InputSubForm 子表单

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-sub-form#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-sub-form"

    multiple: Optional[bool] = None
    """
    - 是否为多选模式
    - 默认值：false
    """

    labelField: Optional[str] = None
    """当值中存在这个字段，则按钮名称将使用此字段的值来展示。"""

    btnLabel: Optional[str] = None
    """
    - 按钮默认名称
    - 默认值："设置"
    """

    minLength: Optional[int] = None
    """
    - 限制最小个数。
    - 默认值：0
    """

    maxLength: Optional[int] = None
    """
    - 限制最大个数。
    - 默认值：0
    """

    draggable: Optional[bool] = None
    """是否可拖拽排序"""

    addable: Optional[bool] = None
    """是否可新增"""

    removable: Optional[bool] = None
    """是否可删除"""

    addButtonClassName: Optional[str] = None
    """
    - 新增按钮 CSS 类名
    - 默认值：""
    """

    itemClassName: Optional[str] = None
    """
    - 值元素 CSS 类名
    - 默认值：""
    """

    itemsClassName: Optional[str] = None
    """
    - 值包裹元素 CSS 类名
    - 默认值：""
    """

    form: SerializeAsAny[Optional[AForm]] = None
    """子表单配置，同 Form"""

    addButtonText: Optional[str] = None
    """
    - 自定义新增一项的文本
    - 默认值：""
    """

    showErrorMsg: Optional[bool] = None
    """
    - 是否在左下角显示报错信息
    - 默认值：true
    """
