import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import urllib.request

moves = [
    (0, 30, 30),
    (1, 40, 1),
    (2, 50, 1),
    (3, 0, -80),
    (4, 50, 80),
    (5, 40, 1),
    (6, 50, 1),
    (7, 50, 1),
    (8, 50, 1),
    (9, 50, -50),
    (10, 50, 80),
    (11, 50, 1),
    (12, 50, 1),
    (13, 50, 1),
    (14, 0, 30),
    (15, 50, 30)
]

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

for item in med_missiles + med_energy + med_projectile:  # med_hybrid
    os.makedirs(f"raw\\{item}", exist_ok=True)

driver = webdriver.Chrome()
driver.maximize_window()

for ship, shader, booster, guns in ships:
    for gun in guns:
        driver.get("https://eve-nt.uk/designer/")

        # Get trough legal message
        elem = driver.find_element(By.XPATH, '/html/body')
        elem.send_keys(Keys.ESCAPE)

        # Get
        tags = driver.find_elements(By.CLASS_NAME, "header")

        # Load ship
        elem3 = driver.find_element(By.ID, "hull")
        sel = Select(elem3)
        sel.select_by_visible_text(ship)

        elem3 = driver.find_element(By.ID, "skin")
        sel = Select(elem3)
        sel.select_by_visible_text(shader)

        elem3 = driver.find_element(By.ID, "booster")
        sel = Select(elem3)
        sel.select_by_visible_text(booster)

        elem3 = driver.find_element(By.ID, "hull_load")
        elem3.click()

        # Open Fittings and load Guns
        tags[4].click()
        time.sleep(0.1)
        elem3 = driver.find_element(By.ID, "turret")
        sel = Select(elem3)
        sel.select_by_visible_text(gun)

        elem3 = driver.find_element(By.ID, "turrets_load")
        elem3.click()

        tags[4].click()

        time.sleep(4)

        # Open Export Window
        tags[5].click()

        for name, x, y in moves:
            time.sleep(0.1)
            # Move Screenshot to position
            action = ActionChains(driver)
            action.drag_and_drop_by_offset(elem, x, y).perform()

            # Download
            elem3 = driver.find_element(By.ID, "export")
            elem3.click()
            time.sleep(0.1)

            elem3 = driver.find_element(By.ID, "export_preview")
            link = elem3.get_property("src")
            urllib.request.urlretrieve(link, f"raw\\{gun}\\{ship}{name}.jpg")

            time.sleep(0.1)

            elem = driver.find_element(By.XPATH, '/html/body')
            elem.send_keys(Keys.ESCAPE)
        tags[5].click()


driver.close()