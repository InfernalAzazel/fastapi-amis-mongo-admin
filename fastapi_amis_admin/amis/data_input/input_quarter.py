from fastapi_amis_admin.amis.data_input.input_date import AInputDate


class AInputQuarter(AInputDate):
    """
    InputQuarter 季度

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-quarter#%E4%BA%8B%E4%BB%B6%E8%A1%A8
    """

    type: str = "input-quarter"
