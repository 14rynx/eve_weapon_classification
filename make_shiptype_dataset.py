import os
import shutil

n = 0

med_missiles = ['Rapid Light Missile Launcher II',  'Heavy Assault Missile Launcher II', 'Heavy Missile Launcher II']
med_energy = ['Heavy Pulse Laser II', 'Focused Medium Pulse Laser II', 'Quad Light Beam Laser II', 'Focused Medium Beam Laser II', 'Heavy Beam Laser II']
med_hybrid = []  #['Heavy Electron Blaster II', 'Heavy Ion Blaster II', 'Heavy Neutron Blaster II', 'Dual 150mm Railgun II', '200mm Raligun II', '250mm Railgun II']
med_projectile = ['Dual 180mm Autocannon II', '220mm Vulcan Autocannon I', '425mm Autocannon II', '650mm Artillery Cannon II', '720mm Howitzer Artillery II']


ships = [
    # CALDARI
    ("Caracal", "Caldari", "Caldari", med_missiles),
    ("Cerberus", "Caldari", "Caldari", med_missiles),
    ("Moa", "Caldari", "Caldari", med_hybrid),
    ("Onyx", "Caldari", "Caldari", med_missiles),
    ("Eagle", "Caldari", "Caldari", med_hybrid),
    ("Osprey", "Caldari", "Caldari", med_missiles),  # For ONI
    ("Rook", "Caldari", "Caldari", med_missiles),
    ("Falcon", "Caldari", "Caldari", med_missiles),
    ("Blackbird", "Caldari", "Caldari", med_missiles + med_hybrid),

    ("Ferox", "Caldari", "Caldari", med_hybrid),
    ("Vulture", "Caldari", "Caldari", med_hybrid),
    ("Drake", "Caldari", "Caldari", med_missiles),
    ("Nighthawk", "Caldari", "Caldari", med_missiles),

    # MINMATAR
    ("Scythe", "Minmatar", "Minmatar", med_projectile + med_missiles),  # For SFI
    ("Rupture", "Minmatar", "Minmatar", med_projectile),
    ("Broadsword", "Minmatar", "Minmatar", med_projectile),
    ("Muninn", "Minmatar", "Minmatar", med_projectile),
    ("Stabber", "Minmatar", "Minmatar", med_projectile),
    ("Vagabond", "Minmatar", "Minmatar", med_projectile),
    ("Bellicose", "Minmatar", "Minmatar", med_missiles),
    ("Rapier", "Minmatar", "Minmatar", med_missiles),
    ("Huginn", "Minmatar", "Minmatar", med_projectile),

    ("Hurricane", "Minmatar", "Minmatar", med_projectile),
    ("Sleipnir", "Minmatar", "Minmatar", med_projectile),
    ("Cyclone", "Minmatar", "Minmatar", med_missiles),
    ("Claymore", "Minmatar", "Minmatar", med_missiles),

    # AMARR
    ("Augoror", "Amarr", "Amarr", med_energy), # For Aug Navy
    ("Maller", "Amarr", "Amarr", med_energy),
    ("Sacrilege", "Amarr", "Amarr", med_missiles),
    ("Devoter", "Amarr", "Amarr", med_energy),
    ("Omen", "Amarr", "Amarr", med_energy),
    ("Zealot", "Amarr", "Amarr", med_energy),
    ("Arbitrator", "Amarr", "Amarr", med_missiles),
    ("Curse", "Amarr", "Amarr", med_missiles),
    ("Pilgrim", "Amarr", "Amarr", med_missiles),

    ("Harbinger", "Amarr", "Amarr", med_energy),
    ("Absolution", "Amarr", "Amarr", med_energy),
    ("Prophecy", "Amarr", "Amarr", med_missiles),
    ("Damnation", "Amarr", "Amarr", med_missiles),

    #  GALLENTE
    ("Exequror", "Gallente", "Gallente", med_hybrid),  # For ENI
    ("Thorax", "Gallente", "Gallente", med_hybrid),
    ("Deimos", "Gallente", "Gallente", med_hybrid),
    ("Vexor", "Gallente", "Gallente", med_hybrid),
    ("Ishtar", "Gallente", "Gallente", med_hybrid),
    ("Celestis", "Gallente", "Gallente", med_hybrid + med_missiles),
    ("Arazu", "Gallente", "Gallente", med_hybrid),
    ("Lachesis", "Gallente", "Gallente", med_hybrid),

    ("Brutix", "Gallente", "Gallente", med_hybrid),
    ("Myrmidon", "Gallente", "Gallente", med_hybrid),
    ("Astarte", "Gallente", "Gallente", med_hybrid),
    ("Eos", "Gallente", "Gallente", med_hybrid),

    # PIRATE FACTIONS
    ("Orthrus", "Mordus Legion", "Caldari", med_missiles),
    # ("Gila", "Guristas", "Caldari", med_missiles),
    ("Phantasm", "Sansha Nation", "Amarr", med_energy),
    ("Ashimmu", "Bloodraider", "Amarr", med_energy),
    ("Cynabal", "Angel", "Minmatar", med_projectile),
    ("Vigilant", "Serpentis", "Gallente", med_hybrid),

]

# for ship in ships:
    # os.makedirs(os.path.join("shiptybe_dataset", ship[0]))

for (subdir, _, files) in os.walk("data_normalized"):
    for file in files:
        n += 1
        name = os.path.join("shiptybe_dataset", ''.join(c for c in file.split(".")[0] if not c.isnumeric()), subdir.split("\\")[-1] + str(n) + ".png")
        shutil.copyfile(os.path.join(subdir, file), name)