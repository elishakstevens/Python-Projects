import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", 'Mangalore', -5))

with sqlite3.connect('dbRoster.db') as connection:
    c = connection.cursor()
    c.execute("DROP TABLE IF EXISTS Roster")
    c.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES (?, ?, ?)", rosterValues)
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas' ")

    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
    for row in c.fetchall():
        name = row[0]
        iq = str(row[1])
        print(name + ', ' + iq)

connection.close()
