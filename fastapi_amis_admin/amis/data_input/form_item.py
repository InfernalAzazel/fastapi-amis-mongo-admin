from fastapi_amis_admin.amis.data_display.remark import ARemarkT
from fastapi_amis_admin.amis.data_display.table import ATableColumn
from fastapi_amis_admin.amis.data_display.table2 import ATableColumn2
from fastapi_amis_admin.amis.types import *


class AFormItem(AmisNode):
    """
    FormItem 普通表单项

    表单项 是组成一个表单的基本单位，它具有的一些特性会帮助我们更好地实现表单操作。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """



    class AutoFill(BaseAmisModel):

        showSuggestion: Optional[bool] = None
        """true 为参照录入，false 自动填充"""

        api: Optional[API] = None
        """自动填充接口/参照录入筛选 CRUD 请求配置"""

        silent: Optional[bool] = None
        """是否展示数据格式错误提示，默认为 true"""

        fillMappinng: SerializeAsAny[Optional[SchemaNode]] = None
        """自动填充/参照录入数据映射配置，键值对形式，值支持变量获取及表达式"""
        trigger: Optional[str] = None

        """showSuggestion 为 true 时，参照录入支持的触发方式，目前支持 change「值变化」｜ focus 「表单项聚焦」"""
        mode: Optional[str] = None

        """showSuggestion 为 true 时，参照弹出方式 dialog, drawer, popOver"""
        labelField: Optional[str] = None

        """showSuggestion 为 true 时，设置弹出 dialog,drawer,popOver 中 picker 的 labelField"""
        position: Optional[str] = None

        """showSuggestion 为 true 时，参照录入 mode 为 popOver 时，可配置弹出位置"""
        size: Optional[str] = None

        """showSuggestion 为 true 时，参照录入 mode 为 dialog 时，可设置大小"""
        columns: SerializeAsAny[Optional[List[Union["ATableColumn", "ATableColumn2"]]]] = None
        """showSuggestion 为 true 时，数据展示列配置"""

        filter: SerializeAsAny[Optional[SchemaNode]] = None
        """showSuggestion 为 true 时，数据查询过滤条件"""

    class StaticSchema(SchemaNode):
        limit: Optional[int] = None
        """
        - 2.4.0 select、checkboxes 等选择类组件多选时展示态展示的数量
        - 默认值：10
        """

    class Validation(BaseAmisModel):
        """
        表单项值发生变化即校验

        默认校验是当进行行为操作时，对表单项进行校验，如果你想每次表单项的值发生变化的时候就校验，请配置 "validateOnChange": true

        参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formitem#%E6%94%AF%E6%8C%81%E7%9A%84%E6%A0%BC%E5%BC%8F%E6%A0%A1%E9%AA%8C
        """
        isEmail: Optional[bool] = None
        """必须是 电子邮件"""

        isUrl: Optional[bool] = None
        """必须是 Url"""

        isNumeric: Optional[bool] = None
        """必须是 数值"""

        isAlpha: Optional[bool] = None
        """必须是 字母"""

        isAlphanumeric: Optional[bool] = None
        """必须是 字母或者数字"""

        isInt: Optional[bool] = None
        """必须是 整形"""

        isFloat: Optional[bool] = None
        """必须是 浮点形"""

        isLength: Optional[int] = None
        """是否长度正好等于设定值"""

        minLength: Optional[int] = None
        """最小长度"""

        maxLength: Optional[int] = None
        """最大长度"""

        maximum: Optional[int] = None
        """最大值"""

        minimum: Optional[int] = None
        """最小值"""

        equals: Optional[str] = None
        """当前值必须完全等于 xxx"""

        equalsField: Optional[str] = None
        """当前值必须与 xxx 变量值一致"""

        isJson: Optional[bool] = None
        """是否是合法的 Json 字符串"""

        isUrlPath: Optional[bool] = None
        """是 url 路径"""

        isPhoneNumber: Optional[bool] = None
        """是否为合法的手机号码"""

        isTelNumber: Optional[bool] = None
        """是否为合法的电话号码"""

        isZipcode: Optional[bool] = None
        """是否为邮编号码"""

        isId: Optional[bool] = None
        """是否为身份证号码，支持 18 位和 15 位验证，单个验证请使用 isId18 / isId15"""

        matchRegexp: Optional[str] = None
        """
        - 必须命中某个正则
        - matchRegexp${n}:/foo/ 这样的需要手动加入字段
        """

        isDateTimeSame: Optional[bool] = None
        """日期和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeBefore: Optional[bool] = None
        """日期早于目标日期，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeAfter: Optional[bool] = None
        """日期晚于目标日期，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeSameOrBefore: Optional[bool] = None
        """日期早于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeSameOrAfter: Optional[bool] = None
        """日期晚于目标日期或和目标日期相同，支持指定粒度，默认到毫秒 millisecond"""

        isDateTimeBetween: Optional[bool] = None
        """日期处于目标日期范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""

        isTimeSame: Optional[bool] = None
        """时间和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeBefore: Optional[bool] = None
        """时间早于目标时间，支持指定粒度，默认到毫秒 millisecond"""

        isTimeAfter: Optional[bool] = None
        """时间晚于目标时间，支持指定粒度，默认到毫秒 millisecond"""

        isTimeSameOrBefore: Optional[bool] = None
        """时间早于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeSameOrAfter: Optional[bool] = None
        """时间晚于目标时间或和目标时间相同，支持指定粒度，默认到毫秒 millisecond"""

        isTimeBetween: Optional[bool] = None
        """时间处于目标时间范围，支持指定粒度和区间的开闭形式，默认到毫秒 millisecond，左右开区间'()'"""

        isVariableName: Optional[bool] = None
        """是否为合法的变量名，默认规则为 /^[a-zA-Z_]+[a-zA-Z0-9]*$/ 可以自己指定如 {isVariableName: /^a.*$/}"""

    type: str = "input-text"
    """指定表单项类型"""

    className: Optional[str] = None
    """表单最外层类名"""

    inputClassName: Optional[str] = None
    """表单控制器类名"""

    labelClassName: Optional[str] = None
    """label 的类名"""

    name: Optional[str] = None
    """字段名，指定该表单项提交时的 key"""

    value: Optional[str] = None
    """表单默认值"""

    label: Union[bool, Template, None] = None
    """表单项标签"""

    labelAlign: Optional[str] = None
    """
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值：'right'
    """

    labelRemark: SerializeAsAny[Optional[ARemarkT]] = None
    """表单项标签描述"""

    description: Optional[Template] = None
    """表单项描述"""

    placeholder: Optional[str] = None
    """表单项描述"""

    inline: Optional[bool] = None
    """是否为 内联 模式"""

    strictMode: Optional[bool] = None
    """通过配置 false 可以及时获取所有表单里面的数据，否则可能会有不同步"""

    submitOnChange: Optional[bool] = None
    """是否该表单项值发生变化时就提交当前表单。"""

    disabled: Optional[bool] = None
    """当前表单项是否是禁用状态"""

    disabledOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""

    visible: Optional[bool] = None
    """当前表单项是否禁用的条件"""

    visibleOn: Optional[Expression] = None
    """当前表单项是否禁用的条件"""

    required: Optional[bool] = None
    """是否为必填"""

    requiredOn: Optional[Expression] = None
    """通过表达式来配置当前表单项是否为必填"""

    validations: SerializeAsAny[Optional[Union["Validation", Expression]]] = None
    """表单项值格式验证，支持设置多个，多个规则用英文逗号隔开"""

    validateApi: Optional[API] = None
    """表单校验接口"""

    autoFill: Optional[AutoFill] = None
    """数据录入配置，自动填充或者参照录入"""

    static: Optional[bool] = None
    """2.4.0 当前表单项是否是静态展示，目前支持静支持静态展示的表单项"""

    staticClassName: Optional[str] = None
    """2.4.0 静态展示时的类名"""

    staticLabelClassName: Optional[str] = None
    """2.4.0 静态展示时的 Label 的类名"""

    staticInputClassName: Optional[str] = None
    """2.4.0 静态展示时的 value 的类名"""

    staticSchema: SerializeAsAny[Optional[StaticSchema]] = None
    """2.4.0 自定义静态展示方式"""
