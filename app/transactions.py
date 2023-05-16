import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

class TransactionsMethod():
    
    def __init__(self) -> None:
        
        self.baseUrl= os.getenv('URL_BASE')
        self.token= os.getenv('TOKEN')


    def create_transactions(self, getPayload):
        """
        This function sends a POST request to create transactions using the provided payload and returns the
        response.
        
        :param getPayload: It is a variable that contains the data payload to be sent in the HTTP POST
        request to the specified URL. The contents of the payload depend on the specific API being used and
        the data required by the server to process the request
        :return: The function `create_transactions` is returning the `response` object.
        """

        headers = {
        'Content-Type': 'application/json',
        'Authorization': self.token,
        'x-mock-response-code': '201'
        }

        url = f"{self.baseUrl}/api/merchant-transactions"
        payload =  json.dumps(getPayload)
        response = requests.request("POST", url, headers=headers, data=payload)


        
        return response


    def get_transactions(self,IdTransaction):
        """
        This function retrieves transaction information from a merchant API using a specified transaction ID
        and returns an error message if there is one.
        
        :param IdTransaction: The unique identifier of a transaction that you want to retrieve information
        for
        :return: an error message if there is an error in the response from the API, otherwise it is
        returning the response text.
        """

        url = f"{self.baseUrl}/api/merchant-transactions/{IdTransaction}"

        payload={}
        headers ={
        'Authorization': self.token
        }
        response = requests.request("GET", url, headers=headers, data=payload)

        try:
            res=json.loads(response.text)
            return res['error']['message']
        except Exception as e:
            print(e)
            return response.text

    # document why this method is empty
    def List_payment_methods(self):
        pass

