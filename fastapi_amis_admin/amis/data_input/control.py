from fastapi_amis_admin.amis.types import *


class AControl(AmisNode):
    """
    Control 表单项包裹

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/control
    """
    type: str =  'control'
    """指定 control 渲染器"""

    label: Optional[str] = None
    """标签"""

    description: Optional[str] = None
    """描述"""

    body: Optional[Union[str, dict, list]] = None
    """内容容器"""