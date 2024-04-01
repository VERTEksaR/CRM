from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from adv_company.models import AdvCompany
from .serializers import AdvSerializer


class AdvAPIView(APIView):
    @staticmethod
    def get(request: Request) -> Response:
        companies = list(AdvCompany.objects.prefetch_related('service'))

        if len(companies) != 0:
            serializer = AdvSerializer(instance=companies, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        return Response(data='Список с компаниями пуст', status=status.HTTP_200_OK)

    @staticmethod
    def post(request: Request) -> Response:
        serializer = AdvSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OneAdvAPIView(APIView):
    @staticmethod
    def get(request: Request, *args, **kwargs) -> Response:
        company = AdvCompany.objects.get(id=kwargs['id'])
        serializer = AdvSerializer(instance=company)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request: Request, *args, **kwargs) -> Response:
        company = AdvCompany.objects.get(id=kwargs['id'])
        serializer = AdvSerializer(instance=company, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request: Request, *args, **kwargs) -> Response:
        company = AdvCompany.objects.get(id=kwargs['id'])
        company.delete()
        return Response(status=status.HTTP_200_OK)
