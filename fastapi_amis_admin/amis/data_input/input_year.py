from fastapi_amis_admin.amis.data_input.input_date import AInputDate


class AInputYear(AInputDate):
    """
    Year 年份选择

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-year#%E5%8A%A8%E4%BD%9C%E8%A1%A8
    """

    type: str = "input-year"