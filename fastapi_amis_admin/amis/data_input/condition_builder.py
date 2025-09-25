from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AConditionBuilder(AFormItem):
    """
    组合条件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/condition-builder#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Field(AmisNode):
        type: str = "text"

        label: Optional[str] = None
        """字段名称"""

        placeholder: Optional[str] = None
        """占位符"""

        operators: Optional[List[str]] = None
        """
        - 定义可以用于该字段的操作符列表。这些操作符用于构建查询条件
        - 默认值：[ 'equal', 'not_equal', 'is_empty', 'is_not_empty', 'like', 'not_like', 'starts_with', 'ends_with' ]
        """

        defaultOp: Optional[str] = None
        """
        - 设置默认使用的操作符
        - 默认值：'equal'
        """

    class Text(Field):
        """文本"""

    class Number(Field):
        """数字"""

        type: str = "number"

        minimum: Optional[int] = None
        """最小值"""

        maximum: Optional[int] = None
        """最大值"""

        step: Optional[int] = None
        """步长"""

    class Date(Field):
        """日期"""

        type: str = "date"

        defaultValue: Optional[str] = None
        """默认值"""

        format: Optional[str] = None
        """
        - 格式
        - 默认值：'YYYY-MM-DD'
        """

        inputFormat: Optional[str] = None
        """
        - 显示的日期格式
        - 默认值：'YYYY-MM-DD'
        """

    class Datetime(Date):
        """日期时间"""

        type: str = "datetime"

        timeFormat: Optional[str] = None
        """
        - 时间格式，决定输入框有哪些
        - 默认值：'HH:mm'
        """


    class Time(Date):
        """时间"""

        type: str = "time"

    class Select(Field):
        """下拉选择"""

        type: str = "select"

        options: Optional[OptionsNode] = None
        """选项列表"""

        source: Optional[API] = None
        """动态选项，请配置 api"""

        searchable: Optional[bool] = None
        """是否可以搜索"""

        autoComplete: Optional[API] = None
        """自动提示补全，每次输入新内容后，将调用接口，根据接口返回更新选项"""

        maxTagCount: Optional[int] = None
        """可以限制标签的最大展示数量，超出数量的部分会收纳到 Popover 中，可以通过 overflowTagPopover 配置 Popover 相关的属性，注意该属性仅在多选模式开启后生效"""

    class Custom(Field):
        value: Optional[Union[str, dict]] = None
        """字段配置右边值需要渲染的组件，支持 amis 输入类组件或自定义输入类组件"""

    class Option(AmisNode):
        label: str
        value: Any

    class InputSettings(AmisNode):
        type: str = 'text'
        """"类型: 'text', 'number', 'boolean', 'date', 'time', 'datetime', 'select'"""

        step: Optional[float] = None
        """"数字类型 - 步长"""

        min: Optional[float] = None
        """"数字类型 - 最小值"""

        max: Optional[float] = None
        """"数字类型 - 最大值"""

        precision: Optional[int] = None
        """"数字类型 - 精度"""

        format: Optional[str] = None
        """"日期时间类型 - 格式"""

        inputFormat: Optional[str] = None
        """"日期时间类型 - 输入框格式"""

        timeFormat: Optional[str] = None
        """"日期时间类型 - 时间格式"""

        options: Optional[List['AConditionBuilder.Option']] = None
        """"选择类型 - 选项集合"""

        multiple: Optional[bool] = None
        """"选择类型 - 是否多选"""

        trueLabel: Optional[str] = None
        """"布尔类型 - 真值 label"""

        falseLabel: Optional[str] = None
        """"布尔类型 - 假值 label"""

        defaultValue: Optional[Any] = None
        """"默认值"""


    type: str = "condition-builder"
    """指定为 condition-builder 组件"""

    className: Optional[str] = None
    """外部 dom 类名"""

    fieldClassName: Optional[str] = None
    """输入字段的类名"""

    source: Optional[str] = None
    """通过远程拉取配置项"""

    embed: Optional[bool] = None
    """
    - 内嵌展示
    - 默认值：true
    """

    fields: SerializeAsAny[Optional[List[Union[Text, Number, Date, Datetime, Time, Select, Custom]]]] = None
    """字段配置"""

    showANDOR: Optional[bool] = None
    """用于 simple 模式下显示切换按钮"""

    showNot: Optional[bool] = None
    """
    - 是否显示「非」按钮
    - 默认值：true
    """

    draggable: Optional[bool] = None
    """
    - 是否可拖拽
    - 默认值：true
    """

    searchable: Optional[bool] = None
    """字段是否可搜索"""

    selectMode: Optional[Literal['list', 'tree', 'chained']] = None
    """
    - 组合条件左侧选项类型
    - 默认值：'list'
    - 版本：'chained'模式需要3.2.0及以上版本
    """

    addBtnVisibleOn: Optional[bool] = None
    """
    - 表达式：控制按钮“添加条件”的显示。参数为depth、breadth，分别代表深度、长度。表达式需要返回boolean类型
    - 版本：3.2.0
    """

    inputSettings: SerializeAsAny[Optional[InputSettings]] = None
    """
    - 开启公式编辑模式时的输入控件类型
    - 版本：3.2.0
    """

    formula: Optional[dict] = None
    """
    - 字段输入控件变成公式编辑器
    - 版本：3.2.0
    """

    showIf: Optional[bool] = None
    """
    - 开启后条件中额外还能配置启动条件
    - 版本：3.2.0
    """

    formulaForIf: Optional[dict] = None
    """
    - 给 showIF 表达式用的公式信息
    - 版本：3.4.0
    """


