from fastapi_amis_admin.amis.types import *


class AInputExcel(AmisNode):
    """
    InputExcel 解析 Excel

    - 2.10.0 以上版本支持 xls 文件格式，2.9.0 及以下版本只支持 xlsx

    这个组件是通过前端对 Excel 进行解析，将结果作为表单项，使用它有两个好处：

    1.节省后端开发成本，无需再次解析 Excel

    2.可以前端实时预览效果，比如配合 input-table 组件进行二次修改

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-excel#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """
    type: str = 'input-excel'

    allSheets: Optional[bool] = None
    """是否解析所有 sheet"""

    parseMode: Optional[str] = None
    """解析模式"""

    includeEmpty: Optional[bool] = None
    """是否包含空值"""

    plainText: Optional[bool] = None
    """是否解析为纯文本"""

    placeholder: Optional[str] = None
    """
    - 占位文本提示
    - 默认值："拖拽 Excel 到这，或点击上传"
    - 版本：2.8.1	
    """

    autoFill: Optional[dict[str, str]] = None
    """
    - 自动填充
    - 版本：3.5.0
    """