from fastapi_amis_admin.amis.types import *


class Video(AmisNode):
    """
    Video 视频

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/video#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "video"

    className: Optional[str] = None
    """外层 Dom 的类名"""

    src: Optional[str] = None
    """视频地址"""

    isLive: Optional[bool] = None
    """
    - 是否为直播
    - 默认值：false
    """

    videoType: Optional[str] = None
    """指定直播视频格式"""

    poster: Optional[str] = None
    """视频封面地址"""

    muted: Optional[bool] = None
    """是否静音"""

    loop: Optional[bool] = None
    """是否循环播放"""

    autoPlay: Optional[bool] = None
    """是否自动播放"""

    rates: Optional[List[float]] = None
    """倍数，格式为[1.0, 1.5, 2.0]"""

    frames: Optional[Dict[str, Any]] = None
    """时刻信息，value 可以设置为图片地址"""

    jumpBufferDuration: Optional[bool] = None
    """点击帧时提前跳转的秒数"""

    stopOnNextFrame: Optional[bool] = None
    """到了下一帧自动停止"""