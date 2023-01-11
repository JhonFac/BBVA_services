from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


# clase para listar
class list(APIView):

    # listar listar
    def get(self, *args):
        return Response({'mensaje':'listo'})

