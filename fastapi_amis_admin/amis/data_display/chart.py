from fastapi_amis_admin.amis.types import *


class AChart(AmisNode):
    """
    Chart 图表

    图表渲染器，采用 echarts 渲染，配置格式跟 echarts 相同，echarts 配置文档

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/chart#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "chart"
    """指定为 chart 渲染器"""

    className: Optional[str] = None
    """外层 Dom 的类名"""

    body: SerializeAsAny[Optional[SchemaNode]] = None
    """内容容器"""

    api: Optional[API] = None
    """配置项接口地址"""

    source: Optional[DataMapping] = None
    """通过数据映射获取数据链中变量值作为配置"""

    initFetch: Optional[bool] = None
    """组件初始化时，是否请求接口"""

    interval: Optional[int] = None
    """刷新时间(最小 1000)"""

    config: Union[dict, str, None] = None
    """设置 eschars 的配置项,当为string的时候可以设置 function 等配置项"""

    style: Optional[dict] = None
    """设置根元素的 style"""

    width: Optional[str] = None
    """设置根元素的宽度"""

    height: Optional[str] = None
    """设置根元素的高度"""

    replaceChartOption: Optional[bool] = None
    """
    - 每次更新是完全覆盖配置项还是追加？
    - 默认值：false
    """

    trackExpression: Optional[str] = None
    """当这个表达式的值有变化时更新图表"""

    dataFilter: Optional[str] = None
    """
    自定义 echart config 转换，函数签名：function(config, echarts, data) {return config;} 
    配置时直接写函数体。其中 config 是当前 echart 配置，echarts 就是 echarts 对象，data 为上下文数据。
    """

    mapURL: Optional[API] = None
    """地图 geo json 地址"""

    mapName: Optional[str] = None
    """地图名称"""

    loadBaiduMap: Optional[str] = None
    """加载百度地图"""