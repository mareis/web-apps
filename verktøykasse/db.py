import sqlite3

print("--- Starter oppsett av database ---")

# 1. Koble til (eller opprett) databasen
# Filen 'database.db' vil bli lagret i mappen du står i
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# 2. Slett gammel tabell hvis den finnes 
# (Dette gjør at vi kan kjøre scriptet flere ganger for å "restarte" databasen)
cursor.execute("DROP TABLE IF EXISTS spill")
print("Gammel tabell slettet (hvis den fantes).")

# 3. Lag tabellen på nytt
# Her bestemmer vi hvilke kolonner vi skal ha: id, tittel, plattform og år
cursor.execute("""
    CREATE TABLE spill (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tittel TEXT NOT NULL,
        plattform TEXT NOT NULL,
        aar INTEGER
    )
""")
print("Ny tabell 'spill' opprettet.")

# 4. Listen med spill vi vil legge inn (Tittel, Plattform, År)
spill_liste = [
    ('Minecraft', 'PC/Konsoll', 2011),
    ('Grand Theft Auto V', 'Multi', 2013),
    ('The Legend of Zelda: Breath of the Wild', 'Nintendo Switch', 2017),
    ('Fortnite', 'Multi', 2017),
    ('Among Us', 'Mobil/PC', 2018),
    ('Elden Ring', 'PC/Konsoll', 2022),
    ('Super Mario Odyssey', 'Nintendo Switch', 2017),
    ('FIFA 24', 'Multi', 2023),
    ('Roblox', 'PC/Mobil', 2006),
    ('Counter-Strike 2', 'PC', 2023),
    ('The Witcher 3', 'PC/Konsoll', 2015),
    ('Stardew Valley', 'Multi', 2016)
]

# 5. Sett inn alle spillene i databasen
# Vi bruker executemany for å sette inn hele listen på én gang.
# (?, ?, ?) er plassholdere for tittel, plattform og år.
cursor.executemany("INSERT INTO spill (tittel, plattform, aar) VALUES (?, ?, ?)", spill_liste)
print(f"La til {len(spill_liste)} spill i databasen.")

# 6. Lagre endringene permanent (commit) og lukk koblingen
connection.commit()
connection.close()

print("--- Ferdig! Filen 'database.db' er nå klar til bruk. ---")