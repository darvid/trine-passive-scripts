from constants import HIGH_LEVEL_GEM_NAMES, META_GEM_NAMES
from models.world import ItemTemplate


# For a BuyCount of over 255 to work, you need to alter
# the item_template table like this:
#    ALTER TABLE item_template CHANGE BuyCount BuyCount smallint;
item_buy_counts = [
    ("Shatter Rounds", 255, 1275),
    ("Iceblade Arrow", 255, 1275),
    ("Arcane Powder", 255, 1275),
    ("Ankh", 255, 1275),
    ("Corpse Dust", 255, 1275),
    ("Light Feather", 255, 1275),
    ("Starleaf Seed", 255, 1275),
    ("Wild Spineleaf", 255, 1275),
    ("Soul Shard", 255, 1275),
    ("Infernal Stone", 255, 1275),
    ("Symbol of Kings", 255, 1275),
    ("Symbol of Divinity", 255, 1275),
    ("Devout Candle", 255, 1275),
    ("Black Jelly", 255, 1275),
    ("Noggenfogger Elixir", 255, 1275),
    ("Savory Deviate Delight", 255, 1275),
    ("Crippling Poison", 255, 1275),
    ("Mind-numbing Poison", 255, 1275),
    ("Instant Poison IX", 255, 1275),
    ("Deadly Poison IX", 255, 1275),
    ("Wound Poison VII", 255, 1275),
    ("Anesthetic Poison II", 255, 1275)
]
item_buy_counts += [
    (gem_name, 1, 1) for gem_name in HIGH_LEVEL_GEM_NAMES 
    if gem_name not in META_GEM_NAMES
]


def merge(session):
    for item_name, buycount, stackable in item_buy_counts:
        item = session.query(ItemTemplate).\
            filter_by(name=item_name).one()
        item.BuyCount = buycount
        item.stackable = stackable
        item.maxcount = 0
        item.BuyPrice = 0
        item.SellPrice = 0
        session.merge(item)