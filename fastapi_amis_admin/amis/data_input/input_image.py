from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputImage(AFormItem):
    """
    InputImage 图片

    图片格式输入，需要实现接收器，提交时将以 url 的方式提交，
    如果需要以表单方式提交请使用 InputFile。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-image#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Crop(BaseAmisModel):
        aspectRatio: Optional[float] = None
        """裁剪比例。浮点型，默认 1 即 1:1，如果要设置 16:9 请设置 1.7777777777777777 即 16 / 9。"""

        rotatable: Optional[bool] = None
        """
        - 裁剪时是否可旋转
        - 默认值：false
        """

        scalable: Optional[bool] = None
        """
        - 裁剪时是否可缩放
        - 默认值：false
        """

        viewMode: Optional[int] = None
        """
        - 裁剪时的查看模式，0 是无限制
        - 默认值：1
        """

        cropFormat: Optional[int] = None
        """
        - 裁剪文件格式
        - 默认值：'image/png'
        """

        cropQuality: Optional[int] = None
        """
        - 裁剪文件格式的质量，用于 jpeg/webp，取值在 0 和 1 之间
        - 默认值：1
        """

    class Limit(BaseAmisModel):
        width: Optional[int] = None
        """限制图片宽度"""

        height: Optional[int] = None
        """限制图片高度"""

        minWidth: Optional[int] = None
        """限制图片最小宽度"""

        minHeight: Optional[int] = None
        """限制图片最小高度"""

        maxWidth: Optional[int] = None
        """限制图片最大宽度"""

        maxHeight: Optional[int] = None
        """限制图片最大高度"""

        aspectRatio: Optional[int] = None
        """
        限制图片宽高比，格式为浮点型数字，默认 1 即 1:1，
        如果要设置 16:9 请设置 1.7777777777777777 即 16 / 9。
        如果不想限制比率，请设置空字符串。
        """

    type: str = "input-image"


    receiver: Optional[API] = None
    """上传文件接口"""

    accept: Optional[str] = None
    """
    - 支持的图片类型格式，请配置此属性为图片后缀，例如.jpg,.png
    - 默认值：'.jpeg,.jpg,.png,.gif'
    """

    capture: Optional[str] = None
    """
    - 控制 input[type=file] 标签的 capture 属性
    - 默认值：'undefined'
    """

    maxSize: Optional[int] = None
    """文件大小限制，单位为B"""

    maxLength: Optional[int] = None
    """一次只允许上传指定数量文件"""

    multiple: Optional[bool] = None
    """
    - 是否多选
    - 默认值：false
    """

    joinValues: Optional[bool] = None
    """
    - 拼接值
    - 默认值：true
    """

    extractValue: Optional[bool] = None
    """
    - 提取值
    - 默认值：false
    """

    delimiter: Optional[str] = None
    """
    - 拼接符
    - 默认值：','
    """

    autoUpload: Optional[bool] = None
    """
    - 是否选择完自动上传
    - 默认值：true
    """

    hideUploadButton: Optional[bool] = None
    """
    - 隐藏上传按钮
    - 默认值：false
    """

    fileField: Optional[str] = None
    """
    - 文件字段名称
    - 默认值：'file'
    """

    crop: SerializeAsAny[Optional[Union[bool, Crop]]] = None
    """ 用来设置是否支持裁剪"""


    limit: SerializeAsAny[Optional[Limit]] = None
    """限制图片大小"""

    frameImage: Optional[str] = None
    """默认占位图地址"""

    fixedSize: Optional[bool] = None
    """是否开启固定尺寸"""

    fixedSizeClassName: Optional[str] = None
    """固定尺寸展示尺寸"""

    initAutoFill: Optional[bool] = None
    """
    - 表单反显时是否执行 autoFill
    - 默认值：false
    """

    uploadBtnText: SerializeAsAny[Optional[Union[str, SchemaNode]]]= None
    """上传按钮文案"""

    dropCrop: Optional[bool] = None
    """
    - 图片上传后是否进入裁剪模式
    - 默认值：true
    """

    initCrop: Optional[bool] = None
    """
    - 初始化后是否立即进入裁剪模式
    - 默认值：false
    """

    draggable: Optional[bool] = None
    """
    - 是否支持拖拽排序
    - 默认值：false
    """

    draggableTip: Optional[str] = None
    """
    - 拖拽提示文案
    - 默认值：'拖拽排序'
    """