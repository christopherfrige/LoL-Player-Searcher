from typing import List, Optional

from pydantic import BaseModel, Field

# MATCH IN HISTORY --------------------------------------------------------------------------------

class InHistoryBaron(BaseModel):
    first: bool
    kills: int


class InHistoryChampion(BaseModel):
    first: bool
    kills: int


class InHistoryDragon(BaseModel):
    first: bool
    kills: int


class InHistoryInhibitor(BaseModel):
    first: bool
    kills: int


class InHistoryRiftHerald(BaseModel):
    first: bool
    kills: int


class InHistoryTower(BaseModel):
    first: bool
    kills: int


class Objectives(BaseModel):
    baron: InHistoryBaron
    champion: InHistoryChampion
    dragon: InHistoryDragon
    inhibitor: InHistoryInhibitor
    riftHerald: InHistoryRiftHerald
    tower: InHistoryTower


class InHistoryTeam(BaseModel):
    bans: List
    objectives: Objectives
    teamId: int
    win: bool


class InHistoryChallenges(BaseModel):
    _12AssistStreakCount: Optional[int] = Field(None, alias='12AssistStreakCount')
    abilityUses: Optional[int]
    acesBefore15Minutes: Optional[int]
    alliedJungleMonsterKills: Optional[int]
    baronTakedowns: Optional[int]
    blastConeOppositeOpponentCount: Optional[int]
    bountyGold: Optional[int]
    buffsStolen: Optional[int]
    completeSupportQuestInTime: Optional[int]
    controlWardsPlaced: Optional[int]
    damagePerMinute: Optional[float]
    damageTakenOnTeamPercentage: Optional[float]
    dancedWithRiftHerald: Optional[int]
    deathsByEnemyChamps: Optional[int]
    dodgeSkillShotsSmallWindow: Optional[int]
    doubleAces: Optional[int]
    dragonTakedowns: Optional[int]
    earlyLaningPhaseGoldExpAdvantage: Optional[int]
    effectiveHealAndShielding: Optional[int]
    elderDragonKillsWithOpposingSoul: Optional[int]
    elderDragonMultikills: Optional[int]
    enemyChampionImmobilizations: Optional[int]
    enemyJungleMonsterKills: Optional[int]
    epicMonsterKillsNearEnemyJungler: Optional[int]
    epicMonsterKillsWithin30SecondsOfSpawn: Optional[int]
    epicMonsterSteals: Optional[int]
    epicMonsterStolenWithoutSmite: Optional[int]
    firstTurretKilledTime: Optional[float]
    flawlessAces: Optional[int]
    fullTeamTakedown: Optional[int]
    gameLength: Optional[float]
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int]
    goldPerMinute: Optional[float]
    hadOpenNexus: Optional[int]
    highestChampionDamage: Optional[int]
    immobilizeAndKillWithAlly: Optional[int]
    initialBuffCount: Optional[int]
    initialCrabCount: Optional[int]
    jungleCsBefore10Minutes: Optional[int]
    junglerTakedownsNearDamagedEpicMonster: Optional[int]
    kTurretsDestroyedBeforePlatesFall: Optional[int]
    kda: Optional[float]
    killAfterHiddenWithAlly: Optional[int]
    killParticipation: Optional[float]
    killedChampTookFullTeamDamageSurvived: Optional[int]
    killingSprees: Optional[int]
    killsNearEnemyTurret: Optional[int]
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int]
    killsOnRecentlyHealedByAramPack: Optional[int]
    killsUnderOwnTurret: Optional[int]
    killsWithHelpFromEpicMonster: Optional[int]
    knockEnemyIntoTeamAndKill: Optional[int]
    landSkillShotsEarlyGame: Optional[int]
    laneMinionsFirst10Minutes: Optional[int]
    laningPhaseGoldExpAdvantage: Optional[int]
    legendaryCount: Optional[int]
    lostAnInhibitor: Optional[int]
    maxCsAdvantageOnLaneOpponent: Optional[int]
    maxKillDeficit: Optional[int]
    maxLevelLeadLaneOpponent: Optional[int]
    moreEnemyJungleThanOpponent: Optional[int]
    multiKillOneSpell: Optional[int]
    multiTurretRiftHeraldCount: Optional[int]
    multikills: Optional[int]
    multikillsAfterAggressiveFlash: Optional[int]
    mythicItemUsed: Optional[int]
    outerTurretExecutesBefore10Minutes: Optional[int]
    outnumberedKills: Optional[int]
    outnumberedNexusKill: Optional[int]
    perfectDragonSoulsTaken: Optional[int]
    perfectGame: Optional[int]
    pickKillWithAlly: Optional[int]
    poroExplosions: Optional[int]
    quickCleanse: Optional[int]
    quickFirstTurret: Optional[int]
    quickSoloKills: Optional[int]
    riftHeraldTakedowns: Optional[int]
    saveAllyFromDeath: Optional[int]
    scuttleCrabKills: Optional[int]
    shortestTimeToAceFromFirstTakedown: Optional[float]
    skillshotsDodged: Optional[int]
    skillshotsHit: Optional[int]
    snowballsHit: Optional[int]
    soloBaronKills: Optional[int]
    soloKills: Optional[int]
    stealthWardsPlaced: Optional[int]
    survivedSingleDigitHpCount: Optional[int]
    survivedThreeImmobilizesInFight: Optional[int]
    takedownOnFirstTurret: Optional[int]
    takedowns: Optional[int]
    takedownsAfterGainingLevelAdvantage: Optional[int]
    takedownsBeforeJungleMinionSpawn: Optional[int]
    takedownsFirstXMinutes: Optional[int]
    takedownsInAlcove: Optional[int]
    takedownsInEnemyFountain: Optional[int]
    teamBaronKills: Optional[int]
    teamDamagePercentage: Optional[float]
    teamElderDragonKills: Optional[int]
    teamRiftHeraldKills: Optional[int]
    threeWardsOneSweeperCount: Optional[int]
    tookLargeDamageSurvived: Optional[int]
    turretPlatesTaken: Optional[int]
    turretTakedowns: Optional[int]
    turretsTakenWithRiftHerald: Optional[int]
    twentyMinionsIn3SecondsCount: Optional[int]
    unseenRecalls: Optional[int]
    visionScoreAdvantageLaneOpponent: Optional[int]
    visionScorePerMinute: Optional[int]
    wardTakedowns: Optional[int]
    wardTakedownsBefore20M: Optional[int]
    wardsGuarded: Optional[int]


