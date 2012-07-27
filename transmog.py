from sqlalchemy import *
from sqlalchemy.dialects.mysql import TINYINT
from models.world import DeclarativeBase, ItemTemplate
from constants import ChrRaces, ChrClasses


class TransmogSet(DeclarativeBase):

    __tablename__ = "transmog_sets"
    __table_args__ = {}

    id = Column(u"id", Integer(), nullable=False, primary_key=True)
    account_id = Column(u"account_id", Integer())
    empty = Column(u"empty", Boolean(), nullable=False, default=False)
    class_ = Column(u"class", TINYINT(), primary_key=True)
    race = Column(u"race", TINYINT(), primary_key=True)
    rating = Column(u"rating", SMALLINT(), primary_key=True)
    bracket = Column(u"bracket", SMALLINT(), primary_key=True)
    helm_id = Column(u"helm_id", Integer())
    shoulder_id = Column(u"shoulder_id", Integer())
    chest_id = Column(u"chest_id", Integer())
    wrist_id = Column(u"wrist_id", Integer())
    hands_id = Column(u"hands_id", Integer())
    waist_id = Column(u"waist_id", Integer())
    legs_id = Column(u"legs_id", Integer())
    boots_id = Column(u"boots_id", Integer())
    mh_id = Column(u"mh_id", Integer())
    oh_id = Column(u"oh_id", Integer())


