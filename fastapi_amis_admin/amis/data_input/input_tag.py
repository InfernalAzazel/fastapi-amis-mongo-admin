from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputTag(AFormItem):
    """
    InputTag 标签选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-tag#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-tag"

    options: Optional[OptionsNode] = None
    """选项组"""

    optionsTip: Optional[Union[List[Dict[str, Any]], List[str]]] = None
    """
    - 选项提示
    - 默认值："最近您使用的标签"
    """

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
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

    clearable: Optional[bool] = None
    """
    - 在有值的时候是否显示一个删除图标在右侧
    - 默认值：false
    """

    resetValue: Optional[str] = None
    """
    - 删除后设置此配置项给定的值
    - 默认值：""
    """

    max: Optional[int] = None
    """允许添加的标签的最大数量"""

    maxTagLength: Optional[int] = None
    """单个标签的最大文本长度"""

    maxTagCount: Optional[int] = None
    """标签的最大展示数量"""

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    """

    enableBatchAdd: Optional[bool] = None
    """
    - 是否开启批量添加模式
    - 默认值：false
    """

    separator: Optional[str] = None
    """
    - 开启批量添加后，输入多个标签的分隔符
    - 默认值："-"
    """