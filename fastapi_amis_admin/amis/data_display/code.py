from fastapi_amis_admin.amis.types import *


class ACode(AmisNode):
    """
    Code 代码高亮

    使用代码高亮的方式来显示一段代码

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/code#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "code"
    """指定为 code 渲染器"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    value: Optional[str] = None
    """显示的颜色值"""

    name: Optional[str] = None
    """在其他组件中，时，用作变量映射"""

    language: Optional[str] = None
    """
    - 所使用的高亮语言
    - 默认值：plaintext
    """

    tabSize: Optional[int] = None
    """
    - 默认 tab 大小
    - 默认值：4
    """

    editorTheme: Optional[str] = None
    """
    - 主题，还有 'vs-dark'
    - 默认值：'vs'
    """

    wordWrap: Optional[bool] = None
    """
    - 是否折行
    - 默认值：true
    """

    maxHeight: Optional[Union[str, int]] = None
    """最大高度"""