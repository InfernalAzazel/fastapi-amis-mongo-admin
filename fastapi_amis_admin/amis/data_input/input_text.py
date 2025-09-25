from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputText(AFormItem):
    """
    InputText 输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-text#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class AddOn(AmisNode):
        """
        其他参数请参考按钮文档
        """
        type: Optional[str] = None
        """请选择 text 、button 或者 submit"""

        label: Optional[str] = None
        """文字说明"""

        position: Optional[Literal['left', 'right']] = 'right'
        """addOn 位置"""



    type: str = "input-text"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[Union[str, API]] = None
    """自动补全"""

    multiple: Optional[bool] = None
    """是否多选"""

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

    addOn: SerializeAsAny[Optional[AddOn]] = None
    """输入框附加组件"""

    trimContents: Optional[bool] = None
    """是否去除首尾空白文本"""

    clearValueOnEmpty: Optional[bool] = None
    """文本内容为空时去掉这个值"""

    creatable: Optional[bool] = None
    """是否可以创建，默认为可以"""

    clearable: Optional[bool] = None
    """是否可清除"""

    resetValue: Optional[str] = None
    """
    - 清除后设置此配置项给定的值
    - 默认值：''
    """

    prefix: Optional[str] = None
    """
    - 前缀
    - 默认值：''
    """

    suffix: Optional[str] = None
    """
    - 后缀
    - 默认值：''
    """

    showCounter: Optional[bool] = None
    """是否显示计数器"""

    minLength: Optional[int] = None
    """限制最小字数"""

    maxLength: Optional[int] = None
    """限制最大字数"""

    transform: Optional[Dict[str, bool]] = None
    """自动转换值"""

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """
    - 输入框边框模式
    - 默认值："full"
    """

    inputControlClassName: Optional[str] = None
    """control 节点的 CSS 类名"""

    nativeInputClassName: Optional[str] = None
    """原生 input 标签的 CSS 类名"""

    nativeAutoComplete: Optional[str] = None
    """
    - 原生 input 标签的 autoComplete 属性
    - 默认值：'off'
    """