import requests
import json

class TheBottingCompany:
    def __init__(self):
        self.token = ""
        self.webhooks = []
    
    def loadSecret(self):
        with open("secret.json", "r") as file:
            data = json.loads(file.read())
            self.token = data["chatGptToken"]
            self.webhooks = data["webhooks"]
            file.close()
    
    def ask(self, text):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + self.token,
        }
        data = { 
            "model": "text-davinci-003",
            "prompt": text,
            "max_tokens": 200,
            "temperature": 1.0,
        }
        response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
        output = response.json()
        
        return output["choices"][0]["text"]

if __name__ == "__main__":
    instance = TheBottingCompany()
    instance.loadSecret()
