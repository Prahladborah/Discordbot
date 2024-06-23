def get_leveling_info(level):
    leveling_areas = [
        (range(1, 34), "Nisel Mountain:Mountainside", "Shell Mask", "Keep grinding till you reach 34 to 36"),
        (range(34, 50), "Ancient Empress Tomb: Area 1", "Bone Dragonewt", "Level there till at least 50 or 56"),
        (range(50, 60), "Land Of Chaos", "Hidden boss: Forestia (normal/hard)", "Level there till 60"),
        (range(60, 69), "Land Of Chaos", "Hidden boss: Forestia (Nightmare)", "Level there till 69"),
        (range(70, 80), "Land Under Cultivation:Hill", "Masked Warrior (Hard)", "Level there till 74-76"),
        (range(80, 90), "Land Under Cultivation:Hill", "Masked Warrior (Nightmare)", "Level there till 90-94"),
        (range(90, 100), "Gravel Terrace:Jade Raptor (Nightmare) or Polde Ice Valley", "Don-Yeti", "Level till 100-104"),
        (range(100, 110), "Land Under Cultivation:Hill", "Masked Warrior (Ultimate)", "Level there till 110"),
        (range(110, 117), "Spring of Rebirth: Top", "Cerberus (Nightmare)", "Level there till 117"),
        (range(117, 130), "Magic Waste Site: Deepest Part", "Scrader (Ultimate)", "Level there till 130-132"),
        (range(130, 140), "Spring of Rebirth: Top", "Cerberus (Ultimate)", "Level there till 140"),
        (range(140, 148), "Dark Castle: Area 2", "Memecoleous (Ultimate)", "Level there till 148..Ask friends to help its a hellish boss if you are a rookie"),
        (range(148, 153), "Plastida: Deepest Part", "Imitator (Ultimate)", ""),
        (range(154, 158), "Small Demi Machina Factory Core", "Tyrant Machina (Ultimate)", ""),
        (range(158, 164), "Large Demi Machina Factory: Deepest Part", "Mozto Machina (Ultimate)", ""),
        (range(164, 175), "Ultimea Palace: Throne", "Venena Coenubia (Nightmare)", "Level there till 175-176"),
        (range(176, 184), "Droma Square", "Ultimate Machina (Ultimate)", "Level there till 184"),
        (range(184, 198), "Ultimea Palace: Throne", "Venena Coenubia (Ultimate)", "Level there till 194-198"),
        (range(198, 208), "Dark Dragon Shrine: Near the Top", "Finstern the Dark Dragon (Ultimate)", "Level there till 208"),
        (range(208, 220), "Labilans Sector: Square", "Kuzto (Ultimate)", "Level there till 220"),
        (range(220, 230), "Recetacula Sector: Depot Rooftop", "Gravicep (Ultimate) or better to do main quest", "Level there till 230"),
        (range(230, 245), "Arche Valley: Depths", "Arachnidemon (Ultimate)", "Better suggestion: do mq till 250"),
        (range(245, 260), "Operation Zone: Cockpit Area", "Trickster Dragon Mimyugon (Nightmare)", ""),
        (range(260, 285), "No info", "", "Do mq till 285"),
        (range(285, 295), "Boss colon", "", ""),
        (range(295, 300), "Boss colon", "", ""),
    ]

    for level_range, area, enemy, note in leveling_areas:
        if level in level_range:
            return f"Area: {area}\nEnemy: {enemy}\nNote: {note}"

    return None
