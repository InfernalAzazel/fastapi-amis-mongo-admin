from fastapi_amis_admin.amis.types import *


class Audio(AmisNode):
    """
    Audio 音频

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/audio#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "audio"

    className: Optional[str] = None
    """外层 Dom 的类名"""

    inline: Optional[bool] = None
    """
    - 是否是内联模式
    - 默认值：true
    """

    src: Optional[str] = None
    """音频地址"""

    loop: Optional[bool] = None
    """
    - 是否循环播放
    - 默认值：false
    """

    autoPlay: Optional[bool] = None
    """
    - 是否自动播放
    - 默认值：false
    """

    rates: Optional[List[float]] = None
    """
    - 可配置音频播放倍速
    - 默认值：[]
    """

    controls: Optional[List[str]] = None
    """
    - 内部模块定制化
    - 默认值：['rates', 'play', 'time', 'process', 'volume']
    """