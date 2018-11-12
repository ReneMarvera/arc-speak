import pyttsx3
import requests

def charlieSpeak(cad):

	engine = pyttsx3.init()

	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[0].id)

	engine.say(cad)
	engine.runAndWait()
	

str1 = input("Ingresa un texto: ")
resp = requests.post("http://209.97.143.4:8000/arclight/parsemessage", data = {
	"model_id":"5bd642c741d1701e640c938e",
	"message":str1
})

intent_name =  resp.json()['result']['intent']['name']
if(float(resp.json()['result']['intent']['confidence']) >= 0.80):
	if intent_name == "saludar":
		charlieSpeak("Hola amigo")
	elif intent_name == "despedirse":
		charlieSpeak("Adiós")
	elif intent_name == "agradecimiento":
		charlieSpeak("De nada, estoy para ayudarte.")
else:
	charlieSpeak("Lo siento, no te he entendido.")