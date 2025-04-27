### README ###
### This uses python exec rather than having to write your own parser
### This is dangerous because CPython with try to execute it no matter what, so any typo or normal text from the llm errors the program.
### The gpt should be told that its output will be passed into python exec, so it can run multiple at the same time and also be careful about syntax
### To save you the trouble of running ollama, just use the openai API, itll probably cost less than a dollar for this use case.
### FYI, the llm can pass in mulpile successive commands using ; or \n as a seperator.

### the optimal use for this would be run your laptop at the school on a phone hotspot. It would be either accessing your computer (tailscale, port forwarding) or the openai api
### The usb dongle for the drone would be in your laptop.

from codrone_edu.drone import Drone, pair, close, takeoff, land, emergency_stop, hover, avoid_wall, keep_distance, move_forward, move_backward, move_left, move_right, move_distance, turn_degree, turn_left, turn_right    # *
# This is so that the llm is limited to thesecouple functions so it doesn't overthink coding. you can let it have full access by changing the list to * and telling the llm all the funcs

import requests
import json

API_URL = "http://localhost:11434/api/generate"

drone = Drone()
drone.pair()
#I know nothing about the ollama api, so this requestAPI function can be changed to fix it.
####To fix it, it just needs to take in the user prompt as a string and return a string that contains the code the llm gives us. cannot be async request.
def requestAPI(prompt:str) -> str:
    data = {
        "model": "llama3",
        "prompt": prompt,
    }
    
    response = requests.post(API_URL, json=data)
    
    if response.status_code == 200:
        text = response.text
        split = text.splitlines()
        json = [json.loads(line) for line in split]
        
        for line in json:
            text = line["response"]
        print(text)
        return text
    else:
        print("Error:", response.status_code)
    
def validate(code:str) -> bool:
    try:
        compile(code, "<string>", "exec")
        return True
    except SyntaxError:
        print("This value didn't compile.", code)
        return False

def runCode(code:str) -> bool:
    if validate(code):
        print("Code to be ran:\n"+code)
        try:
            exec(code)
            return True
        except Exception as e:
            print("ERROR while executing", e)
            return False
    else:
        return False

def exiter(string:str):
    if string.lower().strip() == "exit":
        drone.emergency_stop()
        print("Goodbye")
        drone.close()
        exit()

command = ""
while True:
    # If you want to tell the llm the last command failed. The problem is that it might try to say sorry or fix the old code. You would have to discourage that in the system prompt.
    if command == "ERROR":
        command = input("What should it do? Type exit to exit")
        exiter(command)
        #command += "FYI, the last command broke, keep that in mind, dont fix it, but don't repeat the problem"
    else:
        command = input("What should it do? Type exit to exit")
        exiter(command)
    
    AI = requestAPI(command)
    
    worked = runCode(AI)
    
    if not worked:
        command = "ERROR"
    
drone.close()