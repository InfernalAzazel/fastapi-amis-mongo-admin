from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class Wizard(AmisNode):
    """
    Wizard 向导

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/wizard#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Step(BaseModel):
        title: Optional[str] = None
        """步骤标题"""

        mode: Optional[str] = None
        """展示默认，跟 Form 中的模式一样，选择：normal、horizontal 或者 inline。"""

        horizontal: Optional[Dict[str, Any]] = None
        """当为水平模式时，用来控制左右占比"""

        api: Optional[Dict] = None
        """当前步骤保存接口，可以不配置。"""

        initApi: Optional[Dict] = None
        """当前步骤数据初始化接口。"""

        initFetch: Optional[bool] = None
        """当前步骤数据初始化接口是否初始拉取。"""

        initFetchOn: Optional[str] = None
        """当前步骤数据初始化接口是否初始拉取，用表达式来决定。"""

        body:SerializeAsAny[Optional[List[AFormItem]]] = None
        """当前步骤的表单项集合，请参考 FormItem。"""

        closeDialogOnSubmit: Optional[bool] = None
        """提交的时候是否关闭弹窗。"""

        jumpableOn: Optional[str] = None
        """配置是否可跳转的表达式"""

        actions: SerializeAsAny[Optional[List[SchemaNode]]] = None
        """自定义每一步的操作按钮"""

    type: str = "wizard"

    mode: Optional[str] = None
    """
    - 展示模式，选择：horizontal 或者 vertical
    - 默认值：'horizontal'
    """

    api: Optional[API] = None
    """最后一步保存的接口。"""

    initApi: Optional[API] = None
    """初始化数据接口"""

    initFetch: Optional[bool] = None
    """初始是否拉取数据。"""

    initFetchOn: Optional[Expression] = None
    """初始是否拉取数据，通过表达式来配置"""

    actionPrevLabel: Optional[str] = None
    """
    - 上一步按钮文本
    - 默认值：'上一步'
    """

    actionNextLabel: Optional[str] = None
    """
    - 下一步按钮文本
    - 默认值：'下一步'
    """

    actionNextSaveLabel: Optional[str] = None
    """
    - 保存并下一步按钮文本
    - 默认值：'保存并下一步'
    """

    actionFinishLabel: Optional[str] = None
    """
    - 完成按钮文本
    - 默认值：'完成'
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    actionClassName: Optional[str] = None
    """
    - 按钮 CSS 类名
    - 默认值：'btn-sm btn-default'
    """

    reload: Optional[str] = None
    """操作完后刷新目标对象。"""

    redirect: Optional[Template] = None
    """
    - 操作完后跳转。
    - 默认值：3000
    """

    target: Optional[str] = None
    """可以把数据提交给别的组件而不是自己保存。"""

    steps: Optional[List[Step]] = None
    """数组，配置步骤信息"""

    startStep: Optional[Union[str, int]] = None
    """
    - 起始默认值，从第几步开始。
    - 默认值：'1'
    """