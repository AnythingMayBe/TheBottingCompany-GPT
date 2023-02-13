import requests
import json
import time

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

        failed = 0
        while True:
            time.sleep(2)
            response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=data)
            output = response.json()
            try:
                if output["choices"][0]["text"] != "":
                    break
                else:
                    failed += 1
                    if failed > 3:
                        return "Can you say it again please?"
            except KeyError: time.sleep(2)
        
        return output["choices"][0]["text"]

    def loop(self):
        base = "Hello"
        while True:
            for webhook in self.webhooks:
                base = self.ask(base)
                self.postWebhook(webhook, base)

    def postWebhook(self, webhook, message):
        req = requests.post(webhook, json={"content": message})




if __name__ == "__main__":
    instance = TheBottingCompany()
    instance.loadSecret()
    instance.loop()