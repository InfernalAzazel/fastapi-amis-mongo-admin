from fastapi_amis_admin.amis.data_input.transfer import ATransfer


class ATabsTransfer(ATransfer):
    """
    TabsTransfer 组合穿梭器

    在穿梭器（Transfer）的基础上扩充了左边的展示形式，
    支持 Tabs 的形式展示。对应的 options 的顶级数据，
    顶层 options 的成员支持 selectMode 配置这个 tab 下面的选项怎么展示。
    title 可以配置 tab 的标题。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/tabs-transfer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "tabs-transfer"