from fastapi_amis_admin.amis.types import *


class ASteps(AmisNode):
    """
    Steps 步骤条

    步骤条组件

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/steps#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """


    class Step(AmisNode):
        title: SerializeAsAny[Optional[SchemaNode]] = None
        """标题"""

        subTitle: SerializeAsAny[Optional[SchemaNode]] = None
        """子标题"""

        description: SerializeAsAny[Optional[SchemaNode]] = None
        """详细描述"""

        icon: Optional[str] = None
        """icon 名，支持 fontawesome v4 或使用 url"""

        value: Optional[str] = None
        """步骤值"""

        className: Optional[str] = None
        """自定义 CSS 类名称"""

    type: str = "steps"

    steps: Optional[List[Step]] = None
    """
    - 数组，配置步骤信息
    - 默认值：[]
    """

    source: Optional[API] = None
    """选项组源，可通过数据映射获取当前数据域变量、或者配置 API 对象"""

    name: Optional[str] = None
    """关联上下文变量"""

    value: Optional[Union[str, int]] = None
    """设置默认值，注意不支持表达式"""

    status: Optional[Union[str, Dict[str, str]]] = None
    """状态"""

    className: Optional[str] = None
    """自定义类名"""

    mode: Optional[Literal['horizontal', 'vertical', 'simple']] = None
    """
    - 指定步骤条模式
    - 默认值：'horizontal'
    """

    labelPlacement: Optional[Literal['horizontal', 'vertical']] = None
    """
    - 指定标签放置位置
    - 默认值：'horizontal'
    """

    progressDot: Optional[bool] = None
    """
    - 点状步骤条
    - 默认值：false
    """