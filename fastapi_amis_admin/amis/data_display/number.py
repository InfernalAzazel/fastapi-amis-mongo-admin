from fastapi_amis_admin.amis.types import *


class ANumber(AmisNode):
    """
    Number 数字展示

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/number#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'number'
    """如果在 Table、Card 和 List 中，为"number"；在 Form 中用作静态展示，为"static-number" 或者 input-number 配置 static 属性"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """数值"""

    name: Optional[str] = None
    """在其他组件中，用作变量映射"""

    placeholder: Optional[str] = None
    """占位内容"""

    kilobitSeparator: Optional[bool] = None
    """
    - 是否千分位展示
    - 默认值：true
    """

    precision: Optional[int] = None
    """用来控制小数点位数"""

    percent: Optional[Union[bool, int]] = None
    """是否用百分比展示，如果是数字，还可以控制百分比小数点位数"""

    prefix: Optional[str] = None
    """前缀"""

    affix: Optional[str] = None
    """后缀"""