from random import choice
from sqlalchemy import desc

from constants import ChrClasses, ChrRaces, CLASS_RACE_COMBOS
from models.world import ItemTemplate, Playercreateinfo, \
    PlayercreateinfoItem, NpcVendor


# Starting locations for each faction
FACTION_SPAWNS = {
    "HORDE": {
        "map": 530, 
        "zone": 3521, 
        "position_x": 252.989853, 
        "position_y": 7778.522949, 
        "position_z": 23.224953, 
        "orientation": 1.469257
    },
    # "ALLIANCE": {
    #     "map": 530, 
    #     "zone": 3521, 
    #     "position_x": 278.586060, 
    #     "position_y": 5945.748535, 
    #     "position_z": 149.781937,
    #     "orientation": 1.284102
    # }
    "ALLIANCE": {
        "map": 530, 
        "zone": 3521, 
        "position_x": 281.377441, 
        "position_y": 5994.965820, 
        "position_z": 144.731903,
        "orientation": 1.542708
    }
}


DELETE_ITEMS = [
    2516, # Light Shot
    2512, # Rough Arrow
    2101, # Light Quiver
    2102, # Small Ammo Pouch
    2508, # Old Blunderbuss
    12282, # Worn Battleaxe
]


# Starting items for -all- class/race combinations
STARTING_ITEMS = [
    # give everyone except hunters 4 bags
    [
        ChrRaces.PLAYABLE,
        [r for r in ChrClasses.ALL if r != ChrClasses.HUNTER],
        (
            ("Portable Hole", 4),
        )
    ],
    # give hunters 3 bags + quiver
    [
        ChrRaces.PLAYABLE,
        (ChrClasses.HUNTER,),
        (
            ("Portable Hole", 3),
            "Nerubian Reinforced Quiver"
        )
    ],
    # give both factions nether rays
    [
        ChrRaces.PLAYABLE,
        ChrClasses.ALL,
        (
            lambda: choice(["Blue", "Silver", "Red", "Purple", "Green"]) + 
                " Riding Nether Ray",
        )
    ],
    [
        ChrRaces.HORDE,
        ChrClasses.ALL,
        ("Horn of the Black War Wolf",)
    ],
    [
        ChrRaces.ALLIANCE,
        ChrClasses.ALL,
        ("Reins of the Black War Elekk",)
    ],
    # shaman totems
    [
        ChrRaces.HORDE,
        (ChrClasses.SHAMAN,),
        ("Air Totem", "Fire Totem", "Water Totem", "Earth Totem")
    ],
    # reagents for druids, priests, rogues, and mages
    [
        ChrRaces.PLAYABLE,
        (ChrClasses.DRUID,),
        ("Wild Spineleaf",)
    ],
    [
        ChrRaces.PLAYABLE,
        (ChrClasses.ROGUE,),
        (
            ("Crippling Poison", 255),
            ("Mind-numbing Poison", 255),
            ("Instant Poison IX", 255),
            ("Deadly Poison IX", 255),
            ("Wound Poison VII", 255),
            ("Anesthetic Poison II", 255),
        )
    ]
]

def remove_blizz_starting_items(session):
    # WARNING: DOES NOT MAKE BACKUPS.
    for item_id in DELETE_ITEMS:
        session.query(ItemTemplate).\
            filter_by(entry=item_id).delete()
        # optional, but removes errors about non-existent items in vendors
        session.query(NpcVendor).\
            filter_by(item=item_id).delete()


def remove_faction_req_shatar_mounts(session):
    for mount in session.query(ItemTemplate).\
        filter(ItemTemplate.name.like("%Riding Nether Ray")):
        mount.RequiredReputationRank = 3 # Neutral


def merge_starting_locations(session):
    for faction in ("ALLIANCE", "HORDE"):
        for race in getattr(ChrRaces, faction):
            session.query(Playercreateinfo).\
                filter_by(race=race.id).\
                update(FACTION_SPAWNS[faction])


def class_race_items_iter(itemspec):
    for allowed_races, allowed_classes, items in itemspec:
        for item_name in items:
            for race in allowed_races:
                for class_ in allowed_classes:
                    yield (race, class_, item_name)


def clean(session):
    for race, class_, item_name in class_race_items_iter(STARTING_ITEMS):
        if isinstance(item_name, (tuple, list)):
            item_name, amount = item_name
        item = session.query(ItemTemplate).\
            filter_by(name=item_name).\
            order_by(desc(ItemTemplate.RequiredSkillRank)).\
            first()
        session.query(PlayercreateinfoItem).\
            filter_by(race=race, class_=class_.id,
                itemid=item.entry).\
            delete()


def merge_starting_items(session):
    for race, class_, item_name in class_race_items_iter(STARTING_ITEMS):
        if isinstance(item_name, (tuple, list)):
            item_name, amount = item_name
        else:
            amount = 1
        item = session.query(ItemTemplate).\
            filter_by(name=item_name).\
            order_by(desc(ItemTemplate.RequiredSkillRank)).\
            first()
        session.query(PlayercreateinfoItem).\
            filter_by(race=race.id, class_=class_.id,
                itemid=item.entry).\
            delete()
        session.add(PlayercreateinfoItem(
            race=race.id,
            class_=class_.id,
            itemid=item.entry,
            amount=amount
        ))


def merge(session):
    remove_blizz_starting_items(session)
    remove_faction_req_shatar_mounts(session)
    merge_starting_locations(session)
    merge_starting_items(session)