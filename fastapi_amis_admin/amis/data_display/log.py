from fastapi_amis_admin.amis.types import *


class Log(AmisNode):
    """
    source 支持高级配置

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/log#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "log"

    height: Optional[int] = None
    """
    - 展示区域高度
    - 默认值：500
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    autoScroll: Optional[bool] = None
    """
    - 是否自动滚动
    - 默认值：true
    """

    disableColor: Optional[bool] = None
    """
    - 是否禁用 ansi 颜色支持
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """加载中的文字"""

    encoding: Optional[str] = None
    """
    - 返回内容的字符编码
    - 默认值：utf-8
    """

    source: Optional[API] = None
    """接口"""

    credentials: Optional[str] = None
    """
    - fetch 的 credentials 设置
    - 默认值：'include'
    """

    rowHeight: Optional[int] = None
    """设置每行高度，将会开启虚拟渲染"""

    maxLength: Optional[int] = None
    """最大显示行数"""

    operation: Optional[List[str]] = None
    """
    - 可选日志操作
    - 默认值：['stop','restart','clear','showLineNumber','filter']
    """