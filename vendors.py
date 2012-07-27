from sqlalchemy import desc
from sqlalchemy.orm import class_mapper

from constants import InventoryType, NpcFlag, HIGH_LEVEL_GEM_NAMES
from util import get_items, init_custom_id, incr_custom_id
from models.world import CreatureTemplate, ItemTemplate, NpcText, NpcVendor


TOC_ACCESSORIES = [
    "Amulet of Binding Elements^",
    "Charge of the Demon Lord^",
    "Collar of Ceaseless Torment^",
    "Cry of the Val'kyr^",
    "Legionnaire's Gorget^",
    "Necklace of Unerring Mettle^",

    "Pandora's Plea^",
    "Bandit's Insignia^",
    "Comet's Trail^",
    "Darkmoon Card: Greatness%",
    "Death's Choice^",
    "Death's Verdict^",
    "Eitrigg's Oath^",
    "Fetish of Volatile Power^",
    "Flow of Knowledge^",
    "Juggernaut's Vitality^",
    "Needle-Encrusted Scorpion^",
    "Platinum Disks of Battle^",
    "Platinum Disks of Sorcery^",
    "Platinum Disks of Swiftness^",
    "Reign of the Dead^",
    "Reign of the Unliving^",
    "Satrina's Impeding Scarab^",
    "Scale of Fates^",
    "Show of Faith^",
    "Solace of the Defeated^",
    "Solace of the Fallen^",
    "Talisman of Volatile Power^",
    "Vengeance of the Forsaken^",
    "Battlemaster's Precision^",
    "Battlemaster's Rage^",
    "Battlemaster's Ruination^",
    "Battlemaster's Vivacity^",
    "Darkmoon Card: Death^",
    "Extract of Necromantic Power^",
    "Binding Light^",
    "Coren's Chromium Coaster^",
    "Binding Stone^",
    "Dark Matter^",
    "Mjolnir Runestone^",
    "Talisman of Resurgence^",
    "Meteorite Crystal^",
    "Dying Curse^",
    "Flare of the Heavens^",
    "Shard of the Crystal Heart^",
    "Mark of Supremacy^",
    "Lavanthor's Talisman^",
    
    "Band of Callous Aggression^",
    "Band of the Traitor King^",
    "Band of the Violent Temperment^",
    "Circle of the Darkmender^",
    "Firestorm Band^",
    "Ring of Callous Aggression^",
    "Signet of the Earthshaker^",
]
TOC_OFFSETS = [
    "Shawl of Fervent Crusader^",
    "Drape of Bitter Incantation^",
    "Cloak of the Silver Covenant^",
    "Cloak of the Victorious Combatant^",
    "Cloak of the Unmoving Guardian^",
    "Maiden's Favor^",
    "Shawl of the Refreshing Winds^",
    "Pride of the Eredar^",
    "Strength of the Nerub^",
    "Cloak of the Unflinching Guardian^",
    "Might of the Nerub^",
    "Cloak of the Triumphant Combatant^",
    "Cloak of Serrated Blades^",
    "Drape of the Refreshing Winds^",
    "Drape of the Sunreavers^",
    "Maiden's Adoration^",
    "Shawl of the Devout Crusader^",
    "Pride of the Demon Lord^",
    "Tattered Castle Drape^",

    "Dawnwalkers^",
    "Sabatons of the Courageous^",
    "Greaves of the 7th Legion^",
    "Dawnbreaker Sabatons^",
    "Dawnbreaker Greaves^",
    "Boots of the Courageous^",
    "Boots of the Mourning Widow^",
    "Footpads of the Icy Floe^",
    "Sandals of the Mourning Widow^",
    "Boots of the Harsh Winter^",
    "Boots of the Unrelenting Storm^",
    "Icewalker Treads^",
    "Treads of the Icewalker^",
    "Boots of Tortured Space^",
    "Boots of Tremoring Earth^",
    "Greaves of Ruthless Judgment^",
    "Sabatons of Ruthless Judgment^",
    "Sabatons of Tremoring Earth^",

    "Armbands of Dark Determination^",
    "Bindings of the Ashen Saint^",
    "Armbands of the Ashen Saint^",
    "Bracers of Dark Determination^",
    "Bracers of the Untold Massacre^",
    "Armguards of the Shieldmaiden^",
    "Bracers of the Silent Massacre^",
    "Bindings of the Autumn Willow^",
    "Boneshatter Vambraces^",
    "Dark Essence Bindings^",
    "Wristwraps of Cloudy Omen^",
    "Bindings of Dark Essence^",
    "Bracers of the Shieldmaiden^",
    "Vambraces of the Broken Bond^",
    "Bracers of Cloudy Omen^",
    "Bracers of the Autumn Willow^",
    "Boneshatter Armplates^",
    "Bracers of the Broken Bond^",

    "Cord of the Tenebrous Mist^",
    "Cord of Pale Thorns ^",
    "Belt of Deathly Dominion^",
    "Belt of the Forgotten Martyr^",
    "Belt of the Merciless Killer^",
    "Cord of Biting Cold^",
    "Belt of Biting Cold^",
    "Bloodbath Girdle^",
    "Belt of Pale Thorns^",
    "Waistguard of Deathly Dominion^",
    "Girdle of the Forgotten Martyr^",
    "Belt of the Ice Burrower^",
    "Binding of the Ice Burrower^",
    "Belt of the Pitiless Killer^",
    "Girdle of Bloodied Scars^",
    "Belt of Bloodied Scars^",
    "Bloodbath Belt^",
    "Belt of the Tenebrous Mist^",
]
TOC_WEAPONS = [
    "Blade of Tarasque^",
    "Steel Bladebreaker^",
    "Lionhead Slasher^",
    "Talonstrike^",
    "Justicebringer^",
    "Twin Spike^",
    "Lupine Longstaff^",
    "Stormpike Cleaver^",
    "Misery's End^",
    "Archon Glaive^",
    "Blade of the Unbroken Covenant^",
    "Silverwing Defender^",
    "Decimation^",
    "Remorseless^",
    "Catastrophe^",
    "Clemency^",
    "BRK-1000^",
    "Barb of Tarasque^",
    "Stygian Bladebreaker^",
    "Blood Fury^",
    "Death's Head Crossbow^",
    "Dual-blade Butcher^",
    "Gouge of the Frigid Heart^",
    "Twin's Pact^",
    "Hellscream Slicer^",
    "Suffering's End^",
    "Hellion Glaive^",
    "Mortalis^",
    "Orgrim's Deflector^",
    "Fleshrender^",
    "Cudgel of the Damned^",
    "Grievance^",
    "Sufferance^",
    "Fezzik's Autocannon^",
]
SEASON_7_AND_8_MAINSET_NAMES = [
    "Dreadplate", "Leather", "Chain", "Silk", "Felweave",
    "Plate", "Kodohide", "Dragonhide", "Wyrmhide", "Ornamented",
    "Scaled", "Mail", "Linked", "Ringmail", "Mooncloth", "Satin"
]
SEASON_7_AND_8_WEAPON_NAMES = [
    "Dirk", "Eviscerator", "Spike", "Blade of Celerity",

    "Splitter", "Dicer", "Handaxe",

    "Swiftblade", "Longblade",

    "Left Claw", "Left Razor", 

    "Gavel", "Punisher", "Truncheon",

    "Shotgun", "Repeater", "Recurve",

    "War Edge", 

    "Acute Staff", "Skirmish Staff", "Combat Staff", "Light Staff",
    
    "Sunderer", "Claymore", "Halberd", "Crusher",

    "Piercing Touch", "Touch of Defeat", "Baton of Light",
    "Wand of Alacrity",
    
    "Compendium", "EndGame", "Reprieve", "Grimoire",

    "Barrier", "Redoubt", "Shield Wall",
    
    "Idol of Resolve", "Idol of Steadfastness", "Idol of Tenacity",
    "Libram of Fortitude", "Libram of Justice",
    "Totem of Indomitability", "Totem of Survival", "Totem of the Third Wind",
    "Sigil of Strife"
]
SEASON_7_MAINSET = ["Relentless Gladiator's " + i + "%" for i in 
    SEASON_7_AND_8_MAINSET_NAMES]
