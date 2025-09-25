from fastapi_amis_admin.amis.types import *


class AEachLoop(AmisNode):
    """
    Each 循环渲染器

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/each#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    type: str = "each"
    """指定为 Each 组件"""

    value: Optional[list] = None
    """用于循环的值"""

    name: Optional[str] = None
    """获取数据域中变量"""

    source: Optional[DataMapping] = None
    """获取数据域中变量， 支持 数据映射"""

    items: Optional[dict] = None
    """使用value中的数据，循环输出渲染器"""

    placeholder: Optional[str] = None
    """当 value 值不存在或为空数组时的占位文本"""

    itemKeyName: Optional[str] = None
    """
    - 获取循环当前数组成员
    - 默认值：'item'
    """

    indexKeyName: Optional[str] = None
    """
    - 获取循环当前索引
    - 默认值：index
    """