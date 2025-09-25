from fastapi_amis_admin.amis.data_input.transfer import ATransfer


class ATabsTransferPicker(ATransfer):
    """
    TabsTransferPicker 穿梭选择器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/tabs-transfer-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tabs-transfer-picker"