SEASON_8_MAINSET = ["Wrathful Gladiator's " + i + "%" for i in 
    SEASON_7_AND_8_MAINSET_NAMES]
    
SEASON_7_WEAPONS = ["Relentless Gladiator's " + i + "%" for i in 
SEASON_7_AND_8_WEAPON_NAMES]
SEASON_8_WEAPONS = ["Wrathful Gladiator's " + i + "%" for i in 
SEASON_7_AND_8_WEAPON_NAMES]

ICC_HEROIC_OFFSETS = [
    "Taiga Bindings^",
    "Ether-Soaked Bracers^",
    "Wrists of Septic Shock^",
    "Gargoyle Spit Bracers^",
    "Bracers of Pale Illumination^",
    "Icecrown Rampart Bracers^",
    "Bracers of Dark Blessings^",
    "Coldwraith Bracers^",
    "Vambraces of the Frost Wyrm Queen^",
    "Bracers of Eternal Dreaming^",
    "The Lady's Brittle Bracers^",
    "Scourge Hunter's Vambraces^",
    "Polar Bear Claw Bracers^",
    "Toskk's Maximized Wristguards^",
    "Death Surgeon's Sleeves^",
    "Bloodsunder's Bracers^",
    "Crypt Keeper's Bracers^",
    "Bracers of Dark Reckoning^",

    "Ironrope Belt of Ymirjar^",
    "Tightening Waistband^",
    "Blood-Drinker's Girdle^",
    "Cauterized Cord^",
    "Flesh-Shaper's Gurney Strap^",
    "Cord of Dark Suffering^",
    "Deathspeaker Disciple's Belt^",
    "Soulthief's Braided Belt^",
    "Cord of the Patronizing Practitioner^",
    "Linked Scourge Vertebrae^",
    "Etched Dragonbone Girdle^",
    "Waistband of Righteous Fury^",
    "Belt of the Blood Nova^",
    "Nerub'ar Stalker's Cord^",
    "Belt of Broken Bones^",
    "Lingering Illness^",
    "Professor's Bloodied Smock^",
    "Astrylian's Sutured Cinch^",
    "Coldwraith Links^",
    "Crushing Coldwraith Belt^",

    "Lich Wrappings^",
    "Heartsick Mender's Cape^",
    "Cloak of Many Skins^",
    "Saronite Gargoyle Cloak^",
    "Shawl of Nerubian Silk^",
    "Frostbinder's Shredded Cape^",
    "Shadowvault Slayer's Cloak^",
    "Greatcloak of the Turned Champion^",
    "Winding Sheet^",
    "Royal Crimson Cloak^",

    "Pale Corpse Boots^",
    "Taldaram's Soft Slippers^",
    "Shuffling Shoes^",
    "Taldron's Long Neglected Boots^",
    "Icecrown Spire Sandals^",
    "Bone Drake's Enameled Boots^",
    "Boots of the Frozen Seed^",
    "Ancient Skeletal Boots^",
    "Wyrmwing Treads^",
    "Scourge Fanged Stompers^",
    "Boots of the Funeral March^",
    "Blood-Soaked Saronite Stompers^",
    "Necrophotic Greaves^",
    "Boots of Unnatural Growth^",
    "Plague Scientist's Boots^",
    "Grinning Skull Greatboots^",
    "Treads of the Wasteland^",
    "Frostbitten Fur Boots^",
]
ICC_HEROIC_ACCESSORIES = [
    "Collar of Haughty Disdain^",
    "Pendant of Split Veins^",
    "Infected Choker^",
    "Choker of Filthy Diamonds^",
    "Precious's Putrid Collar^",
    "Soulcleave Pendant^",
    "Marrowgar's Scratching Choker^",
    "Rimetooth Pendant^",
    "Noose of Malachite^",
    "Sindragosa's Cruel Claw^",
    "Ahn'kahar Onyx Neckguard^",
    "Amulet of the Silent Eulogy^",
    "Bile-Encrusted Medallion^",
    "Holiday's Grace^",
    "Blood Queen's Crimson Choker^",
    "Lana'thel's Chain of Flagellation^",
    "Bone Sentinel's Amulet^",

    "Seal of the Twilight Queen^",
    "Cerise Coiled Ring^",
    "Thrice Fanged Signet^",
    "Rotface's Rupturing Ring^",
    "Signet of Putrefaction^",
    "Saurfang's Cold-Forged Band^",
    "Abomination's Bloody Ring^",
    "Memory of Malygos^",
    "Juggernaut Band^",
    "Ring of Maddening Whispers^",
    "Skeleton Lord's Circle^",
    "Ring of Rapid Ascent^",
    "Seal of Many Mouths^",
    "Might of Blight^",
    "Valanar's Other Signet Ring^",
    "Incarnadine Band of Mending^",
    "Devium's Eternally Cold Ring^",
    "Frostbrood Sapphire Ring^",
    "Loop of the Endless Labyrinth^",
    "Marrowgar's Frigid Eye^",
    "Band of the Bone Colossus^",

    "Whispering Fanged Skull^",
    "Unidentifiable Organ^",
    "Muradin's Spyglass^",
    "Sliver of Pure Ice^",
    "Althor's Abacus^",
    "Phylactery of the Nameless Lich^",
    "Sindragosa's Flawless Fang^",
    "Deathbringer's Will^",
    "Corpse Tongue Coin^",
    "Dislodged Foreign Object^",
    "Tiny Abomination in a Jar^",
    "Bauble of True Blood^",
]
ICC_HEROIC_WEAPONS_277 = [
    "Nibelung^",
    "Distant Land^",
    "Bryntroll, the Bone Arbiter^",
    "Dying Light^",
    "Bloodfall^",
    "Cryptmaker^",
    "Glorenzelg, High-Blade of the Silver Hand",
    "Oathbinder, Charge of the Ranger-General",
    "Archus, Greatstaff of Antonidas",
    "Halion, Staff of Forgotten Love",
    "Tainted Twig of Nordrassil",
    "Warmace of Menethil",
    "Shadow's Edge",
    "Sister Svalna's Aether Staff",
    "Oxheart",
    "Hersir's Greatspear",
    "Shaft of Glacial Ice",
    "Abracadaver",
    "Mag'hari Chieftain's Staff",
    "Ramaladni's Blade of Culling",
    "Citadel Enforcer's Claymore",
    "Gluth's Fetching Knife",
    "Nightmare Ender^",
    "Zod's Repeating Longbow^",
    "Corpse-Impaling Spike^",
    "Fal'inrush, Defender of Quel'thalas",
    "Windrunner's Heartseeker",
    "Rowan's Rifle of Silver Bullets",
    "Dreamhunter's Carbine",
    "Lana'thel's Bloody Nail",
    "Stakethrower",
    "Wand of Ruby Claret",
    "Njorndar Bone Bow",
    "Heartpierce",
    "Scourgeborne Waraxe",
    "Bloodvenom Blade^",
    "Rib Spreader^",
    "Last Word^",
    "Lungbreaker",
    "Havoc's Call, Blade of Lordaeron Kings",
    "Mithrios, Bronzebeard's Legacy",
    "Heaven's Fall, Kryss of a Thousand Lies",
    "Stormfury, Black Blade of the Betrayer",
    "Troggbane, Axe of the Frostborne King",
    "Frost Giant's Cleaver",
    "Bone Warden's Splitter",
    "Bloodsipper",
    "Bonebreaker Scepter",
    "Gutbuster",
    "The Facelifter",
    "Flesh-Carving Scalpel",
    "Soulbreaker",
    "Keleseth's Seducer^",
    "Splintershard",
    "Rigormortis^",
    "Frozen Bonespike",
    "Trauma",
    "Black Bruise^",
    "Tel'thas, Dagger of the Blood King",
    "Bloodsurge, Kel'Thuzad's Blade of Agony",
    "Royal Scepter of Terenas II",
    "Pugius, Fist of Defiance",
    "Valius, Gavel of the Lightbringer",
    "Midnight Sun",
    "Trauma",
    "Frozen Bonespike",
    "Frost Needle",
    "Bleak Coldarra Carver",
    "Abomination Knuckles",
    "Lockjaw",
    "Totem of the Avalanche",
    "Totem of the Surging Sea",
    "Libram of Three Truths",
    "Sigil of the Hanged Man",
    "Sigil of the Vengeful Heart",
    "Idol of the Crying Moon",
    "Libram of Discord",
]


