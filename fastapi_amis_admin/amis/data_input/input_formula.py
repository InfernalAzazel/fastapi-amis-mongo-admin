from typing import Optional, Literal
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputFormula(AFormItem):
    """
    InputFormula 公式编辑器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-formula#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-formula"
    """指明为 input-formula 组件"""

    title: Optional[Optional[str]] = None
    """
    - 弹框标题
    - 默认值：'公式编辑器'
    """

    header: Optional[str] = None
    """编辑器 header 标题，如果不设置，默认使用表单项label字段"""

    evalMode: Optional[bool] = None
    """
    - 表达式模式 或者 模板模式，模板模式则需要将表达式写在 ${ 和 } 中间
    - 默认值：true
    """

    variables: Optional[list[dict]] = None
    """可用变量"""

    variableMode: Literal['tabs', 'tree', 'list'] = 'list'
    """
    - 可配置成 tabs 或者 tree 默认为列表，支持分组
    - 默认值：'list'
    """

    functions: Optional[list[dict]] = None
    """可以不设置，默认就是 amis-formula 里面定义的函数，如果扩充了新的函数则需要指定"""

    inputMode: Optional[Literal['button', 'input-button', 'input-group']] = None
    """控件的展示模式"""

    icon: Optional[str] = None
    """可以不设置，默认就是 amis-formula 里面定义的函数，如果扩充了新的函数则需要指定"""

    btnLabel: Optional[str] = None
    """
    - 按钮文本，inputMode为button时生效
    - 默认值：'公示编辑'
    """

    level: Optional[Literal['info', 'success', 'warning','danger','link','primary','dark','light']] = None
    """
    - 按钮样式
    - 默认值：'default'
    """

    allowInput: Optional[bool] = None
    """输入框是否可输入"""

    btnSize: Optional[Literal['xs', 'sm', 'md', 'lg']] = None
    """按钮大小"""

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """输入框边框模式"""

    placeholder: Optional[str] = None
    """
    - 输入框占位符
    - 默认值：'暂无数据'
    """

    className: Optional[str] = None
    """控件外层 CSS 样式类名"""

    variableClassName: Optional[str] = None
    """变量面板 CSS 样式类名"""

    functionClassName: Optional[str] = None
    """函数面板 CSS 样式类名"""

    mixedMode: Optional[bool] = None
    """混合模式"""