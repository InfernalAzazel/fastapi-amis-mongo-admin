from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ASelect(AFormItem):
    """
    Select 选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/select#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "select"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[API] = None
    """动态选项组"""

    autoComplete: Optional[API] = None
    """自动提示补全"""

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：'false'
    """

    labelField: Optional[str] = None
    """
    - 选项标签字段
    - 默认值：'label'
    """

    valueField: Optional[str] = None
    """
    - 选项值字段
    - 默认值：'value'
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    checkAll: Optional[bool] = None
    """
    - 是否支持全选
    - 默认值：false
    """

    checkAllLabel: Optional[str] = None
    """
    - 全选的文字
    - 默认值：'全选'
    """

    checkAllBySearch: Optional[bool] = None
    """
    - 有检索时只全选检索命中的项
    - 默认值：true
    """

    defaultCheckAll: Optional[bool] = None
    """
    - 默认是否全选
    - 默认值：false
    """

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 多选
    - 默认值：false
    """

    searchable: Optional[bool] = None
    """
    - 检索
    - 默认值：false
    """

    filterOption: Optional[str] = None
    """控制选项过滤的函数"""

    createBtnLabel: Optional[str] = None
    """
    - 新增选项按钮标签
    - 默认值：'新增选项'
    """

    addControls: SerializeAsAny[Optional[List[AFormItem]]] = None
    """自定义新增表单项"""

    addApi: Optional[API] = None
    """配置新增选项接口"""

    editable: Optional[bool] = None
    """
    - 编辑选项
    - 默认值：false
    """

    editControls: SerializeAsAny[Optional[List[AFormItem]]] = None
    """自定义编辑表单项"""

    editApi: Optional[API] = None
    """配置编辑选项接口"""

    removable: Optional[bool] = None
    """
    - 删除选项
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """配置删除选项接口"""

    autoFill: Optional[Dict[str, Any]] = None
    """自动填充"""

    menuTpl: Optional[str] = None
    """支持配置自定义菜单"""

    clearable: Optional[bool] = None
    """是否展示清空图标"""

    hideSelected: Optional[bool] = None
    """
    - 隐藏已选选项
    - 默认值：false
    """

    mobileClassName: Optional[str] = None
    """移动端浮层类名"""

    selectMode: Optional[str] = None
    """选择模式"""

    searchResultMode: Optional[str] = None
    """搜索结果展示形式"""

    columns: Optional[List[Dict[str, Any]]] = None
    """当展示形式为 table 时配置展示哪些列"""

    leftOptions: Optional[List[Dict[str, Any]]] = None
    """当展示形式为 associated 时配置左边的选项集"""

    leftMode: Optional[str] = None
    """当展示形式为 associated 时配置左边的选择形式"""

    rightMode: Optional[str] = None
    """当展示形式为 associated 时配置右边的选择形式"""

    maxTagCount: Optional[int] = None
    """标签的最大展示数量"""

    overflowTagPopover: Optional[Dict[str, Any]] = None
    """
    - 收纳浮层的配置属性
    - 默认值: {"placement": "top", "trigger": "hover", "showArrow": false, "offset": [0, -10]}
    """

    optionClassName: Optional[str] = None
    """选项 CSS 类名"""

    popOverContainerSelector: Optional[str] = None
    """弹层挂载位置选择器"""

    overlay: Optional[Dict[str, Any]] = None
    """
    - 弹层宽度与对齐方式
    - 类型: { width: string | number, align: "left" | "center" | "right" }
    """

    showInvalidMatch: Optional[bool] = None
    """
    - 选项值与选项组不匹配时选项值是否飘红
    - 默认值：false
    """