SEASON_8_MAINSET_EXTENDEDCOSTS = [
    lambda item: 2949 if item.InventoryType == InventoryType.HEAD else -1,
    # default for shoulders: 2948
    lambda item: 1431 if item.InventoryType == InventoryType.SHOULDER else -1,
    lambda item: 2952 if item.InventoryType in 
        (InventoryType.CHEST, InventoryType.ROBE) else -1,
    lambda item: 2953 if item.InventoryType == InventoryType.LEGS else -1,
    lambda item: 2954 if item.InventoryType == InventoryType.HANDS else -1,
]
SEASON_8_MAINSET_DISCOUNTED_EXTENDEDCOSTS = [
    lambda item: 2951 if item.InventoryType == InventoryType.HEAD else -1,
    # default for shoulders: 2948
    lambda item: 2356 if item.InventoryType == InventoryType.SHOULDER else -1,
    lambda item: 2954 if item.InventoryType in 
        (InventoryType.CHEST, InventoryType.ROBE) else -1,
    lambda item: 2962 if item.InventoryType == InventoryType.LEGS else -1,
    lambda item: 2958 if item.InventoryType == InventoryType.HANDS else -1,
]
SEASON_8_WEAPON_EXTENDEDCOSTS = [
    lambda item: 2386 if item.InventoryType == InventoryType.TWO_HAND else -1,
    lambda item: 2381 if item.InventoryType in
        (InventoryType.WEAPON, InventoryType.MAIN_HAND,
        InventoryType.RANGED_WEAPON, InventoryType.RANGED_RIGHT) else -1,
    lambda item: 2372 if item.InventoryType in
        (InventoryType.OFF_HAND, InventoryType.SHIELD, InventoryType.TOME) 
        else -1,
    lambda item: 2382 if item.InventoryType in
        (InventoryType.RELIC, InventoryType.THROWN) else -1
]


