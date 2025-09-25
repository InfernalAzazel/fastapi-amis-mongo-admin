from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class APicker(AFormItem):
    """
    Picker 列表选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """



    class OverflowConfig(BaseModel):
        maxTagCount: Optional[int] = None
        """
        - 标签的最大展示数量
        - 默认值：-1
        """

        displayPosition: Optional[List[Literal['select', 'crud']]] = None
        """
        - 收纳标签生效的位置
        - 默认值：['select', 'crud']
        """

        overflowTagPopover: Optional[Dict[str, Any]] = None
        """
        - 选择器内收纳标签的 Popover 配置
        - 默认值：{"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
        """

        overflowTagPopoverInCRUD: Optional[Dict[str, Any]]
        """
        - CRUD 顶部内收纳标签的 Popover 配置
        - 默认值：{"placement": "bottom", "trigger": "hover", "showArrow": false, "offset": [0, 10]}
        """

    type: str = "picker"

    options: Optional[Union[List[Dict[str, Any]], List[str]]] = None
    """选项组"""

    source: Optional[Union[str, Dict[str, Any]]] = None
    """动态选项组"""

    multiple: Optional[bool] = None
    """是否为多选"""

    delimiter: Optional[bool] = None
    """
    - 拼接符
    - 默认值：false
    """

    labelField: Optional[bool] = None
    """
    - 选项标签字段
    - 默认值："label"
    """

    valueField: Optional[bool] = None
    """
    - 选项值字段
    - 默认值："value"
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

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    modalTitle: Optional[str] = None
    """
    - 设置模态框的标题
    - 默认值：'请选择'
    """

    modalMode: Optional[Literal['dialog', 'drawer']] = None
    """
    - 设置 dialog 或者 drawer，用来配置弹出方式
    - 默认值："dialog"
    """

    pickerSchema: Optional[SerializeAsAny[Optional[Union[SchemaNode]]] ] = None
    """
    - 即用 List 类型的渲染，来展示列表信息，更多配置参考 CRUD
    - 默认值："{mode: 'list', listItem: {title: '${label}'}}"
    """

    embed: Optional[bool] = None
    """
    - 是否使用内嵌模式
    - 默认值：false
    """

    overflowConfig: SerializeAsAny[Optional[OverflowConfig]] = None
    """
    - 开启最大标签展示数量的相关配置
    - 版本：3.4.0
    """

    size: Optional[Literal['xs', 'sm', 'md', 'lg', 'xl', 'full']] = None
    """组件大小"""