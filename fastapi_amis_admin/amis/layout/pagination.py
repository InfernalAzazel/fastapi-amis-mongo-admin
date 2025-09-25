from typing import Literal, Union, List, Optional
from fastapi_amis_admin.amis.types import AmisNode



class APagination(AmisNode):
    """
    Pagination 分页组件

    参考：https://baidu.github.io/amis/zh-CN/components/pagination#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = "pagination"
    """	指定为 Pagination 渲染器"""

    mode: Literal["simple", "normal"] = "normal"
    """迷你版本/简易版本 只显示左右箭头，配合 hasNext 使用"""

    layout: Union[str, List[str]] = ["pager"]
    """通过控制 layout 属性的顺序，调整分页结构布局"""

    maxButtons: Union[str, int] = 5
    """最多显示多少个分页按钮，最小为 5"""

    total: Optional[int] = None
    """总条数"""

    activePage: int = 1
    """当前页数"""

    perPage: int = 10
    """	每页显示多条数据"""

    showPerPage: bool = False

    """是否展示 perPage 切换器 layout 和 showPerPage 都可以控制"""
    size: Literal['sm', 'md'] = 'md'

    """组件尺寸，支持md、sm设置，版本: 6.0.0后支持变量"""
    ellipsisPageGap: Union[int, str] = 5
    """多页跳转页数，页数较多出现...时点击省略号时每次前进/后退的页数，默认为5，版本: 6.0.0后支持变量"""

    perPageAvailable: List[int] = [10, 20, 50, 100]
    """指定每页可以显示多少条"""

    showPageInput: bool = False
    """是否显示快速跳转输入框 layout 和 showPageInput 都可以控制"""

    disabled: bool = False
    """	是否禁用"""

    onPageChange: Optional[str] = None
    """分页改变触发，(page: number, perPage: number) => void;"""
