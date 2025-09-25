from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AChainedSelect(AFormItem):
    """
    Chained-Select 链式下拉框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/chain-select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "chained-select"
    """指定为 chained-select 组件"""

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[Union[str, API]] = None
    """自动选中"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：','
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