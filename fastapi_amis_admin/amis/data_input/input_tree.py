from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputTree(AFormItem):
    """
    InputTree 树形选择框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-tree#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-tree"

    options: Optional[OptionsNode] = None
    """选项组"""

    source: Optional[Union[str, API]] = None
    """动态选项组"""

    autoComplete: Optional[API] = None
    """自动提示补全"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

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

    iconField: Optional[str] = None
    """
    - 图标值字段
    - 默认值：'icon'
    """

    deferField: Optional[str] = None
    """
    - 懒加载字段
    - 默认值：'defer'
    - 版本：3.6.0
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

    creatable: Optional[bool] = None
    """
    - 新增选项
    - 默认值：false
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

    searchable: Optional[bool] = None
    """
    - 是否可检索
    - 默认值：false
    - 版本：2.8.0前仅tree-select支持
    """

    hideRoot: Optional[bool] = None
    """
    - 是否隐藏根节点
    - 默认值：true
    """

    rootLabel: Optional[str] = None
    """
    - 顶级节点文字
    - 默认值："顶级"
    """

    showIcon: Optional[bool] = None
    """
    - 是否显示图标
    - 默认值：true
    """

    showRadio: Optional[bool] = None
    """
    - 是否显示单选按钮
    - 默认值：false
    """

    showOutline: Optional[bool] = None
    """
    - 是否显示树层级展开线
    - 默认值：false
    """

    initiallyOpen: Optional[bool] = None
    """
    - 默认展开所有层级
    - 默认值：true
    """

    unfoldedLevel: Optional[int] = None
    """
    - 默认展开级数
    - 默认值：1
    """

    autoCheckChildren: Optional[bool] = None
    """
    - 选中父节点时级联选择子节点
    - 默认值：true
    """

    cascade: Optional[bool] = None
    """
    - 子节点可反选
    - 默认值：false
    """

    withChildren: Optional[bool] = None
    """
    - 值包含父子节点值
    - 默认值：false
    """

    onlyChildren: Optional[bool] = None
    """
    - 值只包含子节点值
    - 默认值：false
    """

    onlyLeaf: Optional[bool] = None
    """
    - 只允许选择叶子节点
    - 默认值：false
    """

    rootCreatable: Optional[bool] = None
    """
    - 是否可以创建顶级节点
    - 默认值：false
    """

    rootCreateTip: Optional[str] = None
    """
    - 创建顶级节点的悬浮提示
    - 默认值："添加一级节点"
    """

    minLength: Optional[int] = None
    """最少选中的节点数"""

    maxLength: Optional[int] = None
    """最多选中的节点数"""

    treeContainerClassName: Optional[str] = None
    """树最外层容器类名"""

    enableNodePath: Optional[bool] = None
    """
    - 节点路径模式
    - 默认值：false
    """

    pathSeparator: Optional[str] = None
    """
    - 节点路径的分隔符
    - 默认值：'/'
    """

    highlightTxt: Optional[str] = None
    """标签中需要高亮的字符"""

    itemHeight: Optional[int] = None
    """
    - 每个选项的高度
    - 默认值：32
    """

    virtualThreshold: Optional[int] = None
    """
    - 虚拟渲染的阈值
    - 默认值：100
    """

    menuTpl: Optional[str] = None
    """选项自定义渲染 HTML 片段"""

    enableDefaultIcon: Optional[bool] = None
    """
    - 为选项添加默认的前缀 Icon
    - 默认值：true
    """

    heightAuto: Optional[bool] = None
    """
    - 自动增长高度
    - 默认值：false
    - 版本：3.0.0
    """