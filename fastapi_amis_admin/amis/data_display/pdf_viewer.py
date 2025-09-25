from fastapi_amis_admin.amis.types import *


class APDFViewer(AmisNode):
    """
    PDF Viewer

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/pdf-viewer#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "pdf-viewer"

    src: Optional[str] = None
    """文档地址"""

    width: Optional[int] = None
    """宽度"""

    height: Optional[int] = None
    """高度"""

    background: Optional[str] = None
    """
    - PDF 背景色
    - 默认值：#fff
    """