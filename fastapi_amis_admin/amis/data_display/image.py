from fastapi_amis_admin.amis.types import *


class AImage(AmisNode):
    """
    Image 图片

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/image#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['image', 'static-image'] = "image"
    """如果在 Table、Card 和 List 中，为'image'；在 Form 中用作静态展示，为'static-image'"""

    className: Optional[str] = None
    """外部 CSS 类名"""

    innerClassName: Optional[str] = None
    """组件内层 CSS 类名"""

    imageClassName: Optional[str] = None
    """图像 CSS 类名"""

    thumbClassName: Optional[str] = None
    """图片缩率图 CSS 类名"""

    height: Optional[int] = None
    """图片缩率高度"""

    width: Optional[int] = None
    """图片缩率宽度"""

    title: Optional[Optional[str]] = None
    """标题"""

    imageCaption: Optional[str] = None
    """描述"""

    placeholder: Optional[str] = None
    """占位文本"""

    defaultImage: Optional[str] = None
    """无数据时显示的图片"""

    src: Optional[str] = None
    """缩略图地址"""

    href: Optional[Template] = None
    """外部链接地址"""

    originalSrc: Optional[str] = None
    """原图地址"""

    enlargeAble: Optional[bool] = None
    """支持放大预览"""

    enlargeTitle: Optional[str] = None
    """放大预览的标题"""

    enlargeCaption: Optional[str] = None
    """放大预览的描述"""

    enlargeWithGallary: Optional[str] = None
    """
    - 在表格中，图片的放大功能会默认展示所有图片信息，设置为false将关闭放大模式下图片集列表的展示
    - 默认值：true
    """

    thumbMode:  Optional[Literal['w-full', 'h-full', 'contain', 'cover']] = None
    """
    - 预览图模式
    - 默认值：'contain'
    """

    thumbRatio: Optional[Literal['1:1', '4:3', '16:9']] = None
    """
    - 预览图比例
    - 默认值：'1:1'
    """

    imageMode: Optional[Literal['thumb', 'original']] = None
    """
    - 图片展示模式，缩略图模式 或者 原图模式
    - 默认值：'thumb'
    """
    showToolbar: Optional[bool] = None
    """放大模式下是否展示图片的工具栏，版本号 2.2.0 以上"""

    toolbarActions: SerializeAsAny[Optional[list['AImageAction']]] = None
    """图片工具栏，支持旋转，缩放，默认操作全部开启，版本号 2.2.0 以上"""

    maxScale: Optional[Union[int, Template]] = None
    """执行调整图片比例动作时的最大百分比，版本号 3.4.4 以上"""

    minScale: Optional[Union[int, Template]] = None
    """执行调整图片比例动作时的最小百分比，版本号 3.4.4 以上"""


class AImageAction(AmisNode):
    key: Literal['rotateRight', 'rotateLeft', 'zoomIn', 'zoomOut', 'scaleOrigin']
    """操作key"""

    label: Optional[str] = None
    """动作名称"""

    icon: Optional[str] = None
    """动作icon"""

    iconClassName: Optional[str] = None
    """动作自定义CSS类"""

    disabled: Optional[bool] = None
    """动作是否禁用"""
