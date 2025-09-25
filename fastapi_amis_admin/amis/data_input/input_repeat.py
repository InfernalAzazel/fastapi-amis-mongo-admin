from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputRepeat(AFormItem):

    """
    InputRepeat 重复频率选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-repeat#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-repeat"

    options: Optional[str] = None
    """
    - 可用配置 secondly,minutely,hourly,daily,weekdays,weekly,monthly,yearly
    - 默认值：'hourly,daily,weekly,monthly'
    """

    placeholder: Optional[str] = None
    """
    - 当不指定值时的说明
    - 默认值：'不重复'
    """