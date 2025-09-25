from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ACheckboxes(AFormItem):
    """
    Checkboxes 复选框

    用于实现多选

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/checkboxes#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "checkboxes"
    """指定为 checkboxes 组件"""

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[str] = None
    """	
    - 拼接符
    - 默认值：','
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    columnsCount: Optional[int] = None
    """
    - 选项按几列显示，默认为一列
    - 默认值：1
    """

    menuTpl: Optional[str] = None
    """支持自定义选项渲染"""

    checkAll: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：false
    """

    inline: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：true
    """

    defaultCheckAll: Optional[bool] = None
    """
    - 默认是否全选
    - 默认值：false
    """

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
    """

    createBtnLabel: Optional[str] = None
    """
    - 新增选项
    - 默认值：'新增选项'
    """

    addControls: SerializeAsAny[Optional[List[AFormItem]]] = None
    """自定义新增表单项"""

    addApi: Optional[API] = None
    """配置新增选项接口"""

    editable: Optional[bool] = None
    """
    - 编辑选项
    - 默认值：false
    """

    editControls: SerializeAsAny[Optional[List[AFormItem]]] = None
    """自定义编辑表单项"""

    editApi: Optional[API] = None
    """配置编辑选项接口"""

    removable: Optional[bool] = None
    """
    - 删除选项
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """
    - 配置删除选项接口
    - 默认值：false
    """

    optionType: Optional[Literal["default", "button"]] = None
    """
    - 按钮模式
    - 默认值：'default'
    """

    itemClassName: Optional[str] = None
    """	选项样式类名"""

    labelClassName: Optional[str] = None
    """labelClassName"""