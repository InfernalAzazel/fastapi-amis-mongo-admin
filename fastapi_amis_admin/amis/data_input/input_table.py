from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputTable(AFormItem):
    """
    InputTable 表格

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-table#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-table"

    addable: Optional[bool] = None
    """
    - 是否可增加一行
    - 默认值：false
    """

    copyable: Optional[bool] = None
    """
    - 是否可复制一行
    - 默认值：false
    """

    copyData: Optional[Dict[str, Any]] = None
    """控制复制时的数据映射，不配置时复制整行数据"""

    childrenAddable: Optional[bool] = None
    """
    - 是否可增加子级节点
    - 默认值：false
    """

    editable: Optional[bool] = None
    """
    - 是否可编辑
    - 默认值：false
    """

    removable: Optional[bool] = None
    """
    - 是否可删除
    - 默认值：false
    """

    showTableAddBtn: Optional[bool] = None
    """
    - 是否显示表格操作栏添加按钮
    - 默认值：true
    """

    showFooterAddBtn: Optional[bool] = None
    """
    - 是否显示表格下方添加按钮
    - 默认值：true
    """

    addApi: Optional[API] = None
    """新增时提交的 API"""

    footerAddBtn: SerializeAsAny[Optional[SchemaNode]] = None
    """底部新增按钮配置"""

    updateApi: Optional[API] = None
    """修改时提交的 API"""

    deleteApi: Optional[API] = None
    """删除时提交的 API"""

    addBtnLabel: Optional[str] = None
    """增加按钮名称"""

    addBtnIcon: Optional[str] = None
    """
    - 增加按钮图标
    - 默认值："plus"
    """

    subAddBtnLabel: Optional[str] = None
    """子级增加按钮名称"""

    subAddBtnIcon: Optional[str] = None
    """
    - 子级增加按钮图标
    - 默认值："sub-plus"
    """

    copyBtnLabel: Optional[str] = None
    """复制按钮文字"""

    copyBtnIcon: Optional[str] = None
    """
    - 复制按钮图标
    - 默认值："copy"
    """

    editBtnLabel: Optional[str] = None
    """
    - 编辑按钮名称
    - 默认值：""
    """

    editBtnIcon: Optional[str] = None
    """
    - 编辑按钮图标
    - 默认值："pencil"
    """

    deleteBtnLabel: Optional[str] = None
    """
    - 删除按钮名称
    - 默认值：""
    """

    deleteBtnIcon: Optional[str] = None
    """
    - 删除按钮图标
    - 默认值："minus"
    """

    confirmBtnLabel: Optional[str] = None
    """
    - 确认编辑按钮名称
    - 默认值：""
    """

    confirmBtnIcon: Optional[str] = None
    """
    - 确认编辑按钮图标
    - 默认值："check"
    """

    cancelBtnLabel: Optional[str] = None
    """
    - 取消编辑按钮名称
    - 默认值：""
    """

    cancelBtnIcon: Optional[str] = None
    """
    - 取消编辑按钮图标
    - 默认值："times"
    """

    needConfirm: Optional[bool] = None
    """
    - 是否需要确认操作
    - 默认值：true
    """

    canAccessSuperData: Optional[bool] = None
    """
    - 是否可以访问父级数据
    - 默认值：false
    """

    strictMode: Optional[bool] = None
    """
    - 性能优化选项
    - 默认值：true
    """

    minLength: Optional[Union[int, str]] = None
    """
    - 最小行数
    - 默认值：0
    """

    maxLength: Optional[Union[int, str]] = None
    """
    - 最大行数
    - 默认值：Infinity
    """

    perPage: Optional[int] = None
    """每页展示几行数据，如果不配置则不会显示分页器"""

    columns: Optional[List[Dict[str, Any]]] = None
    """列信息"""