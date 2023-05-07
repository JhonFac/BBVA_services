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
        """
        This function sends a POST request to create transactions using the provided payload and returns the
        response.
        
        :param getPayload: It is a variable that contains the data payload to be sent in the HTTP POST
        request to the specified URL. The contents of the payload depend on the specific API being used and
        the data required by the server to process the request
        :return: The function `create_transactions` is returning the `response` object.
        """

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
        """
        This function sends a GET request to retrieve a specific merchant transaction using its ID.
        
        :param IdTransaction: This is a parameter that represents the unique identifier of a transaction. It
        is used to retrieve information about a specific transaction from the API
        :return: the response object obtained from making a GET request to a specific URL with a given
        transaction ID and headers. The response object contains information about the transaction.
        """

        
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