TRANSMOG_SETS = {
    # Hunter
    ChrClasses.HUNTER.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1000,
            "bracket": 0,
            "items": {
                "helm": "Gronnstalker's Helmet",
                "shoulder": "Gronnstalker's Spaulders",
                "chest": "Gronnstalker's Chestguard",
                "wrist": "Gronnstalker's Bracers",
                "hands": "Gronnstalker's Gloves",
                "legs": "Gronnstalker's Leggings",
                "boots": "Gronnstalker's Boots"
            }
        }
    ],

    # Death Knight
    ChrClasses.DEATH_KNIGHT.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Conqueror's Darkruned Helmet",
                "shoulder": "Conqueror's Darkruned Shoulderplates",
                "chest": "Conqueror's Darkruned Battleplate",
                "hands": "Conqueror's Darkruned Gauntlets",
                "waist": "Acherus Knight's Girdle",
                "legs": "Conqueror's Darkruned Legplates",
                "boots": "Boots of the Underdweller"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Heroes' Scourgeborne Helmet",
                "shoulder": "Heroes' Scourgeborne Pauldrons",
                "chest": "Heroes' Scourgeborne Battleplate",
                "hands": "Heroes' Scourgeborne Gauntlets",
                "waist": "Magroth's Meditative Cincture",
                "legs": "Heroes' Scourgeborne Legplates",
                "boots": "Bladed Steelboots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Helm of the Faceless",
                "shoulder": "Shoulderplates of the Deconstructor",
                "chest": "Unbreakable Chestguard",
                "hands": "Handguards of the Enclave",
                "waist": "Dragonslayer's Brace",
                "legs": "Saronite Plated Legguards",
                "boots": "Charred Saronite Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Greathelm of the Scourge Champion",
                "shoulder": "Blood-Soaked Saronite Plated Spaulders",

                "chest": "Saronite War Plate",
                "hands": "Bloodbane's Gauntlets of Command",
                "waist": "The Plaguebringer's Girdle",
                "legs": "Engraved Saronite Legplates",
                "boots": "Greaves of the Slaughter"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Second Helm of the Executioner",
                "shoulder": "Shoulderplates of Frozen Blood",
                "chest": "Icebound Bronze Cuirass",
                "hands": "Rusty Frozen Fingerguards",
                "waist": "Titanium Links of Lore",
                "legs": "Legguards of the Frosty Depths",
                "boots": "Black Spire Sabatons"
            }
        }
    ],
    
    # Druid
    ChrClasses.DRUID.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Thunderheart Cover",
                "shoulder": "Thunderheart Pauldrons",
                "chest": "Thunderheart Chestguard",
                "wrist": "Thunderheart Wristguards",
                "hands": "Thunderheart Gauntlets",
                "waist": "Belt of Primal Majesty",
                "legs": "Thunderheart Leggings",
                "boots": "Thunderheart Treads"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Nordrassil Headguard",
                "shoulder": "Nordrassil Life-Mantle",
                "chest": "Nordrassil Chestpiece",
                "wrist": "Grove-Bands of Remulos",
                "hands": "Nordrassil Gloves",
                "waist": "Girdle of Zaetar",
                "legs": "Nordrassil Life-Kilt",
                "boots": "Orca-Hide Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Crown of Malorne",
                "shoulder": "Shoulderguards of Malorne",
                "chest": "Chestguard of Malorne",
                "wrist": "Bracers of the White Stag",
                "hands": "Handguards of Malorne",
                "waist": "Cord of Nature's Sustenance",
                "legs": "Legguards of Malorne",
                "boots": "Forestlord Striders"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Valorous Dreamwalker Headpiece",
                "shoulder": "Valorous Dreamwalker Spaulders",
                "chest": "Valorous Dreamwalker Robe",
                "wrist": "Esteemed Bindings",
                "hands": "Valorous Dreamwalker Handguards",
                "waist": "Shackled Cinch",
                "legs": "Valorous Dreamwalker Leggings",
                "boots": "Rainey's Chewed Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Brutal Gladiator's Dragonhide Helm",
                "shoulder": "Brutal Gladiator's Dragonhide Spaulders",
                "chest": "Brutal Gladiator's Kodohide Tunic",
                "wrist": "Guardian's Dragonhide Bracers",
                "hands": "Brutal Gladiator's Dragonhide Gloves",
                "waist": "Guardian's Dragonhide Belt",
                "legs": "Brutal Gladiator's Dragonhide Legguards",
                "boots": "Guardian's Dragonhide Boots"
            }
        }
    ],
    
    # Mage
    ChrClasses.MAGE.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Vengeful Gladiator's Silk Cowl",
                "shoulder": "Vengeful Gladiator's Silk Amice",
                "chest": "Vengeful Gladiator's Silk Raiment",
                "hands": "Vengeful Gladiator's Silk Handguards",
                "waist": "Vindicator's Silk Belt",
                "legs": "Vengeful Gladiator's Silk Trousers",
                "boots": "Vindicator's Silk Footguards"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Frostfire Circlet",
                "shoulder": "Frostfire Shoulderpads",
                "chest": "Frostfire Robe",
                "hands": "Frostfire Gloves",
                "waist": "Frostfire Belt",
                "legs": "Frostfire Leggings",
                "boots": "Frostfire Sandals"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Cowl of Tirisfal",
                "shoulder": "Mantle of Tirisfal",
                "chest": "Robes of Tirisfal",
                "hands": "Gloves of Tirisfal",
                "waist": "Fire-Cord of the Magus",
                "legs": "Leggings of Tirisfal",
                "boots": "Velvet Boots of the Guardian"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Gladiator's Silk Cowl",
                "shoulder": "Gladiator's Silk Amice",
                "chest": "Gladiator's Silk Raiment",
                "hands": "Gladiator's Silk Handguards",
                "waist": "General's Silk Belt",
                "legs": "Gladiator's Silk Trousers",
                "boots": "General's Silk Footguards"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Brutal Gladiator's Silk Cowl",
                "shoulder": "Brutal Gladiator's Silk Amice",
                "chest": "Brutal Gladiator's Silk Raiment",
                "hands": "Brutal Gladiator's Silk Handguards",
                "waist": "Guardian's Silk Belt",
                "legs": "Brutal Gladiator's Silk Trousers",
                "boots": "Guardian's Silk Footguards"
            }
        }
    ],
    
    # Paladin
    ChrClasses.PALADIN.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Judgement Crown",
                "shoulder": "Judgement Spaulders",
                "chest": "Judgement Breastplate",
                "wrist": "Judgement Bindings",
                "hands": "Judgement Gauntlets",
                "waist": "Judgement Belt",
                "legs": "Judgement Legplates",
                "boots": "Judgement Sabatons"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Lightbringer Faceguard",
                "shoulder": "Lightbringer Pauldrons",
                "chest": "Lightbringer Breastplate",
                "wrist": "The Seeker's Wristguards",
                "hands": "Lightbringer Gauntlets",
                "waist": "Girdle of the Lightbearer",
                "legs": "Lightbringer Greaves",
                "boots": "Pearl Inlaid Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Brutal Gladiator's Lamellar Helm",
                "shoulder": "Brutal Gladiator's Lamellar Shoulders",
                "chest": "Brutal Gladiator's Lamellar Chestpiece",
                "wrist": "Guardian's Lamellar Bracers",
                "hands": "Brutal Gladiator's Lamellar Gauntlets",
                "waist": "Guardian's Lamellar Belt",
                "legs": "Brutal Gladiator's Lamellar Legguards",
                "boots": "Guardian's Lamellar Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Merciless Gladiator's Scaled Helm",
                "shoulder": "Merciless Gladiator's Scaled Shoulders",
                "chest": "Merciless Gladiator's Scaled Chestpiece",
                "hands": "Merciless Gladiator's Scaled Gauntlets",
                "waist": "Veteran's Scaled Belt",
                "legs": "Merciless Gladiator's Scaled Legguards",
                "boots": "Veteran's Ornamented Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Gladiator's Lamellar Helm",
                "shoulder": "Gladiator's Lamellar Shoulders",
                "chest": "Gladiator's Lamellar Chestpiece",
                "hands": "Gladiator's Lamellar Gauntlets",
                "waist": "General's Lamellar Belt",
                "legs": "Gladiator's Lamellar Legguards",
                "boots": "General's Lamellar Greaves"
            }
        }
    ],
    
    # Priest
    ChrClasses.PRIEST.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Cowl of Benevolence",
                "shoulder": "Amice of Brilliant Light",
                "chest": "Garments of Temperance",
                "hands": "Gloves of Unfailing Faith",
                "waist": "Belt of Divine Inspiration",
                "legs": "Adorned Supernal Legwraps",
                "boots": "Slippers of Dutiful Mending"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Cowl of the Avatar",
                "shoulder": "Mantle of the Avatar",
                "chest": "Vestments of the Avatar",
                "hands": "Gloves of the Avatar",
                "waist": "Belt of the Long Road",
                "legs": "Breeches of the Avatar",
                "boots": "Boots of the Long Road"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Circlet of Faith",
                "shoulder": "Shoulderpads of Faith",
                "chest": "Robe of Faith",
                "hands": "Gloves of Faith",
                "waist": "Belt of Faith",
                "legs": "Leggings of Faith",
                "boots": "Sandals of Faith"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Valorous Cowl of Sanctification",
                "shoulder": "Valorous Shoulderpads of Sanctification",
                "chest": "Valorous Robe of Sanctification",
                "hands": "Valorous Gloves of Sanctification",
                "waist": "Starwatcher's Binding",
                "legs": "Valorous Leggings of Sanctification",
                "boots": "Treads of the False Oracle"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Cowl of Light's Purity",
                "shoulder": "Shawl of Wonderment",
                "chest": "Robes of Faltered Light",
                "hands": "Handguards of the Dawn",
                "waist": "Belt of Absolution",
                "legs": "Pantaloons of Calming Strife",
                "boots": "Treads of Absolution"
            }
        }
    ],
    
    # Rogue
    ChrClasses.ROGUE.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Deathmantle Helm",
                "shoulder": "Deathmantle Shoulderpads",
                "chest": "Deathmantle Chestguard",
                "wrist": "Vambraces of Ending",
                "hands": "Deathmantle Handguards",
                "waist": "Belt of One-Hundred Deaths",
                "legs": "Deathmantle Legguards",
                "boots": "Boots of Effortless Striking"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Bloodfang Hood",
                "shoulder": "Bloodfang Spaulders",
                "chest": "Bloodfang Chestpiece",
                "wrist": "Bloodfang Bracers",
                "hands": "Bloodfang Gloves",
                "waist": "Bloodfang Belt",
                "legs": "Bloodfang Pants",
                "boots": "Bloodfang Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Vengeful Gladiator's Leather Helm",
                "shoulder": "Vengeful Gladiator's Leather Spaulders",
                "chest": "Vengeful Gladiator's Leather Tunic",
                "wrist": "Vindicator's Leather Bracers",
                "hands": "Vengeful Gladiator's Leather Gloves",
                "waist": "Vindicator's Leather Belt",
                "legs": "Vengeful Gladiator's Leather Legguards",
                "boots": "Vindicator's Leather Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Valorous Bonescythe Helmet",
                "shoulder": "Valorous Bonescythe Pauldrons",
                "chest": "Valorous Bonescythe Breastplate",
                "wrist": "Sinner's Bindings",
                "hands": "Valorous Bonescythe Gauntlets",
                "waist": "Stalk-Skin Belt",
                "legs": "Valorous Bonescythe Legplates",
                "boots": "Boots of Captain Ellis"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Garona's Guise",
                "shoulder": "Shoulderpads of the Intruder",
                "chest": "Embrace of the Gladiator",
                "wrist": "Solar Bindings",
                "hands": "Gloves of the Stonereaper",
                "waist": "Relic Hunter's Cord",
                "legs": "Proto-Hide Leggings",
                "boots": "Runed Ironhide Boots"
            }
        }
    ],
    
    # Shaman
    ChrClasses.SHAMAN.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Vengeful Gladiator's Linked Helm",
                "shoulder": "Vengeful Gladiator's Linked Spaulders",
                "chest": "Vengeful Gladiator's Linked Armor",
                "hands": "Vengeful Gladiator's Linked Gauntlets",
                "waist": "Vindicator's Linked Girdle",
                "legs": "Vengeful Gladiator's Mail Leggings",
                "boots": "Vindicator's Linked Sabatons"
            }
        },
            {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Cataclysm Headguard",
                "shoulder": "Cataclysm Shoulderguards",
                "chest": "Cataclysm Chestguard",
                "hands": "Cataclysm Gloves",
                "waist": "Girdle of Fallen Stars",
                "legs": "Cataclysm Legguards",
                "boots": "Tempest-Strider Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Earthshatter Headpiece",
                "shoulder": "Earthshatter Spaulders",
                "chest": "Earthshatter Tunic",
                "hands": "Earthshatter Handguards",
                "waist": "Earthshatter Girdle",
                "legs": "Earthshatter Legguards",
                "boots": "Earthshatter Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Cyclone Headdress",
                "shoulder": "Cyclone Shoulderpads",
                "chest": "Cyclone Hauberk",
                "hands": "Cyclone Gloves",
                "waist": "Belt of Gale Force",
                "legs": "Cyclone Kilt",
                "boots": "Windshear Boots"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Brutal Gladiator's Linked Helm",
                "shoulder": "Brutal Gladiator's Linked Spaulders",
                "chest": "Brutal Gladiator's Linked Armor",
                "hands": "Brutal Gladiator's Linked Gauntlets",
                "waist": "Guardian's Linked Girdle",
                "legs": "Brutal Gladiator's Linked Leggings",
                "boots": "Guardian's Linked Sabatons"
            }
        }
    ],
    
    # Warlock
    ChrClasses.WARLOCK.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Vengeful Gladiator's Dreadweave Hood",
                "shoulder": "Vengeful Gladiator's Dreadweave Mantle",
                "chest": "Vengeful Gladiator's Dreadweave Robe",
                "wrist": "Vindicator's Dreadweave Cuffs",
                "hands": "Vengeful Gladiator's Dreadweave Gloves",
                "waist": "Vindicator's Dreadweave Belt",
                "legs": "Vengeful Gladiator's Dreadweave Leggings",
                "boots": "Vindicator's Dreadweave Stalkers"
            }
        },
         {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Conqueror's Deathbringer Hood",
                "shoulder": "Conqueror's Deathbringer Shoulderpads",
                "chest": "Conqueror's Deathbringer Robe",
                "hands": "Conqueror's Deathbringer Gloves",
                "waist": "Sash of Potent Incantations",
                "legs": "Conqueror's Deathbringer Leggings",
                "boots": "Starlight Treads"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Hood of the Corruptor",
                "shoulder": "Mantle of the Corruptor",
                "chest": "Robe of the Corruptor",
                "hands": "Gloves of the Corruptor",
                "waist": "Cord of Screaming Terrors",
                "legs": "Leggings of the Corruptor",
                "boots": "Boots of the Shifting Nightmare"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Gladiator's Dreadweave Hood",
                "shoulder": "Gladiator's Dreadweave Mantle",
                "chest": "Gladiator's Dreadweave Robe",
                "hands": "Gladiator's Dreadweave Gloves",
                "waist": "General's Dreadweave Belt",
                "legs": "Gladiator's Dreadweave Leggings",
                "boots": "General's Dreadweave Stalkers"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Valorous Plagueheart Circlet",
                "shoulder": "Valorous Plagueheart Shoulderpads",
                "chest": "Valorous Plagueheart Robe",
                "hands": "Valorous Plagueheart Gloves",
                "waist": "Cincture of Polarity",
                "legs": "Valorous Plagueheart Leggings",
                "boots": "Boots of Persuasion"
            }
        }
    ],
    
    # Warrior
    ChrClasses.WARRIOR.id: [
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 1,
            "items": {
                "helm": "Vengeful Gladiator's Plate Helm",
                "shoulder": "Vengeful Gladiator's Plate Shoulders",
                "chest": "Vengeful Gladiator's Plate Chestpiece",
                "wrist": "Vindicator's Plate Bracers",
                "hands": "Vengeful Gladiator's Plate Gauntlets",
                "waist": "Vindicator's Plate Belt",
                "legs": "Vengeful Gladiator's Plate Legguards",
                "boots": "Vindicator's Plate Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1800,
            "bracket": 1,
            "items": {
                "helm": "Merciless Gladiator's Plate Helm",
                "shoulder": "Merciless Gladiator's Plate Shoulders",
                "chest": "Merciless Gladiator's Plate Chestpiece",
                "wrist": "Veteran's Plate Bracers",
                "hands": "Merciless Gladiator's Plate Gauntlets",
                "waist": "Veteran's Plate Belt",
                "legs": "Merciless Gladiator's Plate Legguards",
                "boots": "Veteran's Plate Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2100,
            "bracket": 0,
            "items": {
                "helm": "Dreadnaught Helmet",
                "shoulder": "Dreadnaught Pauldrons",
                "chest": "Dreadnaught Breastplate",
                "wrist": "Dreadnaught Bracers",
                "hands": "Dreadnaught Gauntlets",
                "waist": "Dreadnaught Waistguard",
                "legs": "Dreadnaught Legplates",
                "boots": "Dreadnaught Sabatons"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 2000,
            "bracket": 0,
            "items": {
                "helm": "Brutal Gladiator's Plate Helm",
                "shoulder": "Brutal Gladiator's Plate Shoulders",
                "chest": "Brutal Gladiator's Plate Chestpiece",
                "wrist": "Guardian's Plate Bracers",
                "hands": "Brutal Gladiator's Plate Gauntlets",
                "waist": "Guardian's Plate Belt",
                "legs": "Brutal Gladiator's Plate Legguards",
                "boots": "Guardian's Plate Greaves"
            }
        },
        {
            "race": ChrRaces.PLAYABLE,
            "rating": 1900,
            "bracket": 0,
            "items": {
                "helm": "Gladiator's Plate Helm",
                "shoulder": "Gladiator's Plate Shoulders",
                "chest": "Gladiator's Plate Chestpiece",
                "wrist": "General's Plate Bracers",
                "hands": "Gladiator's Plate Gauntlets",
                "waist": "Marshal's Plate Belt",
                "legs": "Gladiator's Plate Legguards",
                "boots": "Marshal's Plate Greaves"
            }
        }
    ]
}


def clean(session):
    table = TransmogSet.__table__
    table.drop(checkfirst=True)


def merge(session):
    table = TransmogSet.__table__
    table.create()

    for class_id, sets in TRANSMOG_SETS.items():
        for setinfo in sets:
            if not isinstance(setinfo["race"], (tuple, list)):
                setinfo["race"] = [setinfo["race"]]
            display_ids = {}
            for slot_name, item_name in setinfo["items"].items():
                item = session.query(ItemTemplate).\
                    filter_by(name=item_name).first()
                assert item
                display_ids[slot_name + "_id"] = item.entry
            for race in setinfo["race"]:
                session.add(TransmogSet(
                    class_=class_id,
                    race=race.id,
                    rating=setinfo["rating"],
                    bracket=setinfo["bracket"],
                    **display_ids
                ))
            session.commit()