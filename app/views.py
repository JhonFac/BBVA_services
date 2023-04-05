from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.transactions import TransactionsMethod
from rest_framework import viewsets

from .models import Payment
from .serializers import PaymentSerializer

Tr=TransactionsMethod()

class list(APIView):

    # obtener orden
    def get(self, request):
      return Response({
        "paymentMethods": [
          "BankInvoice",
          "DebitCard",
          "Pix",
          "CreditCard",
          "Promissories",
          "Privatelabels",
          "Cobranded",
          "Cash"
          ]
      })

class GetTransaction(APIView):

    # obtener orden
    def get(self, request, idOrder):
      print(idOrder)
      res=Tr.get_transactions(idOrder)
      return HttpResponse({res.text})

class Manifest(APIView):

    # listar
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


class PaymentViewSet(viewsets.ModelViewSet):

    serializer_class = PaymentSerializer
    def post(self, request):
        # Obtener los datos del JSON enviado en el body
        data = request.data

        # Serializar los datos
        serializer = PaymentSerializer(data=data)
        
        # Validar los datos
        if serializer.is_valid():
            # Guardar los datos en el modelo Payment
            payment = Payment(
                external_id=data['external_id'],
                callback_url=data['callback_url'],
                merchant_id=data['values']['merchant_id'],
                submerchant_id=data['values']['submerchant_id'],
                company_name=data['values']['company_name'],
                ruc=data['values']['ruc'],
                currency=data['values']['currency'],
                document_number=data['values']['document_number'],
                document_type=data['values']['document_type'],
                first_name=data['values']['first_name'],
                last_name=data['values']['last_name'],
                email=data['values']['email'],
                country_code=data['values']['country_code'],
                phone_number=data['values']['phone_number'],
                payment_concept=data['values']['payment_concept'],
                shipping_postal_code=data['values']['shipping_postal_code'],
                shipping_address=data['values']['shipping_address'],
                additional_data1=data['values']['additional_data1'],
                additional_data2=data['values']['additional_data2'],
                amount=data['amount']
            )
            payment.save()
            
            # Devolver una respuesta exitosa
            return Response({'message': 'Payment created successfully'}, status=status.HTTP_201_CREATED)
        else:
            # Devolver una respuesta con errores de validación
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)