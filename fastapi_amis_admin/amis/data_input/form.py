from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *

class AForm(AmisNode):
    """
    Form 表单

    表单是 amis 中核心组件之一，主要作用是提交或者展示表单数据。

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/index#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(AmisNode):
        fetchSuccess: Optional[str] = None
        """获取成功时提示"""

        fetchFailed: Optional[str] = None
        """获取失败时提示"""

        saveSuccess: Optional[str] = None
        """保存成功时提示"""

        saveFailed: Optional[str] = None
        """保存失败时提示"""

    class Horizontal(AmisNode):
        left: Optional[int] = None
        """左侧标签的宽度比例"""

        right: Optional[int] = None
        """右侧控制器的宽度比"""

        justify: Optional[bool] = None

    type: str = "form"
    """指定 Form 渲染器"""

    name: Optional[str] = None
    """设置一个名字后，方便其他组件与其通信"""

    mode: Optional[Literal['normal', 'horizontal', 'inline']] = None
    """表单展示方式"""

    horizontal: SerializeAsAny[Optional["Horizontal"]] = None
    """
    - 当 mode 为 horizontal 时有用，用来控制 label 的展示占比
    - 默认值: '{"left":2, "right":10, "justify": false}'"""

    labelAlign: Optional[Literal["right", "left"]] = None
    """ 
    - 表单项标签对齐方式，默认右对齐，仅在 mode为horizontal 时生效
    - 默认值: right
    """

    labelWidth: Union[int, str, None] = None
    """表单项标签自定义宽度"""

    title: Optional[Optional[str]] = None
    """
    - Form 的标题 
    - 默认值'表单'"""

    submitText: Optional[Optional[str]] = None
    """
    - 默认的提交按钮名称，如果设置成空，则可以把默认按钮去掉
    - 默认值：'提交'
    """

    className: Optional[str] = None
    """外部 Dom 的类名"""

    body: SerializeAsAny[Optional[List[Union["AFormItem", SchemaNode]]]] = None
    """Form 表单项集合"""

    actions: SerializeAsAny[Optional[List["AAction"]]] = None
    """Form 提交按钮，成员为 Action"""

    messages: SerializeAsAny[Optional[Messages]] = None
    """消息提示覆写，默认消息读取的是 API 返回的消息，但是在此可以覆写它"""

    wrapWithPanel: Optional[bool] = None
    """
    - 是否让 Form 用 panel 包起来，设置为 false 后，actions 将无效
    - 默认值：true
    """

    panelClassName: Optional[str] = None
    """外层 panel 的类名"""

    api: Optional[API] = None
    """Form 用来保存数据的 api"""

    initApi: Optional[API] = None
    """Form 用来获取初始数据的 api"""

    rules: Optional[list] = None
    """表单组合校验规则"""

    interval: Optional[int] = None
    """
    - 刷新时间(最低 3000)
    - 默认值：3000
    """

    silentPolling: Optional[bool] = None
    """
    - 配置刷新时是否显示加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[str] = None
    """
    通过表达式 来配置停止刷新的条件
    """

    initAsyncApi: Optional[API] = None
    """Form 用来获取初始数据的 api,与 initApi 不同的是，会一直轮询请求该接口，直到返回 finished 属性为 true 才 结束"""

    initFetch: Optional[bool] = None
    """
    - 设置了 initApi 或者 initAsyncApi 后，默认会开始就发请求，设置为 false 后就不会起始就请求接口
    - 默认值：true
    """

    initFetchOn: Optional[str] = None
    """用表达式来配置"""

    initFinishedField: Optional[Optional[str]] = None
    """
    - 设置了 initAsyncApi 后，默认会从返回数据的 data.finished 来判断是否完成，也可以设置成其他的 xxx，就会从 data.xxx 中获取
    - 默认值：'finished'
    """

    initCheckInterval: Optional[int] = None
    """
    - 设置了 initAsyncApi 以后，默认拉取的时间间隔
    - 默认值：3000
    """

    asyncApi: Optional[API] = None
    """设置此属性后，表单提交发送保存接口后，还会继续轮询请求该接口，直到返回 finished 属性为 true 才 结束"""

    checkInterval: Optional[int] = None
    """
    - 轮询请求的时间间隔，默认为 3 秒。设置 asyncApi 才有效
    默认值：3000
    """

    finishedField: Optional[Optional[str]] = None
    """
    - 如果决定结束的字段名不是 finished 请设置此属性，比如 is_success
    - 默认值：'finished'
    """

    submitOnChange: Optional[bool] = None
    """
    - 表单修改即提交
    - 默认值：false
    """

    submitOnInit: Optional[bool] = None
    """
    - 初始就提交一次
    - 默认值：false
    """

    resetAfterSubmit: Optional[bool] = None
    """
    - 提交后是否重置表单
    - 默认值：false
    """

    primaryField: Optional[str] = None
    """
    - 设置主键 id, 当设置后，检测表单是否完成时（asyncApi），只会携带此数据
    - 默认值：'id'
    """

    target: Optional[str] = None
    """
    - 默认表单提交自己会通过发送 api 保存数据，但是也可以设定另外一个 form 的 name 值，或者另外一个 CRUD 模型的 name 值。 
    - 如果 target 目标是一个 Form ，则目标 Form 会重新触发 initApi，api 可以拿到当前 form 数据。
    - 如果目标是一个 CRUD 模型，则目标模型会重新触发搜索，参数为当前 Form 数据。
    - 当目标是 window 时，会把当前表单的数据附带到页面地址上。
    """

    redirect: Optional[str] = None
    """设置此属性后，Form 保存成功后，自动跳转到指定页面。支持相对地址，和绝对地址（相对于组内的)"""

    reload: Optional[str] = None
    """操作完后刷新目标对象。请填写目标组件设置的 name 值，如果填写为 window 则让当前页面整体刷新。"""

    autoFocus: Optional[bool] = None
    """
    - 是否自动聚焦
    - 默认值：false
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 指定是否可以自动获取上层的数据并映射到表单项上
    - 默认值：true
    """

    persistData: Optional[str] = None
    """指定一个唯一的 key，来配置当前表单是否开启本地缓存"""

    persistDataKeys: Optional[List[str]] = None
    """指指定只有哪些 key 缓存"""

    clearPersistDataAfterSubmit: Optional[bool] = None
    """
    - 指定表单提交成功后是否清除本地缓存
    - 默认值：true
    """

    preventEnterSubmit: Optional[bool] = None
    """
    - 禁用回车提交表单
    - 默认值：false
    """

    trimValues: Optional[bool] = None
    """
    - trim 当前表单项的每一个值
    - 默认值：false
    """

    promptPageLeave: Optional[bool] = None
    """
    - form 还没保存，即将离开页面前是否弹框确认。
    - 默认值：false
    """

    columnCount: Optional[int] = None
    """
    - 表单项显示为几列
    - 默认值：0
    """

    inheritData: Optional[bool] = None
    """
    - 默认表单是采用数据链的形式创建个自己的数据域
    - 表单提交的时候只会发送自己这个数据域的数据
    - 如果希望共用上层数据域可以设置这个属性为 false
    - 这样上层数据域的数据不需要在表单中用隐藏域或者显式映射才能发送了
    """

    static: Optional[bool] = None
    """
    - 2.4.0 整个表单静态方式展示
    - 详情请查看示例页: https://aisuda.bce.baidu.com/amis/examples/form/switchDisplay
    """

    staticClassName: Optional[str] = None
    """2.4.0 表单静态展示时使用的类名"""

    closeDialogOnSubmit: Optional[bool] = None
    """提交的时候是否关闭弹窗。当 form 里面有且只有一个弹窗的时候，本身提交会触发弹窗关闭，此属性可以关闭此行为"""

    debug: Optional[bool] = None

