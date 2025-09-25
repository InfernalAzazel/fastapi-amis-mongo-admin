from fastapi_amis_admin.amis.types import *



class AGrid(AmisNode):
    """
    Grid 水平分栏

    参考： https://baidu.github.io/amis/zh-CN/components/grid#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Column(AmisNode):
        """列配置"""

        xs: Optional[int] = None
        """宽度占比： 1 - 12"""

        ClassName: Optional[str] = None
        """列类名"""

        sm: Optional[int] = None
        """宽度占比： 1 - 12"""

        md: Optional[int] = None
        """宽度占比： 1 - 12"""

        lg: Optional[int] = None
        """宽度占比： 1 - 12"""

        valign: Optional[str] = None
        """当前列内容的垂直对齐，选填：'top'|'middle'|'bottom'|'between"""

        body: SerializeAsAny[Optional[List[SchemaNode]]] = None

    type: str = "grid"
    """指定为 Grid 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    gap: Optional[str] = None

    """水平间距，选填: 'xs' | 'sm' | 'base' | 'none' | 'md' | 'lg'"""
    valign: Optional[str] = None

    """垂直对齐方式，选填: 'top' | 'middle' | 'bottom' | 'between'"""

    align: Optional[str] = None
    """水平对齐方式，选填: 'left' | 'right' | 'between' | 'center'"""

    columns: SerializeAsAny[Optional[List[SchemaNode]]] = None
    """列集合"""
