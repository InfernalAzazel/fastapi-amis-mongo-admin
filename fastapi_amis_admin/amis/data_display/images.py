from fastapi_amis_admin.amis.data_display.image import AImageAction
from fastapi_amis_admin.amis.types import *


class AImages(AmisNode):
    """
    Images 图片集

    图片集展示，不支持配置初始化接口初始化数据域，
    所以需要搭配类似像Service、Form或CRUD这样的，
    具有配置接口初始化数据域功能的组件，或者手动进行数据域初始化，
    然后通过source属性，获取数据链中的数据，完成数据展示。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/images#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: Literal['images', 'static-images'] = 'images'
    """如果在 Table、Card 和 List 中，为'images'；在 Form 中用作静态展示，为'static-images'"""

    className: Optional[str] = None
    """	外层 CSS 类名"""

    defaultImage: Optional[str] = None
    """默认展示图片"""

    value: Union[str, List[str], List[dict], None] = None
    """图片数组"""

    options: SerializeAsAny[Optional[list['AImageData']]] = None
    """数据源"""

    source: Optional[str] = None
    """数据源"""

    delimiter: Optional[str] = None
    """
    - 分隔符，当 value 为字符串时，用该值进行分隔拆分
    - 默认值：','
    """

    src: Optional[str] = None
    """预览图地址，支持数据映射获取对象中图片变量"""

    originalSrc: Optional[DataMapping] = None
    """原图地址，支持数据映射获取对象中图片变量"""

    enlargeAble: Optional[bool] = None
    """支持放大预览"""

    enlargeWithGallary: Optional[bool] = None
    """默认在放大功能展示图片集的所有图片信息；表格中使用时，设置为true将展示所有行的图片信息；设置为false将关闭放大模式下图片集列表的展示"""

    thumbMode: Optional[Literal['w-full', 'h-full', 'contain', 'cover']] = None
    """
    - 预览图模式
    - 默认值：'contain'
    """

    thumbRatio: Optional[Literal['1:1', '4:3', '16:9']] = None
    """
    - 预览图比例
    - 默认值：'1:1'
    """

    showToolbar: Optional[bool] = None
    """放大模式下是否展示图片的工具栏，版本号 2.2.0 以上"""

    toolbarActions: SerializeAsAny[Optional[list[AImageAction]]] = None
    """图片工具栏，支持旋转，缩放，默认操作全部开启，版本号 2.2.0 以上"""

class AImageData(AmisNode):
    image: str
    """小图，预览图"""

    src: Optional[str] = None
    """原图"""

    title: Optional[str] = None
    """标题"""

    description: Optional[str] = None
    """描述"""
