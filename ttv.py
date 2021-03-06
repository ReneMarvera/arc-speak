import pyttsx3
import requests
import speech_recognition as sr

def charlieSpeak(cad):

	engine = pyttsx3.init()

	rate = engine.getProperty('rate')
	engine.setProperty('rate', rate-60)

	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id)

	engine.say(cad)
	engine.runAndWait()

#str1 = input("Ingresa un texto: ")
text =  sr.RecognizeSpeech('myspeech.wav', 4)
print("\nDice: {}".format(text))

resp = requests.post("http://209.97.143.4:8000/arclight/parsemessage", data = {
	"model_id":"5bd642c741d1701e640c938e",
	"message":text
})

intent_name =  resp.json()['result']['intent']['name']
if(float(resp.json()['result']['intent']['confidence']) >= 0.80):
	print("Hay respuesta")
	if intent_name == "saludar":
		charlieSpeak("Hola amigo")
	elif intent_name == "despedirse":
		charlieSpeak("Adiós")
	elif intent_name == "agradecimiento":
		charlieSpeak("De nada, estoy para ayudarte.")
else:
	print("no hay respuesta")
	charlieSpeak("Lo siento, no te he entendido.")
