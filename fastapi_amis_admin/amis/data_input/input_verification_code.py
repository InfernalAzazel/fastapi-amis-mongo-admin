from typing import Optional
from fastapi_amis_admin.amis.data_input.form_item import AFormItem



class AInputVerificationCode(AFormItem):
    """
    InputVerificationCode 验证码输入

    注意 InputVerificationCode, 可通过粘贴完成填充数据。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-verification-code#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    length: Optional[int] = None
    """
    - 验证码的长度
    - 默认值：6
    """

    masked: Optional[bool] = None
    """
    - 是否是密码模式
    - 默认值：false
    """

    separator: Optional[str] = None
    """分隔符，支持表达式"""
