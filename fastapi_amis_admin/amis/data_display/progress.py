from fastapi_amis_admin.amis.types import *


class AProgress(AmisNode):
    """
    Progress 进度条

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/progress#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal["progress", 'static-progress'] = 'progress'

    mode: Optional[Literal['line', 'circle', 'dashboard']] = None
    """
    - 进度「条」的类型
    - 可选：line, circle, dashboard
    - 默认值：line
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """进度值"""

    placeholder: Optional[str] = None
    """占位文本"""

    showLabel: Optional[bool] = None
    """
    - 是否展示进度文本
    - 默认值：true
    """

    stripe: Optional[bool] = None
    """
    - 背景是否显示条纹
    - 默认值：false
    """

    animate: Optional[bool] = None
    """
    - type 为 line，可支持动画
    - 默认值：false
    """

    map: Optional[Union[str, List[Union[str, Dict[str, Union[int, str]]]]]] = None
    """
    - 进度颜色映射
    - 默认值：['bg-danger', 'bg-warning', 'bg-info', 'bg-success', 'bg-success']
    """

    threshold: Optional[Union[Dict[str, str], List[Dict[str, str]]]] = None
    """阈值（刻度）"""

    showThresholdText: Optional[bool] = None
    """
    - 是否显示阈值（刻度）数值
    - 默认值：false
    """

    valueTpl: Optional[str] = None
    """
    - 自定义格式化内容
    - 默认值：${value}%
    """

    strokeWidth: Optional[int] = None
    """
    - 进度条线宽度
    - 默认值：line 类型为10，circle、dashboard 类型为6
    """

    gapDegree: Optional[int] = None
    """
    - 仪表盘缺角角度
    - 可取值 0 ~ 295
    - 默认值：75
    """

    gapPosition: Optional[str] = None
    """
    - 仪表盘进度条缺口位置
    - 可选：top, bottom, left, right
    - 默认值：bottom
    """