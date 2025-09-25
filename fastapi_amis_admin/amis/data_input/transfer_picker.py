from typing import Optional, Literal
from fastapi_amis_admin.amis.data_input.transfer import ATransfer


class ATransferPicker(ATransfer):
    """
    TransferPicker 穿梭选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/transfer-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "transfer-picker"

    borderMode: Optional[Literal['full', 'half', 'none']] = None
    """边框模式"""

    pickerSize: Optional[Literal['xs','sm', 'md', 'lg', 'xl', 'full']] = None
    """弹窗大小"""