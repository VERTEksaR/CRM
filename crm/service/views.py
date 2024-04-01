import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer

from service.models import Service
from .serializers import ServiceSerializer


class ServicesAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    @staticmethod
    def get(request: Request) -> Response:
        services = list(Service.objects.all())

        if len(services) != 0:
            serializer = ServiceSerializer(instance=services, many=True)
            return Response({"services": serializer.data}, status=status.HTTP_200_OK, template_name='service/services.html')

        return Response(data='Список с услугами пуст', status=status.HTTP_200_OK, template_name='service/services.html')


@api_view(http_method_names=['get', 'post'])
def create_service(request: Request):
    if request.method == 'POST':
        print(request)
        info = json.loads(request.body)
        serializer = ServiceSerializer(data=info)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


class CreateServiceAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    @staticmethod
    def get(request: Request):
        return Response(status=status.HTTP_200_OK, template_name='service/service_create.html')

    @staticmethod
    def post(request: Request) -> Response:
        serializer = ServiceSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServiceAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    @staticmethod
    def get(request: Request, *args, **kwargs) -> Response:
        print(request.data)
        print(kwargs)
        service = Service.objects.get(id=kwargs['pk'])
        serializer = ServiceSerializer(instance=service)
        return Response({"service": serializer.data}, status=status.HTTP_200_OK, template_name='service/service_detail.html')

    @staticmethod
    def put(request: Request, *args, **kwargs) -> Response:
        service = Service.objects.get(id=kwargs['pk'])
        serializer = ServiceSerializer(instance=service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def delete(request: Request, *args, **kwargs) -> Response:
        service = Service.objects.get(id=kwargs['pk'])
        service.delete()
        return Response(status=status.HTTP_200_OK)
