import praw
import urllib.request
import time
import re


print("Connecting...")
reddit = praw.Reddit('Wholesome')
subreddit = reddit.subreddit("test")
print("Success, retrieving threads.")
############################################################
listaAdjNegativos= ["soy feo","soy gordo","soy estupido","soy pusilánime","soy tonto","soy zoquete","soy bobo","soy aburrido","soy boludo",
"soy re feo","soy re gordo","soy re estupido","soy re tonto","soy re zoquete","soy re bobo","soy re aburrido","soy re boludo","soy un re perdedor",
"soy un feo","soy un estupido","soy un tonto","soy un zoquete","soy un bobo","soy un aburrido","soy un boludo","soy un pusilanime","soy un perdedor"]

footer="\n\n"+"***"+"\n\n"+"^I'm ^a ^bot *^bleep, ^bloop*"+"\n\n"+"PM /u/'censored' si tienes alguna queja o mejora"
############################################################
patchArchivo ='censored'


for submission in subreddit.hot(limit=20):	
	sub= reddit.submission(id=submission.id)
	for comment in sub.comments:		
		stringPost = str(comment.body).lower()		
		for adjNegativo in listaAdjNegativos:
			if stringPost.find(adjNegativo)!=-1:				
				print("--------------------------------\n")
				print(submission.id)
				print(comment.body)
				print("--------------------------------\n")
				f=open(patchArchivo,"r")
				archivo= f.readlines()
				for linea in archivo:
					if linea.strip('\r\n') == comment.id:
						encontro=True
						break
					else:
						encontro=False
				if encontro!=True:
					f=open(patchArchivo,"a")
					f.write("\n"+comment.id)
					print("Guardando: "+comment.id)
					comment.reply("No digas eso! para mi eres genial!! \n\n [ Ojala esto te alegre un poco &hearts;&#x02605;&hearts;](https://i.imgur.com/KR1c22t.jpg)"+footer)
					f.close()
				else: 
					print("Se encontro NO se guarda: "+comment.id)
					f.close()
			
