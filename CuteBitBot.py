import praw
import urllib.request
import time
import re
import sqlite3
import configparser

############################################################
config = configparser.ConfigParser()
config.read('SQLLITE.INI')
############################################################



print("Connecting...")
reddit = praw.Reddit('Wholesome')
subreddit = reddit.subreddit("test")
print("Success, retrieving threads.")
############################################################
listaAdjNegativos= ["soy feo","soy gordo","soy estupido","soy pusilánime","soy tonto","soy zoquete","soy bobo","soy aburrido","soy boludo",
"soy re feo","soy re gordo","soy re estupido","soy re tonto","soy re zoquete","soy re bobo","soy re aburrido","soy re boludo","soy un re perdedor",
"soy un feo","soy un estupido","soy un tonto","soy un zoquete","soy un bobo","soy un aburrido","soy un boludo","soy un pusilanime","soy un perdedor"]

footer="\n\n"+"***"+"\n\n"+"^I'm ^a ^bot *^bleep, ^bloop*"+"\n\n"+"PM "+config['Footer']['user']+"si tienes alguna queja o mejora ["+config['Footer']['github']+"]"


############################################################
patchArchivo =config["SQL_LiteDB"]["path"]

for submission in subreddit.hot(limit=20):	
	sub= reddit.submission(id=submission.id)
	for comment in sub.comments:		
		stringPost = str(comment.body).lower()		
		for adjNegativo in listaAdjNegativos:
			if stringPost.find(adjNegativo)!=-1:
				idComment = comment.id				
				print("--------------------------------\n")
				print(submission.id)
				print(comment.body)
				print("--------------------------------\n")
				conn = sqlite3.connect(patchArchivo)				
				cursor = conn.cursor()
				cursor.execute("SELECT * FROM IDrespuestas WHERE ID=?",(idComment,))
				entry = cursor.fetchone()
				if entry is None:
					print("Guardando: "+idComment)
					comment.reply("No digas eso! para mi eres genial!! \n\n [ Ojala esto te alegre un poco &hearts;&#x02605;&hearts;](https://i.redd.it/m44xcdnuq4611.jpg)"+footer)
					cursor.execute("INSERT INTO IDrespuestas(ID) VALUES (?)",(idComment,))
					conn.commit()
					conn.close()
				else: 
					print("Se encontro NO se guarda: "+idComment)
					conn.close()
			
