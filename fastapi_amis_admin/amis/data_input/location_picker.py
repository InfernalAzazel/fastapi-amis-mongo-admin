from fastapi_amis_admin.amis.data_input.form_item import AFormItem
from fastapi_amis_admin.amis.types import *


class ALocationPicker(AFormItem):
    """
    LocationPicker 地理位置

    参数：https://aisuda.bce.baidu.com/amis/zh-CN/components/form/location-picker#%E5%B1%9E%E6%80%A7%E8%A1%A8
    """

    class LocationData(BaseAmisModel):
        address: str
        """地址信息"""

        lng: float
        """
        - 经度
        - 范围：[-180, 180]
        """

        lat: float
        """
        - 维度
        - 范围：[-90, 90]
        """

        vendor: Optional[Literal['baidu', 'gaode']] = None
        """地图厂商类型"""


    type: str = "location-picker"

    value: SerializeAsAny[Optional[LocationData]] = None
    """参考 LocationData"""

    vendor: Optional[Literal['baidu', 'gaode']] = None
    """
    - 地图厂商
    - 默认值：'baidu'
    """

    ak: Optional[str] = None
    """百度/高德地图的 ak"""

    clearable: Optional[bool] = None
    """
    - 输入框是否可清空
    - 默认值：false
    """

    placeholder: Optional[str] = None
    """
    - 默认提示
    - 默认值：'请选择位置'
    """

    autoSelectCurrentLoc: Optional[bool] = None
    """
    - 是否自动选中当前地理位置
    - 默认值：false
    """

    onlySelectCurrentLoc: Optional[bool] = None
    """
    - 是否限制只能选中当前地理位置
    - 默认值：false
    """

    coordinatesType: Optional[Literal['bd09', 'gcj02']] = None
    """
    - 坐标系类型
    - 默认值：'bd09'
    """