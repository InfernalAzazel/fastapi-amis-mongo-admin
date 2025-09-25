from pydantic import Field
from fastapi_amis_admin.amis.data_display.iframe import AIframe
from fastapi_amis_admin.amis.layout.page import APage
from fastapi_amis_admin.amis.types import *

class APageSchema(AmisNode):
    """
    页面配置

    参考：https://baidu.github.io/amis/zh-CN/components/app#%E5%B1%9E%E6%80%A7%E8%AF%B4%E6%98%8E
    """

    label: Optional[str] = None
    """菜单名称"""

    icon: str = "fa fa-flash"
    """菜单图标，比如：fa fa-file."""

    url: Optional[str] = None
    """页面路由路径，当路由命中该路径时，启用当前页面。当路径不是 / 打头时，会连接父级路径。比如：父级的路径为"""

    schema_: SerializeAsAny[Union["APage", "AIframe"]] = Field(None, alias="schema")
    """页面的配置，具体配置请前往 Page 页面说明"""
    schemaApi: Optional[API] = None

    """如果想通过接口拉取，请配置。返回路径为 json>data。schema 和 schemaApi 只能二选一"""
    link: Optional[str] = None

    """如果想配置个外部链接菜单，只需要配置 link 即可"""
    redirect: Optional[str] = None

    """如果想配置个外部链接菜单，只需要配置 link 即可"""
    rewrite: Optional[str] = None

    """改成渲染其他路径的页面，这个方式页面地址不会发生修改"""
    isDefaultPage: Union[bool, str, None] = None

    """当你需要自定义 404 页面的时候有用，不要出现多个这样的页面，因为只有第一个才会有用"""
    visible: Union[bool, str, None] = None

    """有些页面可能不想出现在菜单中，可以配置成 false，另外带参数的路由无需配置，直接就是不可见的"""
    className: Optional[str] = None
    """菜单类名"""

    children: SerializeAsAny[Optional[List["APageSchema"]]] = None
    """子菜单"""


class AApp(BasePage):
    """
    App 多页应用

    用于实现多页应用，适合于全屏模式，如果只是局部渲染请不要使用。
    """

    __default_template_path__: str = "app.jinja2"

    type: str = "app"
    """指定为 app 渲染器"""

    api: Optional[API] = None
    """页面配置接口，如果你想远程拉取页面配置请配置。返回配置路径 json>data>pages，具体格式请参考 pages 属性"""

    brandName: Optional[Template] = None
    """应用名称"""

    logo: Optional[str] = None
    """支持图片地址，或者 svg"""

    className: Optional[str] = None
    """css 类名"""

    header: SerializeAsAny[Optional[Template]] = None
    """顶部区域"""

    asideBefore: SerializeAsAny[Optional[Template]] = None
    """页面菜单上前面区域"""

    asideAfter: SerializeAsAny[Optional[Template]] = None
    """页面菜单下前面区域"""

    footer: SerializeAsAny[Optional[Template]] = None
    """脚页"""

    pages: SerializeAsAny[Optional[List[Union[APageSchema, dict]]]] = None
    """
    Array<页面配置>具体的页面配置。 通常为数组，
    数组第一层为分组，一般只需要配置 label 集合，如果你不想分组，
    直接不配置，真正的页面请在第二层开始配置，即第一层的 children 中
    """



