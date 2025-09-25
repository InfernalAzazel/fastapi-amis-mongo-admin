from fastapi_amis_admin.amis.types import *


class AFormula(AmisNode):
    """
    Formula 公式

    可以设置公式，将公式结果设置到指定表单项上。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/formula#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "formula"

    name: Optional[str] = None
    "需要应用的表单项name值，公式结果将作用到此处指定的变量中去"

    formula: Optional[Expression] = None
    """应用的公式"""

    condition: Optional[Expression] = None
    """公式作用条件"""

    initSet: Optional[bool] = None
    """
    - 初始化时是否设置
    - 默认值：true
    """

    autoSet: Optional[bool] = None
    """
    - 观察公式结果，如果计算结果有变化，则自动应用到变量上
    - 默认值：true
    """

    id: Optional[bool] = None
    """定义个名字，当某个按钮的目标指定为此值后，会触发一次公式应用。这个机制可以在 autoSet 为 false 时用来手动触发"""