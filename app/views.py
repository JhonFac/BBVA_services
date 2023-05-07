from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.transactions import TransactionsMethod
from rest_framework import viewsets

from .models import Manifest, PaymentMethods, Transaction
from .serializers import ManifestSerializer, PaymentMethodsSerializer, TransactionSerializer, CreateTransaccionSerializer

Tr=TransactionsMethod()


# This is a class for creating a transaction using the Django REST framework in Python.
class CreateTransaction(APIView):

    serializer_class = TransactionSerializer

    def post(self, request):

        pymentMethod_serializer = TransactionSerializer(data=request.data)
        if pymentMethod_serializer.is_valid():
            pymentMethod_serializer.save()
            return Response(pymentMethod_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pymentMethod_serializer.errors)


# This is a viewset class that handles creating transactions and returning a response.
class CreateTransactionViewSet(viewsets.ModelViewSet):

    serializer_class = CreateTransaccionSerializer

    def get_queryset(self):
        return Transaction.objects.all()

    def get(self, request):
      res=Tr.create_transactions()
      return HttpResponse({res.text})


# This is a Python class that retrieves transactions for a given order ID using an APIView.
class GetTransaction(APIView):

    def get(self, request, idOrder):
      res=Tr.get_transactions(idOrder)
      return HttpResponse({res.text})


# This is a viewset class for generating transactions with a queryset of all transactions and a
# serializer class for transactions.
class GenerateTransactionViewSet(viewsets.ModelViewSet):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


# This is a viewset class for a Manifest model that allows for listing and creating Manifest objects.
class ManifestViewSet(APIView):

    # serializer_class = ManifestSerializer

    # def get_queryset(self):
    #     return Manifest.objects.all()

    # # listar
    # def get(self, request):
    #   manifest = Manifest.objects.all()
    #   manifest_serializer = ManifestSerializer(manifest, many =True)
    #   return Response(manifest_serializer.data)


    def get(self, *args):
        return Response({
            
        {
  "name": "BBVA",
  "paymentMethods": [
    {
      "name": "Visa",
      "allowsSplit": "onCapture"
    },
    {
      "name": "American Express",
      "allowsSplit": "onCapture"
    },
    {
      "name": "Diners",
      "allowsSplit": "onCapture"
    },
    {
      "name": "Elo",
      "allowsSplit": "onCapture"
    },
    {
      "name": "Hipercard",
      "allowsSplit": "onCapture"
    },
    {
      "name": "Mastercard",
      "allowsSplit": "onCapture"
    },
    {
      "name": "BankInvoice",
      "allowsSplit": "onAuthorize"
    }
  ]
}

   })
    

# This is a Django REST framework viewset for managing payment methods, with a POST method for
# creating new payment methods.
class PaymentViewSet(viewsets.ModelViewSet):

    serializer_class = PaymentMethodsSerializer

    def get_queryset(self):
        return PaymentMethods.objects.all()

    # Create Pyments
    def post(self, request):

        pymentMethod_serializer = PaymentMethodsSerializer(data=request.data)
        if pymentMethod_serializer.is_valid():
            pymentMethod_serializer.save()
            return Response(pymentMethod_serializer.data, status=status.HTTP_201_CREATED)
        return Response(pymentMethod_serializer.errors)
