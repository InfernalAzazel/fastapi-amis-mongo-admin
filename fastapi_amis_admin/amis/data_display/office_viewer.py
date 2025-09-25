from fastapi_amis_admin.amis.types import *


class AOfficeViewer(AmisNode):
    """
    Office Viewer

    - 参考：
     - https://aisuda.bce.baidu.com/amis/zh-CN/components/office-viewer#%E5%B1%9E%E6%80%A7%E8%A1%A8
     - https://aisuda.bce.baidu.com/amis/zh-CN/components/office-viewer-excel#%E9%85%8D%E7%BD%AE%E9%A1%B9
    """

    type: str = "office-viewer"

    classPrefix: Optional[str] = None
    """
    - 渲染的 class 类前缀
    - 默认值：'docx-viewer'
    """

    ignoreWidth: Optional[bool] = None
    """
    - 忽略文档里的宽度设置，用于更好嵌入到页面里，但会减低还原度
    - 默认值：false
    """

    padding: Optional[str] = None
    """设置页面间距，忽略文档中的设置"""

    bulletUseFont: Optional[bool] = None
    """
    - 列表使用字体渲染
    - 默认值：true
    """

    fontMapping: Optional[Dict[str, str]] = None
    """字体映射，是个键值对，用于替换文档中的字体"""

    forceLineHeight: Optional[str] = None
    """设置段落行高，忽略文档中的设置"""

    enableVar: Optional[bool] = None
    """
    - 是否开启变量替换功能
    - 默认值：true
    """

    printOptions: Optional[Dict[str, Any]] = None
    """针对打印的特殊设置，可以覆盖其它所有设置项"""

    src: Optional[API] = None  # Document address
    """文件地址"""

    showFormulaBar: Optional[bool] = None
    """
    - 是否显示公式栏
    - 默认值：true
    """

    showSheetTabBar: Optional[bool] = None
    """
    - 是否显示底部 sheet 切换
    - 默认值：true
    """

    fontURL: Optional[Dict[str, str]] = None
    """字体地址，参考下面的说明"""