from fastapi_amis_admin.amis.function.action import AAction
from fastapi_amis_admin.amis.types import *


class AList(AmisNode):

    class ListItem(BaseAmisModel):
        title: Optional[str] = None
        """标题模板"""

        titleClassName: Optional[str] = None
        """
        - 标题 CSS 类名
        - 默认值：h5
        """

        subTitle: Optional[str] = None
        """副标题模板"""

        avatar: Optional[str] = None
        """图片地址模板"""

        avatarClassName: Optional[str] = None
        """
        - 图片 CSS 类名
        - 默认值：thumb-sm avatar m-r
        """

        desc: Optional[str] = None
        """描述模板"""

        body: Optional[List[Dict[str, Any]]] = None
        """内容容器"""

        actions: SerializeAsAny[Optional[List[AAction]]] = None
        """按钮区域"""

        actionsPosition: Optional[str] = None
        """
        - 按钮位置
        - 可选：'left' or 'right'
        - 默认值：右侧
        """

    type: str= 'list'
    """指定为列表展示，默认值：'list'"""

    title: Optional[str] = None
    """标题"""

    source: Optional[str] = None
    """
    - 数据源
    - 默认值：${items}
    """

    placeholder: Optional[str] = None
    """
    - 当没数据的时候的文字提示
    - 默认值：‘暂无数据’
    """

    selectable: Optional[bool] = None
    """
    - 列表是否可选
    - 默认值：false
    """

    multiple: Optional[bool] = None
    """
    - 列表是否为多选
    - 默认值：true
    """

    className: Optional[str] = None
    """外层 CSS 类名"""

    headerClassName: Optional[str] = None
    """
    - 顶部外层 CSS 类名
    - 默认值：amis-list-header
    """

    footerClassName: Optional[str] = None
    """
    - 底部外层 CSS 类名
    - 默认值：amis-list-footer
    """

    listItem: SerializeAsAny[Optional[List[ListItem]]] = None
    """配置单条信息"""