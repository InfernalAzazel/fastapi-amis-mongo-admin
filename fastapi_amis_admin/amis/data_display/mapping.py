from fastapi_amis_admin.amis.types import *

class AMapping(AmisNode):
    """
    Mapping 映射

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/mapping#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "mapping"

    className: Optional[str] = None
    """外层 CSS 类名"""

    placeholder: Optional[str] = None
    """占位文本"""

    map: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = None
    """映射配置"""

    source: Optional[Union[str, Any]] = None
    """API 或 数据映射"""

    valueField: Optional[str] = None
    """
    - 用来匹配映射的字段名
    - 默认值：value
    - 版本：2.5.2
    """

    labelField: Optional[str] = None
    """
    - 用来展示的字段名
    - 默认值：label
    - 版本：2.5.2
    """

    itemSchema: Optional[API] = None
    """
    - 自定义渲染模板，支持html或schemaNode
    - 版本：2.5.2
    - 使用说明：
      
      - 当映射值是非object时，可使用${item}获取映射值
      
      - 当映射值是object时，可使用映射语法: ${xxx}获取object的值
      
      - 可使用数据映射语法：${xxx}获取数据域中变量值
    """
