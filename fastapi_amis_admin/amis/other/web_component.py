from fastapi_amis_admin.amis.types import *

class WebComponent(AmisNode):
    """
    Web Component

    专门用来渲染 web component 的组件，可以通过这种方式来扩展 amis 组件，比如使用 Angular。

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/web-component#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = 'web-component'


    tag: Optional[str] = None
    """具体使用的 web-component 标签"""

    props: Optional[Dict] = None
    """标签上的属性"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """子节点"""

    style: Optional[Union[str, dict]] = None
    """样式"""
