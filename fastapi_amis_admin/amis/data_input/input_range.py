from typing import Optional, Union, List, Callable, Any, Literal, Dict
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputRange(AFormItem):
    """
    InputRange 滑块

    可以用于选择单个数值或数值范围

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-range#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-range"

    className: Optional[str] = None
    """css 类名"""

    value: Optional[Union[int, str, Dict[str, float], List[int]]] = None
    """当前值"""

    min: Optional[Union[int, str]] = None
    """
    - 最小值，支持变量
    - 默认值：0
    """

    max: Optional[Union[int, str]] = None
    """
    - 最大值，支持变量
    - 默认值：100
    """

    disabled: Optional[bool] = None
    """
    - 是否禁用
    - 默认值：false
    """

    step: Optional[Union[int, str]] = None
    """
    - 步长，支持变量
    - 默认值：1
    """

    showSteps: Optional[bool] = None
    """
    - 是否显示步长
    - 默认值：false
    """

    parts: Optional[Union[int, List[int]]] = None
    """
    - 分割的块数
    - 默认值：1
    """

    marks: Optional[Dict[Union[int, str], Union[str, int, Dict[str, Any]]]] = None
    """刻度标记，支持自定义样式"""

    tooltipVisible: Optional[bool] = None
    """
    - 是否显示滑块标签
    - 默认值：false
    """

    tooltipPlacement: Optional[Literal['top', 'right', 'bottom', 'left']] = None
    """
    - 滑块标签的位置
    - 默认值：'top'
    """

    tipFormatter: Optional[Callable[[Any], Any]] = None
    """控制滑块标签显隐函数"""

    multiple: Optional[bool] = None
    """
    - 支持选择范围
    - 默认值：false
    """

    joinValues: Optional[bool] = None
    """
    - 默认为 true，选择的 value 会通过 delimiter 连接起来
    - 默认值：true
    """

    delimiter: Optional[str] = None
    """
    - 分隔符
    - 默认值：','
    """

    unit: Optional[str] = None
    """单位"""

    clearable: Optional[bool] = None
    """
    - 是否可清除
    - 默认值：false
    """

    showInput: Optional[bool] = None
    """
    - 是否显示输入框
    - 默认值：false
    """

    showInputUnit: Optional[bool] = None
    """
    - 是否显示输入框单位
    - 默认值：false
    """

    onChange: Optional[Callable[[Any], None]] = None
    """当组件的值发生改变时，会触发 onChange 事件"""

    onAfterChange: Optional[Callable[[Any], None]] = None
    """与 onmouseup 触发时机一致，把当前值作为参数传入"""