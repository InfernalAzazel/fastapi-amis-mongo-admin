from fastapi_amis_admin.amis.data_display.remark import *
from fastapi_amis_admin.amis.types import *


class APage(BasePage):
    """
    Page 页面

    Page 组件是 amis 页面 JSON 配置中顶级容器组件，
    是整个页面配置的入口组件。
    """

    __default_template_path__: str = 'page.jinja2'

    type: str = 'page'
    """指定为 Page 组件"""

    title: SerializeAsAny[Optional[SchemaNode]] = None
    """页面标题"""

    subTitle: SerializeAsAny[Optional[SchemaNode]] = None
    """页面副标题"""

    remark: SerializeAsAny[Optional["ARemarkT"]] = None
    """标题附近会出现一个提示图标，鼠标放上去会提示该内容。"""

    aside: SerializeAsAny[Optional[SchemaNode]] = None
    """往页面的边栏区域加内容"""

    asideResizor: Optional[bool] = None
    """页面的边栏区域宽度是否可调整"""

    asideMinWidth: Optional[int] = None
    """页面边栏区域的最小宽度"""

    asideMaxWidth: Optional[int] = None
    """页面边栏区域的最大宽度"""

    asideSticky: bool = True
    """用来控制边栏固定与否"""

    toolbar: SerializeAsAny[Optional[SchemaNode]] = None
    """往页面的右上角加内容，需要注意的是，当有 title 时，该区域在右上角，没有时该区域在顶部"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """往页面的内容区域加内容"""

    className: Optional[str] = None
    """外层 dom 类名"""

    cssVars: Optional[dict] = None
    """自定义 CSS 变量，请参考样式"""

    toolbarClassName: Optional[str] = 'v-middle wrapper text-right bg-light b-b'
    """Toolbar dom 类名"""

    bodyClassName: Optional[str] = 'wrapper'
    """Body dom 类名"""

    asideClassName: Optional[str] = 'w page-aside-region bg-auto'
    """Aside dom 类名"""

    headerClassName: Optional[str] = 'bg-light b-b wrapper'
    """Header 区域 dom 类名"""

    initApi: Optional[API] = None
    """Page 用来获取初始数据的 api。返回的数据可以整个 page 级别使用。"""

    initFetch: bool = True
    """是否起始拉取 initApi"""

    initFetchOn: Optional[Expression] = None
    """是否起始拉取 initApi, 通过表达式配置"""

    interval: int = 3000
    """刷新时间(最小 1000)"""

    silentPolling: bool = False
    """	配置刷新时是否显示加载动画"""

    stopAutoRefreshWhen: Optional[Expression] = None
    """通过表达式来配置停止刷新的条件"""

    pullRefresh: Any = {'disabled': True}
    """下拉刷新配置（仅用于移动端）"""