
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

if __name__ == "__main__":
    instance = TheBottingCompany()
    instance.loadSecret()