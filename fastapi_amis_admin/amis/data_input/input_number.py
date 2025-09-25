from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputNumber(AFormItem):
    """
    InputNumber 数字输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-number#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-number"

    min: Optional[Union[int, Template]] = None
    """最小值"""

    max: Optional[Union[int, Template]] = None
    """最大值"""

    step: Optional[int] = None
    """步长"""

    precision: Optional[int] = None
    """精度，即小数点后几位，支持 0 和正整数"""

    showSteps: Optional[bool] = None
    """
    - 是否显示上下点击按钮
    - 默认值：true
    """

    readOnly: Optional[bool] = None
    """
    - 只读
    - 默认值：false
    """

    prefix: Optional[str] = None
    """前缀"""

    suffix: Optional[str] = None
    """后缀"""

    unitOptions: Optional[List[str]] = None
    """单位选项"""

    kilobitSeparator: Optional[bool] = None
    """
    - 千分分隔
    - 默认值：false
    """

    keyboard: Optional[bool] = None
    """
    - 键盘事件（方向上下）
    - 默认值：true
    """

    big: Optional[bool] = None
    """
    - 是否使用大数
    - 默认值：false
    """

    displayMode: Optional[Literal['base', 'enhance']] = None
    """
    - 样式类型
    - 默认值：'base'
    """

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """
    - 边框模式，全边框，还是半边框，或者没边框
    - 默认值：'full'
    """

    resetValue: Optional[Union[int, str]] = None
    """
    - 清空输入内容时，组件值将设置为 resetValue
    - 默认值：""
    """

    clearValueOnEmpty: Optional[bool] = None
    """
    - 内容为空时从数据域中删除该表单项对应的值
    - 默认值：false
    """