from gpt4all import GPT4All
import os,pathlib, pyttsx3, json, re

engine = pyttsx3.init()
engine.setProperty('rate', 120)





path = pathlib.Path

current_Path = os.curdir

def printQ(respon):
	print(respon)
	engine.say(respon)
	engine.runAndWait()



printQ(f"working directory: {current_Path}" )

print(os.listdir(current_Path))

os.chdir("models")

model_Path = os.curdir
printQ(f"Models directory: {model_Path}" )

#list to store models
models = []

#FIND ALL MODELS
#"./llama/models/Qwen2-1.5B-Instruct.Q4_K_M.gguf"
for file in os.listdir(model_Path):
	if file.endswith(".gguf"):
		model_Name = file
		models.append(model_Name)



#SELECT A MODEL
#prompt a user to select a model 
printQ("Please, Select a model :")
for i, model in enumerate(models):
	print(f"{i+1}. {model}")
model_Num = input("Enter Model Number:")
model_Selected = models[int(model_Num) - 1]
printQ(f"model Selected : {model_Selected}", )



def replace_special_characters(input_text):
	pattern = re.compile(r'<\|im_start\|>|<\|im_end\|>|<\|im_start\||<\|im_start\|#*')
	examples = re.compile(r'Assistant')
	resp = re.compile(r'Human')
	output_text = pattern.sub('\n\r', input_text)
	output_text = examples.sub("   .\\\\rExample, you can try to say or ask ", output_text)
	output_text = resp.sub("You can answer:", output_text)
	return output_text.replace("#",".").replace("assistant"," ")


model = GPT4All(model_name = os.path.abspath(model_Selected)  , allow_download = False)
promt = "hello"
while not promt == "quit":
	with model.chat_session():
		promt = input("QNS:")
		response2 = model.generate(prompt=promt, temp=0)
		#jibu = model.current_chat_session[0]
		response21 = replace_special_characters(response2)
		printQ(response21)
