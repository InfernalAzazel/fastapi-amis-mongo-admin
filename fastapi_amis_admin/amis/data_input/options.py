from fastapi_amis_admin.amis.types import *


class AOptions(AmisNode):
    """
    Options 选择器表单项

    - 选择器表单项 是指那些（例如下拉选择框）具有选择器特性的表单项

    - 它派生自 表单项，拥有表单项所有的特性

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/options#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    options: Optional[Union[ list[dict], list[str]]] = None
    """选项组，供用户选择"""

    source: Optional[Union[API, Tpl]] = None
    """选项组源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    multiple: Optional[bool] = None
    """
    - 是否支持多选
    - 默认值: false
    """

    labelField: Optional[str] = None
    """
    - 标识选项中哪个字段是label值
    - 默认值: 'label'
    """

    valueField: Optional[str] = None
    """
    - 标识选项中哪个字段是label值
    - 默认值: 'value'
    """

    deferField: Optional[str] = None
    """
    - 标识选项中哪个字段是defer值
    - 默认值: 'defer'
    """

    joinValues: Optional[bool] = None
    """
    - 是否拼接value值
    - 默认值: true
    """

    extractValue: Optional[bool] = None
    """
    - 是否将value值抽取出来组成新的数组，只有在joinValues是false是生效
    - 默认值: false
    """

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度，用于虚拟渲染
    - 默认值: 32
    """

    virtualThreshold: Optional[int] = None
    """
    - 在选项数量超过多少时开启虚拟渲染
    - 默认值: 100
    """

    valuesNoWrap: Optional[bool] = None
    """
    - 默认情况下多选所有选项都会显示，通过这个可以最多显示一行，超出的部分变成
    - 默认值: false
    """