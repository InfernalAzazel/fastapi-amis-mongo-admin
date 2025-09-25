from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class AInputFile(AFormItem):
    """
    InputFile 文件上传

    参考: https://aisuda.bce.baidu.com/amis/zh-CN/components/form/input-file#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "input-file"

    receiver: Optional[API] = None
    """
    - 上传文件接口
    - 默认值：'text/plain'
    """

    accept: Optional[str] = None
    """
    - 默认只支持纯文本，要支持其他类型，请配置此属性为文件后缀.xxx
    - 默认值：'text/plain'
    """

    capture: Optional[str] = None
    """
    - 用于控制 input[type=file] 标签的 capture 属性，在移动端可控制输入来源
    - 默认值：'undefined'
    """

    asBase64: Optional[bool] = None
    """
    - 将文件以base64的形式，赋值给当前组件
    - 默认值：false
    """

    asBlob: Optional[bool] = None
    """
    - 将文件以二进制的形式，赋值给当前组件
    - 默认值：false
    """

    maxSize: Optional[int] = None
    """
    - 默认没有限制，当设置后，文件大小大于此值将不允许上传。单位为B
    - 默认值：false
    """

    maxLength: Optional[int] = None
    """默认没有限制，当设置后，一次只允许上传指定数量文件"""

    multiple: Optional[bool] = None
    """是否多选"""

    drag: Optional[bool] = None
    """
    - 是否为拖拽上传
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
    - 否选择完就自动开始上传
    - 默认值：true
    """

    hideUploadButton: Optional[bool] = None
    """
    - 隐藏上传按钮
    - 默认值：false
    """

    stateTextMap: Optional[dict] = None
    """
    - 上传状态文案
    - 默认值：{ init: '', pending: '等待上传', uploading: '上传中', error: '上传出错', uploaded: '已上传', ready: '' }
    """

    fileField: Optional[str] = None
    """
    - 如果你不想自己存储，则可以忽略此属性。
    - 默认值：'file'
    """

    nameField: Optional[str] = None
    """
    - 接口返回哪个字段用来标识文件名
    - 默认值：'name'
    """

    valueField: Optional[str] = None
    """
    - 文件的值用那个字段来标识
    - 默认值：'value'
    """

    urlField: Optional[str] = None
    """
    - 文件下载地址的字段名
    - 默认值：'url'
    """

    btnLabel: Optional[str] = None
    """上传按钮的文字"""

    downloadUrl: Optional[Union[bool, str]] = None
    """
    - 默认显示文件路径的时候会支持直接下载，可以支持加前缀如：http://xx.dom/filename= ，如果不希望这样，可以把当前配置项设置为 false
    - 版本： 1.1.6 版本开始支持
    """

    useChunk: Optional[bool] = None
    """
    - amis 所在服务器，限制了文件上传大小不得超出 10M，所以 amis 在用户选择大文件的时候，自动会改成分块上传模式
    - 默认值：'auto'
    """

    chunkSize: Optional[int] = None
    """
    - 分块大小
    - 默认值：5 * 1024 * 1024
    """

    startChunkApi: Optional[API] = None
    """启动块接口"""

    chunkApi: Optional[API] = None
    """块接口"""

    finishChunkApi: Optional[API] = None
    """完成块接口"""

    concurrency: Optional[int] = None
    """分块上传时并行个数"""

    documentation: Optional[str] = None
    """文档内容"""

    documentLink: Optional[str] = None
    """文档链接"""

    autoFill: Optional[dict[str, str]] = None
    """
    - 初表单反显时是否执行
    - 默认值：true
    """
