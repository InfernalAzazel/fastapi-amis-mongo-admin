from fastapi_amis_admin.amis.types import *


class AProperty(AmisNode):
    """
    Property 属性表

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/property#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Item(AmisNode):
        label: Optional[Template] = None
        """属性名"""

        content: Optional[Template] = None
        """属性值"""

        span: Optional[int] = None
        """属性值跨几列"""

        visibleOn: Optional[Expression] = None
        """显示表达式"""

        hiddenOn: Optional[Expression] = None
        """隐藏表达式"""

    type: str = "property"

    className: Optional[str] = None
    """外层 dom 的类名"""

    style: Optional[Dict[str, Any]] = None
    """外层 dom 的样式"""

    labelStyle: Optional[Dict[str, Any]] = None
    """属性名的样式"""

    contentStyle: Optional[Dict[str, Any]] = None
    """属性值的样式"""

    column: Optional[int] = None
    """
    - 每行几列
    - 默认值：3
    """

    mode: Optional[str] = None
    """
    - 显示模式
    - 可选：'table', 'simple'
    - 默认值：'table'
    """

    separator: Optional[str] = None
    """
    - 'simple' 模式下属性名和值之间的分隔符
    - 默认值：','
    """

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """数据源"""

    items: SerializeAsAny[Optional[List[Item]]] = None
    """配置单条信息"""