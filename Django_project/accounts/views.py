from django.http import JsonResponse
from django.contrib.auth import get_user_model

from rest_framework.generics import ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer

from dotenv import load_dotenv



load_dotenv(override=True)
User = get_user_model()


class UserList(ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer


class SampleView(GenericAPIView):
    permisson_classes = (IsAuthenticated, )

    def get(self, request):
        return JsonResponse({'action': 'get', 'message': 'success'})
    def post(self, request):
        return JsonResponse({'action': 'post', 'message': 'success'})