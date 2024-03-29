from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.transactions import TransactionsMethod
from rest_framework import viewsets
import json
from .models import Manifest, PaymentMethods, Transaction
from .serializers import ManifestSerializer, PaymentMethodsSerializer, TransactionSerializer, CreateTransaccionSerializer
Tr=TransactionsMethod()


# This is a class for creating a transaction using the Django REST framework in Python.
class CreateTransaction(APIView):

    # serializer_class = TransactionSerializer
    # serializer_class = CreateTransaccionSerializer

    def get(self):
        return Transaction.objects.all()

    def post(self, request):

        # return HttpResponse({res.text})

        pymentMethod_serializer = TransactionSerializer(data=request.data)
        if pymentMethod_serializer.is_valid():

            data=request.data
            res=Tr.create_transactions(data)

            if 200 <= res.status_code <= 250:
                print(res.status_code)
                print(res.text)
                pymentMethod_serializer.save()
                response=json.loads(res.text)
                return Response(response, status=status.HTTP_201_CREATED)

            else:
                print(res.status_code)
                return Response(res.status_code, status=status.HTTP_201_CREATED)

        return Response(pymentMethod_serializer.errors)

# This is a viewset class that handles creating transactions and returning a response.
# class CreateTransactionViewSet(viewsets.ModelViewSet):

#     # serializer_class = CreateTransaccionSerializer
#     serializer_class = TransactionSerializer

#     def get_queryset(self):
#         return Transaction.objects.all()



# This is a Python class that retrieves transactions for a given order ID using an APIView.
class GetTransaction(APIView):

    def get(self, request, idOrder):
      print(idOrder)
      res=Tr.get_transactions(idOrder)
      return HttpResponse({res})


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
        res={"paymentMethods":[{"name":"Cuotealo","allowsSplit":"onAuthorize"},{"name":"PagoEfectivo","allowsSplit":"onAuthorize"}],"customFields":[{"name":"AccesKey","type":"text"},{"name":"SecretKey","type":"text"},{"name":"TradeID","type":"text"},{"name":"TradeName","type":"text"},{"name":"TradeEmail","type":"text"},{"name":"Country","type":"select","options":[{"text":"Perú","value":"PE"}]},{"name":"Currency","type":"select","options":[{"text":"Soles","value":"PEN"},{"text":"Dólares","value":"USD"}]}],"autoSettleDelay":{"minimum":"0","maximum":"720"}}
        return JsonResponse(res)


# This is a Django REST framework viewset for managing payment methods, with a POST method for
# creating new payment methods.
# class PaymentViewSet(viewsets.ModelViewSet):
class PaymentViewSet(APIView):

    def get(self, request):
        res={"paymentMethods":["Cuotealo","PagoEfectivo"]}
        return JsonResponse(res)

        # return HttpResponse({res})



    # serializer_class = PaymentMethodsSerializer

    # def get_queryset(self):
    #     return PaymentMethods.objects.all()

    # # Create Pyments
    # def post(self, request):

    #     pymentMethod_serializer = PaymentMethodsSerializer(data=request.data)
    #     if pymentMethod_serializer.is_valid():
    #         pymentMethod_serializer.save()
    #         return Response(pymentMethod_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(pymentMethod_serializer.errors)
