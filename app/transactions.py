import os
import requests
from dotenv import load_dotenv
load_dotenv()

class TransactionsMethod():
    
    def __init__(self) -> None:
        
        self.baseUrl= os.getenv('URL_BASE')
        self.token= os.getenv('TOKEN')
        self.headers ={
        'Authorization': self.token,
        'x-mock-response-code': '200'
        }


    def create_transactions(self, getPayload):

        url = f"{self.baseUrl}/api/merchant-transactions"
        payload = getPayload 
        headers = self.headers
        response = requests.request("POST", url, headers=headers, data=payload)

        if 200 <= response.status_code <= 250:
            print(response.status_code)
            print(response.text)
        else:
            print(response.status_code)
        
        return response

    def get_transactions(self,IdTransaction):
        
        url = f"{self.baseUrl}/api/merchant-transactions/{IdTransaction}"

        payload={}
        headers = self.headers
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response)
        return response 

    # document why this method is empty
    def List_payment_methods(self):
        pass


t=TransactionsMethod()
t.get_transactions('f96ceae6-9d9a-4374-97af-f0b5efb64dd8')