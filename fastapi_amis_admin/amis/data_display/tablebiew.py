from fastapi_amis_admin.amis.types import *

class ATableView(AmisNode):
    """
    Table View 表格展现

    - 1.2.0 及以上版本才有此功能
    - 数据源要求不同
        - table 的数据源需要是多行的数据，最典型的就是来自某个数据库的表
        - table view 的数据源可以来自各种固定的数据，比如单元格的某一列是来自某个变量
    - 功能不同
        - table 只能用来做数据表的展现
        - table view 除了展现复杂的报表，还能用来进行布局
    - 合并单元格方式不同
        - table 的合并单元格需要依赖数据
        - table view 的合并单元格是手动指定的，因此可以支持不规则的数据格式

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E8%A1%A8%E6%A0%BC%E8%AE%BE%E7%BD%AE%E9%A1%B9
    """

    type: str = "table-view"
    """指定组件类型"""

    width: Optional[Union[int, str]] = None
    """
      - 宽度
      - 默认值：'100%'
    """

    padding: Optional[Union[int, str]] = None
    """
      - 单元格默认内间距
      - 默认值：'var(--TableCell-paddingY) var(--TableCell-paddingX)'
    """

    border: Optional[bool] = None
    """
      - 是否显示边框
      - 默认值：true
    """

    borderColor: Optional[str] = None
    """
      - 边框颜色
      - 默认值：'var(--borderColor)'
    """

    trs: SerializeAsAny[Optional['ATableViewRow']] = None
    """参考的行设置 """

    cols: SerializeAsAny[Optional['ATableViewCols']] = None

    caption: Optional[str] = None
    """
    - 标题设置
    - 可以通过 caption 来添加段标题文本，并通过 captionSide 来控制显示在底部还是顶部。
    """

    captionSide: Optional[Literal['top', 'bottom']] = None
    """显示在底部还是顶部"""


class ATableViewRow(AmisNode):
    """
    行设置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E8%A1%8C%E8%AE%BE%E7%BD%AE
    """
    height: Optional[Union[int, str]] = None
    """行高度"""

    background: Optional[str] = None
    """行背景色"""

    tds: SerializeAsAny[Optional['ATableViewTds']] = None
    """参考单元格设置"""


class ATableViewTds(AmisNode):
    """
    单元格设置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E5%8D%95%E5%85%83%E6%A0%BC%E8%AE%BE%E7%BD%AE
    """

    background: Optional[str] = None
    """单元格背景色"""

    color: Optional[str] = None
    """单元格文字颜色"""

    bold: Optional[bool] = None
    """
    - 单元格文字是否加粗
    - 默认值：false
    """

    width: Optional[Union[int, str]] = None
    """单元格宽度，只需要设置第一行"""

    padding: Optional[Union[int, str]] = None
    """
    - 单元格内间距
    - 默认值：'集成表格的设置'
    """

    align: Optional[Literal['left', 'center', 'right']] = None
    """
    - 单元格内的水平对齐
    - 默认值：'left'
    """

    valign: Optional[Literal['top', 'middle', 'bottom', 'baseline']] = None
    """
    - 单元格内的垂直对齐
    - 默认值：'middle'
    """

    colspan: Optional[int] = None
    """单元格水平跨几行"""

    rowspan: Optional[int] = None
    """单元格垂直跨几列"""

    body: SerializeAsAny[Optional[Union[AmisNode, list[AmisNode]]]] = None
    """其它 amis 设置"""


class ATableViewCols(AmisNode):
    """
    列设置项

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/table-view#%E5%88%97%E8%AE%BE%E7%BD%AE%E9%A1%B9
    """
    span: Optional[int] = None
    """这是个跨几列的设置项"""

    style: Optional[dict] = None
    """列样式"""