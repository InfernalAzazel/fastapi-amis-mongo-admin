from fastapi_amis_admin.amis.types import *


class AJSONSchemaEditor(AmisNode):
    """
    JSONSchema Editor

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/json-schema-editor#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'json-schema-editor'

    rootTypeMutable: Optional[bool] = None
    """
    - 顶级类型是否可配置
    - 默认值：false
    """

    showRootInfo: Optional[bool] = None
    """
    - 是否显示顶级类型信息
    - 默认值：false
    """

    disabledTypes: Optional[List[Literal['string', 'number', 'interger', 'object', 'number', 'array', 'boolean', 'null']]] = None
    """用来禁用默认数据类型"""

    definitions: Optional[Dict[str, any]] = None
    """用来配置预设类型"""

    mini: Optional[bool] = None
    """用来开启迷你模式"""

    placeholder: Optional[Dict[str, Any]] =None
    """
    - 属性输入控件的占位提示文本
    - 默认值：{key: "字段名", title: "名称", description: "描述", default: "默认值", empty: "<空>"}
    - 版本：2.8.0
    """