import sqlite3


conn = sqlite3.connect('movies.db')


c = conn.cursor()

 

c.execute("""CREATE TABLE movies( 
	movie_name text,
	lead_actor text,
	actress text,
	year_of_release integer,
	director_name text
	)""")

c.execute("INSERT INTO movies VALUES('London Has Fallen' ,'Gerard Butler','Radha Mitchell','2016','Babak Najafi')")
c.execute("INSERT INTO movies VALUES('olympus has fallen' ,'Gerard Butler','Radha Mitchell','2013','Babak Najafi')")
c.execute("INSERT INTO movies VALUES('The fast and the furious','Vin Diesel','Micheal Rodriguez','2001','Rob Cohen')")
c.execute("INSERT INTO movies VALUES('Need for Speed (film) ','Aaron Paul','Imogen Poots','2014','	Scott Waugh')")

c.execute("SELECT * FROM movies ")



rows = c.fetchall()

for row in rows:
	print(row)
print("")
c.execute("SELECT * from movies WHERE lead_actor = 'Gerard Butler'") 
  

rows = c.fetchall()

for row in rows:
	print(row)

	

conn.commit()