NPC_SPECS = [
    {
        "entry": (18015, 4234),
        "subname": "Profession Trainer",
        "ScriptName": "profession_vendor",
        "npcflag": NpcFlag.GOSSIP,
        "unit_flags": 2,
    },
    {
        "entry": (18014, 4177),
        "subname": "Reagents and General Goods",
        "npcflag": (NpcFlag.VENDOR + 
                    NpcFlag.REAGENT_VENDOR + 
                    NpcFlag.AMMO_VENDOR + 
                    NpcFlag.REPAIRER),
        "vendor_items": [
            "Portable Hole",
            "Star's Sorrow",
            "Shatter Rounds", 
            "Iceblade Arrow", 
            "Arcane Powder",
            "Ankh", 
            "Corpse Dust",
            "Light Feather", 
            "Starleaf Seed", 
            "Wild Spineleaf", 
            "Soul Shard",
            "Infernal Stone", 
            "Symbol of Kings",
            "Symbol of Divinity",
            "Devout Candle", 
            "Black Jelly",
            "Noggenfogger Elixir", 
            "Savory Deviate Delight", 
            "Crippling Poison", 
            "Mind-numbing Poison", 
            "Instant Poison IX", 
            "Deadly Poison IX", 
            "Wound Poison VII", 
            "Anesthetic Poison II"
        ],
        "unit_flags": 2,
    },
    {
        "entry": (18017, 1318),
        "subname": "Enchanter",
        "npcflag": NpcFlag.GOSSIP,
        "ScriptName": "enchant_npc",
        "unit_flags": 2,
    },
    {
        "entry": (18246, 34078),
        "subname": "Relentless Mainset",
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": SEASON_7_MAINSET,
        "unit_flags": 2,
    },
    {
        "entry": (18091, 34075),
        "subname": "Relentless Offsets",
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": ["Relentless Gladiator's " + i + "%" for i in [
            "Cuffs", "Cord", "Treads", "Armwraps", "Belt", "Boots", "Bracers",
            "Girdle", "Greaves", "Wristguards", "Waistguard", "Sabatons",
            "Pendant of%", "Band of%", "Cloak of%",
            "Idol of%", "Libram of%", "Totem of%", "Sigil of%",
        ]] + ["Medallion of the Alliance*", "Medallion of the Horde*"],
        "vendor_items_filters": [
            lambda item: item.ItemLevel == 226 if 
                item.InventoryType == InventoryType.TRINKET
                else True
        ],
        "unit_flags": 2,
    },
    {
        "entry": (16624, 1312),
        "subname": "Gems",
        "vendor_items": HIGH_LEVEL_GEM_NAMES,
        "unit_flags": 2,
    },
    {
        "entry": (25274, 34084),
        "subname": "Relentless Weapons",
        # "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": SEASON_7_WEAPONS,
        "unit_flags": 2,
    },
    {
        "entry": (18005, 34038),
        "subname": "ToC Offsets",
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": TOC_OFFSETS,
        "unit_flags": 2,
    },
    {
        "entry": (18006, 12788),
        "subname": "ToC Accessories",   
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,        
        "vendor_items": TOC_ACCESSORIES,
        "unit_flags": 2,
    },
    {
        "entry": (19694, 34063),
        "subname": "ToC Weapons",
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": TOC_WEAPONS,
        "unit_flags": 2,
    },
    {
        "entry": (35573, 35574),
        "subname": "Tier 9 Heroic",
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR,
        "vendor_items": ["% of Triumph"],
        "vendor_items_filters": [
            lambda item: item.ItemLevel == 258
        ],
        "unit_flags": 2,
    },
    {
        "entry": 33936,
        "subname": "Wrathful Mainset",
        "vendor_items": SEASON_8_MAINSET,
        "extended_cost_filters": SEASON_8_MAINSET_EXTENDEDCOSTS,
        "unit_flags": 2,
    },
    {
        "entry": 34095,
        "subname": "Wrathful Weapons",
        "vendor_items": SEASON_8_WEAPONS,
        "extended_cost_filters": SEASON_8_WEAPON_EXTENDEDCOSTS,
        "unit_flags": 2,
    },
    {
        "entry": (38840, 38181),
        "subname": "ICC Offsets",
        "vendor_items": ICC_HEROIC_OFFSETS,
        "extended_cost_filters": [lambda item: 2471],
        "unit_flags": 2,
    },
    {
        "entry": (37696, 37991),
        "subname": "ICC Accessories",
        "vendor_items": ICC_HEROIC_ACCESSORIES,
        "extended_cost_filters": [lambda item: 2471],
        "unit_flags": 2,
    },
    {
        "entry": (38284, 37999),
        "subname": "ICC Weapons",
        "vendor_items": ICC_HEROIC_WEAPONS_277,
        # "extended_cost_filters": [lambda item: 2471],
        "extended_cost_filters": SEASON_8_WEAPON_EXTENDEDCOSTS,
        "unit_flags": 2,
    },
    {
        "entry": 18581,
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR, # Original: 129
        "ScriptName": "twin_spire_vendor",
        "vendor_items": SEASON_8_MAINSET,
        "extended_cost_filters": SEASON_8_MAINSET_DISCOUNTED_EXTENDEDCOSTS,
        "unit_flags": 2,
    },
    {
        "entry": 18564,
        "npcflag": NpcFlag.GOSSIP + NpcFlag.VENDOR, # Original: 129
        "ScriptName": "twin_spire_vendor",
        "vendor_items": SEASON_8_MAINSET,
        "extended_cost_filters": SEASON_8_MAINSET_DISCOUNTED_EXTENDEDCOSTS,
        "unit_flags": 2,
    },
    {
        "entry": (18247, 34998),
        "npcflag": NpcFlag.GOSSIP,
        "ScriptName": "transmog_npc",
        "subname": "Transmogrificator",
        "unit_flags": 2,
    },
    {
        "entry": incr_custom_id("creature_template"),
        "npcflag": NpcFlag.GOSSIP,
        "ScriptName": "teleporter_npc",
        "name": "Convenient Portal",
        "unit_flags": 2 + 4 + 131072,
        # "modelid1": 30844,
        "IconName": "Taxi",
        "faction_A": 35,
        "faction_H": 35,
        "copy_from": 25552,
    }
]


