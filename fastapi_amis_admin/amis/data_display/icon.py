from fastapi_amis_admin.amis.types import *


class AIcon(AmisNode):
    """
    Icon 图标

    在 React 项目中使用 Icon 需要引入 @fortawesome/fontawesome-free，
    然后在代码中 import '@fortawesome/fontawesome-free/css/all.css'，
    还有相关的 webpack 配置，具体请参考 amis-react-starter 里的配置。

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/icon#%E4%BA%8B%E4%BB%B6%E8%A1%A8
    """

    type: str = "icon"
    """指定组件类型"""

    className: Optional[str] = None
    """外层 CSS 类名"""

    icon: Optional[Template] = None
    """icon 名称，支持 fontawesome v4 或 通过 registerIcon 注册的 icon、或使用 url"""

    vendor: Optional[str] = None
    """icon 类型，默认为fa, 表示 fontawesome v4。也支持 iconfont, 如果是 fontawesome v5 以上版本或者其他框架可以设置为空字符串"""
