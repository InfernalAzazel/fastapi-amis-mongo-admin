from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AMatrixCheckboxes(AFormItem):
    """
    MatrixCheckboxes 矩阵

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/form/matrix-checkboxes#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class RowItem(AmisNode):
        label: str

    class ColumnItem(AmisNode):
        label: str

    type: str = "matrix-checkboxes"

    columns: SerializeAsAny[Optional[List[ColumnItem]]]
    """列信息，数组中 label 字段是必须给出的"""

    rows: SerializeAsAny[Optional[List[RowItem]]] = None
    """行信息，数组中 label 字段是必须给出的"""

    rowLabel: Optional[str] = None
    """行标题说明"""

    source: Optional[API] = None
    """API 地址，如果选项组不固定，可以通过配置 source 动态拉取"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：true
    """

    singleSelectMode: Optional[Literal['cell', 'row', 'column']] = None
    """
    - 设置单选模式，multiple为false时有效
    - 默认值：'column'
    """

    textAlign: Optional[str] = None
    """
    - 当开启多选+全选时
    - 默认值：'center'
    """

    yCheckAll: Optional[bool] = None
    """
    - 列上的全选
    - 默认值：false
    """

    xCheckAll: Optional[bool] = None
    """
    - 行上的全选
    - 默认值：false
    """
