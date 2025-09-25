from typing import Optional
from fastapi_amis_admin.amis.data_input.input_text import AInputText


class AInputPassword(AInputText):
    """
    InputPassword 密码输入框

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-password#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-password"

    revealPassword: Optional[bool] = None
    """
    - 是否展示密码显/隐按钮
    - 默认值：true
    """
