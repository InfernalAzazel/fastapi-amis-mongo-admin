from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *

class AInputGroup(AFormItem):
    """
    Input-Group 输入框组合

    输入框组合选择器 可用于输入框与其他组件进行组合。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-group#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ValidationConfig(BaseModel):
        errorMode: Optional[Literal['full', 'partial']] = None
        """
        - 错误提示风格, full: 整体飘红,partial: 仅错误元素飘红
        - 默认值：'full'
        """

        delimiter: Optional[str] = None
        """
        - 单个子元素多条校验信息的分隔符
        - 默认值：';'
        """

    type: str = "input-group"

    className: Optional[str] = None
    """CSS 类名"""

    body: SerializeAsAny[Optional[list[Union[AFormItem, AmisNode]]]] = None
    """表单项集合"""

    validationConfig: SerializeAsAny[Optional[ValidationConfig]] = None
    """
    - 校验相关配置
    - 版本：2.8.0
    """

