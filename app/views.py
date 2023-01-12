from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# clase para listar
class list(APIView):

    # listar listar
    def get(self, request, data=""):
        return Response(data)
    #     return Response({
    # "paymentMethods": [
    #     "BankInvoice",
    #     "DebitCard",
    #     "Pix",
    #     "CreditCard",
    #     "Promissories",
    #     "Privatelabels",
    #     "Cobranded",
    #     "Cash"
    #         ]
    #     })


class Manifest(APIView):

    # listar listar
    def get(self, *args):
        return Response({
    "paymentMethods": [
      {
        "name": "Visa", 			
        "allowsSplit": "onCapture" 
      }, 
      {
         "name": "Pix", 			
        "allowsSplit": "disabled"
      },
      {
        "name": "MasterCard", 			
        "allowsSplit": "onCapture" 
      },
      {
        "name": "American Express", 			
        "allowsSplit": "onCapture" 
      },
      {
        "name": "BankInvoice", 			
        "allowsSplit": "onAuthorize" 
      },
      {
        "name": "Privatelabels", 			
        "allowsSplit": "disabled" 
      },
      {
        "name": "Promissories", 			
        "allowsSplit": "disabled" 
      }
    ]
   })



class Payment(APIView):

    def post(self, request):
        return Response(data=request.data)

