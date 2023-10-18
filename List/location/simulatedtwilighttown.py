from enum import Enum

from List.configDict import locationType
from List.inventory import ability, misc
from List.location.graph import RequirementEdge, chest, popup, stat_bonus, item_bonus, \
    LocationGraphBuilder, START_NODE


class NodeId(str, Enum):
    TwilightTownMapPopup = "Twilight Town Map Popup"
    MunnyPouchPopup = "Munny Pouch Popup"
    RoxasStation = "Roxas Station"
    TwilightThorn = "Twilight Thorn"
    Axel1 = "Axel 1"
    StruggleChampion = "Struggle Champion"
    SimulatedCentralStation = "STT Central Station"
    SimulatedSunsetTerrace = "STT Sunset Terrace"
    SimulatedMansionFoyer = "STT Mansion Foyer"
    SimulatedMansionDiningRoom = "STT Mansion Dining Room"
    NaminesRoom = "Namine's Room"
    SimulatedMansionLibrary = "STT Mansion Library"
    Axel2 = "Axel 2"
    SimulatedMansionBasement = "STT Mansion Basement"
    DataRoxas = "Data Roxas"


class CheckLocation(str, Enum):
    TwilightTownMap = "Twilight Town Map"
    MunnyPouchOlette = "Munny Pouch (Olette)"
    StationDusks = "Station Dusks"
    StationOfSerenityPotion = "Station of Serenity Potion"
    StationOfCallingPotion = "Station of Calling Potion"
    TwilightThorn = "Twilight Thorn"
    Axel1 = "Axel 1"
    StruggleWinnerChampionBelt = "(Struggle Winner) Champion Belt"
    StruggleLoserMedal = "(Struggle Loser) Medal"
    StruggleTrophy = "The Struggle Trophy"
    CentralStationPotion1 = "Central Station Potion (1)"
    CentralStationHiPotion = "STT Central Station Hi-Potion"
    CentralStationPotion2 = "Central Station Potion (2)"
    SunsetTerraceAbilityRing = "Sunset Terrace Ability Ring"
    SunsetTerraceHiPotion = "Sunset Terrace Hi-Potion"
    SunsetTerracePotion1 = "Sunset Terrace Potion (1)"
    SunsetTerracePotion2 = "Sunset Terrace Potion (2)"
    MansionFoyerHiPotion = "Mansion Foyer Hi-Potion"
    MansionFoyerPotion1 = "Mansion Foyer Potion (1)"
    MansionFoyerPotion2 = "Mansion Foyer Potion (2)"
    MansionDiningRoomElvenBandanna = "Mansion Dining Room Elven Bandanna"
    MansionDiningRoomPotion = "Mansion Dining Room Potion"
    NaminesSketches = "Naminé´s Sketches"
    MansionMap = "Mansion Map"
    MansionLibraryHiPotion = "Mansion Library Hi-Potion"
    Axel2 = "Axel 2"
    MansionBasementCorridorHiPotion = "Mansion Basement Corridor Hi-Potion"
    DataRoxasMagicBoost = "Roxas (Data) Magic Boost"


