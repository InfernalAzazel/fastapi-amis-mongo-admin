from fastapi_amis_admin.amis.types import *
from fastapi_amis_admin.amis.data_display.remark import ARemarkT


class Tasks(AmisNode):
    """
    Tasks 任务操作集合

    参考：https://aisuda.bce.baidu.com/amis/zh-CN/components/tasks#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class TaskItem(BaseModel):
        label: Optional[str] = None
        """任务名称"""

        key: Optional[str] = None
        """任务键值，请唯一区分"""

        remark: Optional[str] = None
        """当前任务状态，支持 html"""

        status: Optional[str] = None
        """
        任务状态：
        0: 初始状态，不可操作。
        1: 就绪，可操作状态。
        2: 进行中，还没有结束。
        3: 有错误，不可重试。
        4: 已正常结束。
        5: 有错误，且可以重试。
        """

    type: str = "tasks"  # Specify as Tasks renderer

    className: Optional[str] = None
    """外层 Dom 的类名"""

    tableClassName: Optional[str] = None
    """table Dom 的类名"""

    items: Optional[List[TaskItem]] = None
    """任务列表"""

    checkApi: Optional[Dict] = None
    """返回任务列表，返回的数据请参考 items。"""

    submitApi: Optional[Dict] = None
    """提交任务使用的 API"""

    reSubmitApi: Optional[Dict] = None
    """如果任务失败，且可以重试，提交的时候会使用此 API"""

    interval: Optional[int] = None
    """
    - 当有任务进行中，会每隔一段时间再次检测，而时间间隔就是通过此项配置
    - 默认值：3000
    """

    taskNameLabel: Optional[str] = None
    """任务名称列说明"""

    operationLabel: Optional[str] = None
    """操作列说明"""

    statusLabel: Optional[str] = None
    """状态列说明"""

    remarkLabel: SerializeAsAny[Optional[ARemarkT]] = None
    """备注列说明"""

    btnText: Optional[str] = None
    """操作按钮文字"""

    retryBtnText: Optional[str] = None
    """重试操作按钮文字"""

    btnClassName: Optional[str] = None
    """
    - 配置容器按钮 className
    - 默认值：'btn-sm btn-default'
    """

    retryBtnClassName: Optional[str] = None
    """
    - 配置容器重试按钮 className
    - 默认值：'btn-sm btn-danger'
    """

    statusLabelMap: Optional[List[str]] = None
    """
    - 状态显示对应的类名配置
    - 默认值：['label-warning', 'label-info', 'label-success', 'label-danger', 'label-default', 'label-danger']
    """

    statusTextMap: Optional[List[str]] = None
    """
    - 状态显示对应的文字显示配置
    - 默认值：['未开始', '就绪', '进行中', '出错', '已完成', '出错']
    """