from src.schemas.league import ContinentEnum, RegionEnum

def get_continent_by_region(region: RegionEnum) -> str:
    return {
        RegionEnum.br1: ContinentEnum.americas,
        RegionEnum.na1: ContinentEnum.americas,
        RegionEnum.la1: ContinentEnum.americas,
        RegionEnum.la2: ContinentEnum.americas,
        RegionEnum.eun1: ContinentEnum.europe,
        RegionEnum.euw1: ContinentEnum.europe,
        RegionEnum.tr1: ContinentEnum.europe,
        RegionEnum.ru: ContinentEnum.europe,
        RegionEnum.jp1: ContinentEnum.asia,
        RegionEnum.kr: ContinentEnum.asia,
        RegionEnum.oc1: ContinentEnum.sea,
        RegionEnum.ph2: ContinentEnum.sea,
        RegionEnum.sg2: ContinentEnum.sea,
        RegionEnum.th2: ContinentEnum.sea,
        RegionEnum.tw2: ContinentEnum.sea,
        RegionEnum.vn2: ContinentEnum.sea,
    }[region]
