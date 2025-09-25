from fastapi_amis_admin.amis.types import *


class Avatar(AmisNode):
    """
    Avatar 头像

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/avatar#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "avatar"

    className: Optional[str] = None
    """外层 dom 的类名"""

    style: Optional[Dict] = None
    """外层 dom 的样式"""

    fit: Optional[str] = None
    """
    - 具体细节可以参考 MDN 文档
    - 默认值：'cover'
    """

    src: Optional[str] = None
    """图片地址"""

    defaultAvatar: Optional[str] = None
    """占位图"""

    text: Optional[str] = None
    """文字"""

    icon: Optional[str] = None
    """
    - 图标
    - 默认值：'fa fa-user'
    """

    shape: Optional[str] = None
    """
    - 形状，有三种 'circle'（圆形）、'square'（正方形）、'rounded'（圆角）
    - 默认值：'circle'
    """

    size: Optional[Union[int, str]] = None
    """
    - 'default' | 'normal' | 'small' 三种字符串类型代表不同大小（分别是 48、40、32）
    - 也可以直接数字表示
    - 默认值：'default'
    """

    gap: Optional[int] = None
    """
    - 控制字符类型距离左右两侧边界单位像素
    - 默认值：4
    """

    alt: Optional[str] = None
    """图像无法显示时的替代文本"""

    draggable: Optional[bool] = None
    """图片是否允许拖动"""

    crossOrigin: Optional[str] = None
    """图片的 CORS 属性设置"""

    onError: Optional[str] = None
    """
    图片加载失败的字符串，这个字符串是一个 New Function 内部执行的字符串，参数是 event
    （使用 event.nativeEvent 获取原生 dom 事件），这个字符串需要返回 boolean 值。
    设置 "return true;" 会在图片加载失败后，使用 text 或者 icon 代表的信息来进行替换。
    注意：图片加载失败，不包括获取数据为空情况
    """
