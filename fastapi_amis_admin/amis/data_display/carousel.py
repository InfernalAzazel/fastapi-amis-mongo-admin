from fastapi_amis_admin.amis.types import *


class ACarousel(AmisNode):
    """
    Carousel 轮播图

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/carousel#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Option(AmisNode):
        image: Optional[str] = None
        """图片链接"""

        href: Optional[str] = None
        """图片打开网址的链接"""

        imageClassName: Optional[str] = None
        """图片类名"""

        title: Optional[Optional[str]] = None
        """图片标题"""

        titleClassName: Optional[str] = None
        """图片标题类名"""

        description: Optional[str] = None
        """图片描述"""

        descriptionClassName: Optional[str] = None
        """图片描述类名"""

        html: Optional[str] = None
        """HTML 自定义，同Tpl一致"""

    type: str = "carousel"
    """指定为 Carousel 渲染器"""

    className: Optional[str] = None
    """
    - 外层 Dom 的类名
    - 默认值：'panel-default'
    """

    options: SerializeAsAny[Optional[List[Option]]] = None
    """轮播面板数据"""

    itemSchema: Optional[dict] = None
    """自定义schema来展示数据"""

    auto: Optional[bool] = None
    """
    - 是否自动轮播
    - 默认值：true
    """

    interval: Optional[str] = None
    """
    - 切换动画间隔
    - 默认值：'5s'
    """

    duration: Optional[int] = None
    """
    - 切换动画间隔
    - 默认值：500
    """

    width: Optional[str] = None
    """
    - 宽度
    - 默认值：'auto'
    """

    height: Optional[str] = None
    """
    - 高度
    - 默认值：'200px'
    """

    controls: Optional[List[str]] = None
    """
    - 显示左右箭头、底部圆点索引
    - 默认值：['dots', 'arrows']
    """
    controlsTheme: Optional[Literal['light', 'dark']] = None
    """
    - 左右箭头、底部圆点索引颜色
    - 默认值：'light'
    """

    animation: Optional[Literal['fade', 'slide']] = None
    """
    - 切换动画效果
    - 默认值：'fade'
    """

    thumbMode: Optional[str] = None
    """
    
    - 图片默认缩放模式
    - 默认值：'"cover" | "contain"'
    """

    multiple: Optional[dict] = None
    """
    - 多图展示，count 表示展示的数量
    - 默认值：{count: 1}
    """

    alwaysShowArrow: Optional[bool] = None
    """
    - 是否一直显示箭头，为 false 时鼠标 hover 才会显示
    - 默认值：false
    """

    icons: Optional[dict] = None
    """
    - 自定义箭头图标
    - 默认值：false
    """