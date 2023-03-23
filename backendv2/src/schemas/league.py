from enum import Enum

class ContinentEnum(str, Enum):
    americas = "americas"
    asia = "asia"
    europe = "europe"
    sea = "sea"

    class Config:  
        use_enum_values = True


class RegionEnum(str, Enum):
    br1 = "br1"
    na1 = "na1"
    eun1 = "eun1"
    euw1 = "euw1"
    jp1 = "jp1"
    kr = "kr"
    la1 = "la1"
    la2 = "la2"
    oc1 = "oc1"
    tr1 = "tr1"
    ru = "ru"
    ph2 = "ph2"
    sg2 = "sg2"
    th2 = "th2"
    tw2 = "tw2"
    vn2 = "vn2"

    class Config:  
        use_enum_values = True