def add_flag(npc, flag):
    if not npc.npcflag & flag == flag:
        npc.npcflag += flag


def merge_gear_prices(session):
    for item in get_items(session,
        HIGH_LEVEL_GEM_NAMES + 
        TOC_ACCESSORIES + 
        TOC_OFFSETS + 
        TOC_WEAPONS +
        ICC_HEROIC_OFFSETS + 
        ICC_HEROIC_ACCESSORIES +
        ICC_HEROIC_WEAPONS_277):
        item.BuyPrice = 0
        item.SellPrice = 1


def merge_zm_npctext(session):
    for faction in ("Alliance", "Horde"):
        npctext = session.merge(NpcText(ID=incr_custom_id("npctext"),
            text0_0="We are not in control of the Twin Spire ruins. Get out there "
                "and help capture the control points, soldier! "
                "For the " + faction + "!"))


def merge_all_npcs(session):
    for npc_spec in NPC_SPECS:
        items = None
        if "vendor_items" in npc_spec:
            items = npc_spec.pop("vendor_items")
        extended_cost_filters = npc_spec.pop("extended_cost_filters", [])
        vendor_items_filters = npc_spec.pop("vendor_items_filters", [])
        copy_from = npc_spec.pop("copy_from", False)
        entries = npc_spec.pop("entry")
        if not isinstance(entries, (tuple, list)):
            entries = [entries]
        for entry in entries:
            lookup_entry = copy_from if copy_from is not False else entry
            query = session.query(CreatureTemplate).\
                filter_by(entry=lookup_entry)
            npc = query.first()
            if npc:
                if copy_from is not False:
                    columns = [p.key for p in 
                        class_mapper(CreatureTemplate).iterate_properties]
                    for col_name in columns:
                        if col_name not in npc_spec:
                            npc_spec[col_name] = getattr(npc, col_name)
                    npc = CreatureTemplate(**npc_spec)
                    npc.entry = entry
                    session.merge(npc)
                    session.commit()
                else:
                    query.update(npc_spec)
            else:
                if copy_from == lookup_entry:
                    session.query(CreatureTemplate).filter_by(entry=entry).\
                        update(npc_spec)
                else:
                    print("no copy_from for {}".format(lookup_entry))
            if items:
                slot = 0
                session.query(NpcVendor).\
                    filter_by(entry=entry).\
                    delete()
                db_items = get_items(session, items)
                for item in db_items:
                    if (vendor_items_filters and 
                        not any([i(item) for i in vendor_items_filters])):
                        continue
                    cost = -1
                    for fn in extended_cost_filters:
                        cost = fn(item)
                        if cost != -1:
                            break
                    cost = None if cost == -1 else cost
                    session.merge(NpcVendor(entry=entry, item=item.entry, 
                        slot=slot, ExtendedCost=cost))
                    slot += 1


def merge(session):
    merge_gear_prices(session)
    merge_zm_npctext(session)
    merge_all_npcs(session)
    # merge_profession_trainers(session)
    # merge_general_goods_vendors(session)
    