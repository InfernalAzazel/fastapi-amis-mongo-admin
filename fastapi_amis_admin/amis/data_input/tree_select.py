from typing import Optional
from fastapi_amis_admin.amis.data_input.input_tree import AInputTree


class ATreeSelect(AInputTree):
    """
    TreeSelect 树形选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/treeselect#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tree-select"

    hideNodePathLabel: Optional[bool] = None
    """
    - 是否隐藏选择框中已选择节点的路径 label 信息
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 是否可检索
    - 默认值：false
    - 仅在 type 为 tree-select 的时候生效
    """