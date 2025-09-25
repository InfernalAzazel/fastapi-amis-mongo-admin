from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem


class AInputCity(AFormItem):
    """
    InputCity 城市选择器

    城市选择器，方便输入城市，可以理解为自动配置了国内城市选项的 Select，支持到县级别。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-city#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'input-city'
    """指明为 input-city 组件"""

    allowCity: Optional[bool] = None
    """
    - 允许选择城市
    - 默认值：true
    """

    allowDistrict: Optional[bool] = None
    """
    允许选择区域
    - 默认值：true
    """

    searchable: Optional[bool] = None
    """
    是否出搜索框
    - 默认值：false
    """

    extractValue: Optional[bool] = None
    """
    - 如果设置成 false 值格式会变成对象，包含 code、province、city 和 district 文字信息
    - 默认值：true
    """