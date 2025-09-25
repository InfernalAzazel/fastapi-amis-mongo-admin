from fastapi_amis_admin.amis.types import *


class APaginationWrapper(AmisNode):
    """
    PaginationWrapper 分页容器

    分页容器组件，可以用来对已有列表数据做分页处理。
    """
    type: str = "pagination-wrapper"
    """指定为 Pagination-Wrapper 渲染器"""

    showPageInput: Optional[bool] = False
    """是否显示快速跳转输入框"""

    maxButtons: Optional[int] = 5
    """最多显示多少个分页按钮"""

    inputName: str = "items"
    """输入字段名"""

    outputName: str = "items"
    """输出字段名"""

    perPage: Optional[int] = None
    """每页显示多条数据"""

    position: Literal["top", "none", "bottom"] = "top"
    """分页显示位置，如果配置为 none 则需要自己在内容区域配置 pagination 组件，否则不显示"""

    body: SerializeAsAny[Optional[SchemaNode]] = None

    """内容区域"""