def make_graph(graph: LocationGraphBuilder):
    stt = locationType.STT

    twilight_town_map_popup = graph.add_location(NodeId.TwilightTownMapPopup, [
        popup(319, CheckLocation.TwilightTownMap, stt),
    ])
    munny_pouch_popup = graph.add_location(NodeId.MunnyPouchPopup, [
        popup(288, CheckLocation.MunnyPouchOlette, stt, vanilla=misc.MunnyPouchOlette),
    ])
    roxas_station = graph.add_location(NodeId.RoxasStation, [
        item_bonus(54, CheckLocation.StationDusks, stt, vanilla=ability.AerialRecovery),
        chest(315, CheckLocation.StationOfSerenityPotion, stt),
        chest(472, CheckLocation.StationOfCallingPotion, stt),
    ])
    twilight_thorn = graph.add_location(NodeId.TwilightThorn, [
        item_bonus(33, CheckLocation.TwilightThorn, stt, vanilla=ability.Guard),
    ])
    axel_1 = graph.add_location(NodeId.Axel1, [
        item_bonus(73, CheckLocation.Axel1, stt, vanilla=ability.Scan),
    ])
    struggle_champion = graph.add_location(NodeId.StruggleChampion, [
        popup(389, CheckLocation.StruggleWinnerChampionBelt, stt),
        popup(390, CheckLocation.StruggleLoserMedal, stt),
        popup(519, CheckLocation.StruggleTrophy, stt),
    ])
    central_station = graph.add_location(NodeId.SimulatedCentralStation, [
        chest(428, CheckLocation.CentralStationPotion1, stt),
        chest(429, CheckLocation.CentralStationHiPotion, stt),
        chest(430, CheckLocation.CentralStationPotion2, stt),
    ])
    sunset_terrace = graph.add_location(NodeId.SimulatedSunsetTerrace, [
        chest(434, CheckLocation.SunsetTerraceAbilityRing, stt),
        chest(435, CheckLocation.SunsetTerraceHiPotion, stt),
        chest(436, CheckLocation.SunsetTerracePotion1, stt),
        chest(437, CheckLocation.SunsetTerracePotion2, stt),
    ])
    mansion_foyer = graph.add_location(NodeId.SimulatedMansionFoyer, [
        chest(449, CheckLocation.MansionFoyerHiPotion, stt),
        chest(450, CheckLocation.MansionFoyerPotion1, stt),
        chest(451, CheckLocation.MansionFoyerPotion2, stt),
    ])
    mansion_dining_room = graph.add_location(NodeId.SimulatedMansionDiningRoom, [
        chest(455, CheckLocation.MansionDiningRoomElvenBandanna, stt),
        chest(456, CheckLocation.MansionDiningRoomPotion, stt),
    ])
    namines_room = graph.add_location(NodeId.NaminesRoom, [
        popup(289, CheckLocation.NaminesSketches, stt),
        popup(483, CheckLocation.MansionMap, stt),
    ])
    mansion_library = graph.add_location(NodeId.SimulatedMansionLibrary, [
        chest(459, CheckLocation.MansionLibraryHiPotion, stt),
    ])
    axel_2 = graph.add_location(NodeId.Axel2, [
        stat_bonus(34, CheckLocation.Axel2, stt),
    ])
    mansion_basement = graph.add_location(NodeId.SimulatedMansionBasement, [
        chest(463, CheckLocation.MansionBasementCorridorHiPotion, stt),
    ])
    data_roxas = graph.add_location(NodeId.DataRoxas, [
        popup(558, CheckLocation.DataRoxasMagicBoost, [stt, locationType.DataOrg]),
    ])

    graph.register_superboss(data_roxas)

    if not graph.reverse_rando:
        graph.add_edge(START_NODE, twilight_town_map_popup)
        graph.add_edge(twilight_town_map_popup, munny_pouch_popup)
        graph.add_edge(munny_pouch_popup, roxas_station)
        graph.add_edge(roxas_station, twilight_thorn, RequirementEdge(battle=True))
        graph.add_edge(twilight_thorn, axel_1, RequirementEdge(battle=True))
        graph.add_edge(axel_1, struggle_champion, RequirementEdge(battle=True))
        graph.add_edge(struggle_champion, central_station)
        graph.add_edge(struggle_champion, sunset_terrace)
        graph.add_edge(sunset_terrace, mansion_foyer, RequirementEdge(battle=True))
        graph.add_edge(mansion_foyer, mansion_dining_room)
        graph.add_edge(mansion_foyer, namines_room)
        graph.add_edge(namines_room, mansion_library)
        graph.add_edge(namines_room, axel_2, RequirementEdge(battle=True))
        graph.add_edge(axel_2, mansion_basement)
        graph.add_edge(mansion_basement, data_roxas, RequirementEdge(battle=True))
        graph.register_first_boss(mansion_basement)
        graph.register_last_story_boss(mansion_basement)
    else:
        graph.add_edge(START_NODE, mansion_foyer)
        graph.add_edge(mansion_foyer, mansion_dining_room)
        graph.add_edge(mansion_foyer, namines_room)
        graph.add_edge(namines_room, mansion_library)
        graph.add_edge(namines_room, axel_2, RequirementEdge(battle=True))
        graph.add_edge(axel_2, mansion_basement)
        graph.add_edge(mansion_basement, central_station)
        graph.add_edge(mansion_basement, sunset_terrace)
        graph.add_edge(sunset_terrace, axel_1, RequirementEdge(battle=True))
        graph.add_edge(axel_1, struggle_champion, RequirementEdge(battle=True))
        graph.add_edge(struggle_champion, roxas_station)
        graph.add_edge(roxas_station, twilight_thorn, RequirementEdge(battle=True))
        graph.add_edge(twilight_thorn, twilight_town_map_popup, RequirementEdge(battle=True))
        graph.add_edge(twilight_town_map_popup, munny_pouch_popup)
        graph.add_edge(munny_pouch_popup, data_roxas, RequirementEdge(battle=True))
        graph.register_first_boss(munny_pouch_popup)
        graph.register_last_story_boss(munny_pouch_popup)