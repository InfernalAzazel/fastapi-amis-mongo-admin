from fastapi_amis_admin.amis.types import *


class AService(AmisNode):
    """
    Service 功能型容器

    - amis 中部分组件，作为展示组件，
      自身没有使用接口初始化数据域的能力，例如：Table、Cards、List等，
      他们需要使用某些配置项，例如source，通过数据映射功能，
      在当前的 数据链 中获取数据，并进行数据展示。

    - 而Service组件就是专门为该类组件而生，它的功能是：配置初始化接口，
      进行数据域的初始化，然后在Service内容器中配置子组件，
      这些子组件通过数据链的方法，获取Service所拉取到的数据。

    参考： https://aisuda.bce.baidu.com/amis/zh-CN/components/service#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class Messages(AmisNode):

        fetchSuccess: Optional[str] = None
        """接口请求成功时的 toast 提示文字"""

        fetchFailed: Optional[str] = None
        """
        - 接口请求失败时 toast 提示文字
        - 默认值：'初始化失败'
        """

    type: str = "service"
    """指定为 service 渲染器	"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """内容容器"""

    api: Optional[API] = None
    """初始化数据域接口地址	"""

    ws: Optional[Union[str, dict]] = None
    """WebScocket 地址"""

    dataProvider: Optional[Union[str, dict]] = None
    """
    - 数据获取函数
    - 版本：1.4.0, 1.8.0 支持env参数，2.3.0 支持基于事件触发
    """

    initFetch: Optional[bool] = None
    """
    - 是否默认拉取
    - 默认值：false
    """

    schemaApi: Optional[API] = None
    """用来获取远程 Schema 接口地址"""

    initFetchSchema: Optional[bool] = None
    """是否默认拉取 Schema"""

    messages: Optional[Messages] = None
    """消息提示覆写，默认消息读取的是接口返回的 toast 提示文字，但是在此可以覆写它。"""

    interval: Optional[int] = None
    """轮询时间间隔，单位 ms(最低 1000)"""

    silentPolling: Optional[bool] = None
    """
    - 配置轮询时是否显示加载动画
    - 默认值：false
    """

    stopAutoRefreshWhen: Optional[Expression] = None
    """配置停止轮询的条件"""

    showErrorMsg: Optional[bool] = None
    """
    - 是否以 Alert 的形式显示 api 接口响应的错误信息，默认展示
    - 默认值：true
    - 版本：2.8.1
    """