class InHistoryStatPerks(BaseModel):
    defense: int
    flex: int
    offense: int


class InHistorySelection(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class InHistoryStyle(BaseModel):
    description: str
    selections: List[InHistorySelection]
    style: int


class InHistoryPerks(BaseModel):
    statPerks: InHistoryStatPerks
    styles: List[InHistoryStyle]


class InHistoryParticipant(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baitPings: int
    baronKills: int
    basicPings: int
    bountyLevel: int
    challenges: InHistoryChallenges
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    championTransform: int
    commandPings: int
    consumablesPurchased: int
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    dangerPings: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: bool
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    getBackPings: int
    goldEarned: int
    goldSpent: int
    holdPings: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    needVisionPings: int
    neutralMinionsKilled: int
    nexusKills: int
    nexusLost: int
    nexusTakedowns: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
    pentaKills: int
    perks: InHistoryPerks
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    profileIcon: int
    pushPings: int
    puuid: str
    quadraKills: int
    riotIdName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionClearedPings: int
    visionScore: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool


class InHistoryMetadata(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class InHistoryInfo(BaseModel):
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List[InHistoryParticipant]
    platformId: str
    queueId: int
    teams: List[InHistoryTeam]
    tournamentCode: str


class InHistoryMatch(BaseModel):
    metadata: Optional[InHistoryMetadata] = None
    info: Optional[InHistoryInfo] = None


# IN MATCH ----------------------------------------------------------------------------------------

class InMatchPerks(BaseModel):
    perkIds: List[int]
    perkStyle: int
    perkSubStyle: int


class InMatchParticipant(BaseModel):
    teamId: int
    spell1Id: int
    spell2Id: int
    championId: int
    profileIconId: int
    summonerName: str
    bot: bool
    summonerId: str
    gameCustomizationObjects: List
    perks: InMatchPerks


class InMatchObservers(BaseModel):
    encryptionKey: str


class InMatchBannedChampion(BaseModel):
    championId: int
    teamId: int
    pickTurn: int


class InMatch(BaseModel):
    gameId: Optional[int] = None
    mapId: Optional[int] = None
    gameMode: Optional[str] = None
    gameType: Optional[str] = None
    gameQueueConfigId: Optional[int] = None
    participants: Optional[List[InMatchParticipant]] = None
    observers: Optional[InMatchObservers] = None
    platformId: Optional[str] = None
    bannedChampions: Optional[List[InMatchBannedChampion]] = None
    gameStartTime: Optional[int] = None
    gameLength: Optional[int] = None

# -------------------------------------------------------------------------------------------------

class SummonerMatches(BaseModel):
    __root__: List[str]
    