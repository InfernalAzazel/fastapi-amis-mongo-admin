from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ANestedSelect(AFormItem):
    """
    NestedSelect 级联选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/nestedselect#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "nested-select"

    options: SerializeAsAny[Optional[OptionsNode]] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[bool] = None
    """
    - 拼接符
    - 默认值：false
    """

    labelField: Optional[bool] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[bool] = None
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

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    cascade: Optional[bool] = None
    """
    - 设置 true时，当选中父节点时不自动选择子节点
    - 默认值：false
    """

    withChildren: Optional[bool] = None
    """
    - 选中父节点时，值里面将包含子节点的值
    - 默认值：false
    """

    onlyChildren: Optional[bool] = None
    """
    - 多选时，选中父节点时，是否只将其子节点加入到值中
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 可否搜索
    - 默认值：false
    """

    searchPromptText: Optional[str] = None
    """
    - 搜索框占位文本
    - 默认值：'输入内容进行检索'
    """

    noResultsText: Optional[str] = None
    """
    - 无结果时的文本
    - 默认值：'未找到任何结果'
    """

    multiple: Optional[bool] = None
    """
    - 可否多选
    - 默认值：false
    """

    hideNodePathLabel: Optional[bool] = None
    """
    - 是否隐藏选择框中已选择节点的路径 label 信息
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    maxTagCount: Optional[int] = None
    """
    - 标签的最大展示数量
    - 版本：3.3.0
    """

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    - 版本：3.3.0
    """