from typing import Optional, Union, Dict, Literal
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputRating(AFormItem):
    """
    InputRating 评分

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-rating#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-rating"

    value: Optional[float] = None
    """当前值"""

    half: Optional[bool] = None
    """
    - 是否使用半星选择
    - 默认值：false
    """

    count: Optional[int] = None
    """
    - 总星数
    - 默认值：5
    """

    readOnly: Optional[bool] = None
    """
    - 只读
    - 默认值：false
    """

    allowClear: Optional[bool] = None
    """
    - 是否允许再次点击后清除
    - 默认值：true
    """

    colors: Optional[Union[str, Dict[str, str]]] = None
    """
    - 星星被选中的颜色
    - 默认值：{'2': '#abadb1', '3': '#787b81', '5': '#ffa900'}
    """

    inactiveColor: Optional[str] = None
    """
    - 未被选中的星星的颜色
    - 默认值：'#e7e7e8'
    """

    texts: Optional[Dict[str, str]] = None
    """星星被选中时的提示文字"""

    textPosition: Optional[Literal['right', 'left']] = None
    """
    - 文字的位置
    - 默认值：right
    """

    char: Optional[str] = None
    """
    - 自定义字符
    - 默认值：★
    """

    className: Optional[str] = None
    """自定义样式类名"""

    charClassName: Optional[str] = None
    """自定义字符类名"""

    textClassName: Optional[str] = None
    """自定义文字类名"""