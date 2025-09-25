from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.function.button import AButton
from fastapi_amis_admin.amis.types import *


class ACombo(AFormItem):
    """
    Combo 组合

    用于将多个表单项组合到一起，实现深层结构的数据编辑。

    比如想提交 user.name 这样的数据结构，有两种方法：一种是将表单项的 name 设置为user.name，另一种就是使用 combo。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/combo#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "combo"
    """指定为 combo 组件"""

    formClassName: Optional[str] = None
    """单组表单项的类名"""

    items: SerializeAsAny[Optional[list[AFormItem]]] = None
    """组合展示的表单项"""

    noBorder: Optional[bool] = None
    """
    - 单组表单项是否显示边框
    - 默认值：false
    """

    scaffold: Optional[dict] = None
    """单组表单项初始值"""

    multiple: Optional[bool] = False
    """是否多选"""

    multiLine: Optional[bool] = False
    """默认是横着展示一排，设置以后竖着展示"""

    minLength: Optional[int] = None
    """
    - 最少添加的条数
    - 版本: 2.4.1 版本后支持变量
    """

    maxLength: Optional[int] = None
    """
    - 最多添加的条数
    - 版本: 2.4.1 版本后支持变量
    """

    flat: Optional[bool] = False
    """
    - 是否将结果扁平化(去掉 name),只有当 items 的 length 为 1 且 multiple 为 true 的时候才有效
    - 默认值：false
    """

    joinValues: Optional[bool] = True
    """
    - 默认为 true 当扁平化开启的时候，是否用分隔符的形式发送给后端，否则采用 array 的方式
    - 默认值：true
    """

    delimiter: Optional[str] = None
    """当扁平化开启并且 joinValues 为 true 时，用什么分隔符"""

    addable: Optional[bool] = False
    """
    - 是否可新增
    - 默认值：false
    """

    addattop: Optional[bool] = False
    """
    - 在顶部添加
    - 默认值：false
    """

    removable: Optional[bool] = False
    """
    - 是否可删除
    - 默认值：false
    """

    deleteApi: Optional[API] = None
    """如果配置了，则删除前会发送一个 api，请求成功才完成删除"""

    deleteConfirmText: Optional[str] = None
    """当配置 deleteApi 才生效！删除时用来做用户确认"""

    draggable: Optional[bool] = False
    """
    - 是否可以拖动排序, 需要注意的是当启用拖动排序的时候，会多一个$id 字段
    - 默认值：false
    """

    draggableTip: Optional[str] = None
    """可拖拽的提示文字"""

    subFormMode: Optional[Literal['normal', 'horizontal', 'inline']] = None
    """
    - 子表单模式
    - 默认值：'normal'
    """

    subFormHorizontal: Optional[dict] = None
    """
    - 当 subFormMode 为 horizontal 时有用，用来控制 label 的展示占比
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """
    - 没有成员时显示
    """

    canAccessSuperData: Optional[bool] = False
    """
    - 指定是否可以自动获取上层的数据并映射到表单项上
    - 默认值：false
    """

    conditions: Optional[dict] = None
    """数组的形式包含所有条件的渲染类型，单个数组内的test 为判断条件，数组内的items为符合该条件后渲染的schema"""

    typeSwitchable: Optional[bool] = None
    """
    - 是否可切换条件，配合conditions使用
    - 默认值：false
    """

    strictMode: Optional[bool] = True
    """默认为严格模式，设置为 false 时，当其他表单项更新是，里面的表单项也可以及时获取，否则不会"""

    syncFields: Optional[list[str]] = None
    """配置同步字段。只有 strictMode 为 false 时有效。如果 Combo 层级比较深，底层的获取外层的数据可能不同步。但是给 combo 配置这个属性就能同步下来。输入格式：["os"]"""

    nullable: Optional[bool]  = False
    """
    - 允许为空，如果子表单项里面配置验证器，且又是单条模式。可以允许用户选择清空（不填）
    - 默认值：false
    """

    itemClassName: Optional[str] = None
    """单组 CSS 类"""

    itemsWrapperClassName: Optional[str] = None
    """组合区域 CSS 类"""

    deleteBtn: Optional[Union[str, AButton]] = None
    """
    - 只有当removable为 true 时有效; 如果为string则为按钮的文本；如果为Button则根据配置渲染删除按钮。
    - 默认值：'自定义删除按钮'
    """

    addBtn: Optional[AButton] = None
    """
    - 可新增自定义配置渲染新增按钮，在tabsMode: true下不生效。
    - 默认值：'自定义新增按钮'
    """

    addButtonClassName: Optional[str] = None
    """新增按钮 CSS 类名"""

    addButtonText: Optional[str] = None
    """新增按钮文字"""