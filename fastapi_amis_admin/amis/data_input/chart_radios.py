from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AChartRadios(AFormItem):
    """
    ChartRadios 图表单选框

    图表点选功能，用来做多个图表联动

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/chart-radios#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "chained-radios"

    options: Optional[OptionsNode] = None
    """选项组"""

    config: Optional[Dict[str, Any]] = None
    """echart 图表配置"""

    showTooltipOnHighlight: Optional[bool] = None
    """
    - 高亮的时候是否显示 tooltip
    - 默认值：false
    """

    chartValueField: Optional[str] = None
    """
    - 图表数值字段名
    - 默认值："value"
    """
