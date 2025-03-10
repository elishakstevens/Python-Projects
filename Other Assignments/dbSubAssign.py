
#import sqlite3 database
import sqlite3

#tuple list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#Create a new database and open connection
conn = sqlite3.connect('dbSubAssign.db')
#Use cursor() method to modify database
cur = conn.cursor()

with conn:
    #Create a new table in the dbSubAssign database with 2 fields
    cur.execute("CREATE TABLE IF NOT EXISTS txt_files ( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                file_name TEXT \
                )")
    #Commit these changes to the database
    conn.commit()

#Iterate through fileList tuple above
for f in fileList:
    #Returns true if 'f' ends with .txt
    #Returns false if not
    if f.endswith('.txt'):
        with conn:
            #Inserting file into txt_files table if ends with .txt
            cur.execute("INSERT INTO txt_files(file_name) VALUES (?)", (f, ))
            #Commit change to database
            conn.commit
            #Print onto the console the file that was inserted into the table
            print("File: {}".format(f))

#Close connection
conn.close()
