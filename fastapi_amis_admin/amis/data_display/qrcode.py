from fastapi_amis_admin.amis.types import *


class AQRCode(AmisNode):
    """
    QRCode 二维码

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/qrcode#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class ImageSettings(AmisNode):
        src: Optional[str] = None
        """图片链接地址"""

        width: Optional[int] = None
        """图片宽度，默认为 codeSize 的 10%"""

        height: Optional[int] = None
        """图片高度，默认为 codeSize 的 10%"""

        x: Optional[int] = None
        """图片水平方向偏移量，默认水平居中"""

        y: Optional[int] = None
        """图片垂直方向偏移量，默认垂直居中"""

        excavate: Optional[bool] = None
        """
        - 图片是否挖孔嵌入
        - 默认值：false
        """

    type: str = 'qr-code'

    className: Optional[str] = None
    """外层 Dom 的类名"""

    qrcodeClassName: Optional[str] = None
    """二维码的类名"""

    codeSize: Optional[int] = None
    """
    二维码的宽高大小
    - 默认值：128
    """

    backgroundColor: Optional[str] = None
    """
    二维码背景色
    - 默认值：'#fff'
    """

    foregroundColor: Optional[str] = None
    """
    二维码前景色
    - 默认值：'#000'
    """

    level: Optional[str] = None
    """
    - 二维码复杂级别
    - 默认值：'L'
    """

    value: Optional[Template] = None
    """
    - 扫描二维码后显示的文本，如果要显示某个页面请输入完整 url（"http://..."或"https://..."开头），支持使用模板
    - 默认值：'https://www.baidu.com'
    """

    imageSettings: Optional[ImageSettings] = None
    """QRCode 图片配置"""