from django.shortcuts import render
# from rest_framework.authtoken.models import Token
from profiles.models import user

from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes,renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.forms.models import model_to_dict

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def obtain_auth_token(request):
    username = request.data.get("username")
    password = request.data.get("password")
    print(username,password)
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user_cur = user.authenticate(username,password)
    if not user_cur:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user_cur)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


# token = Token.objects.create(user=...)
# print(token.key)
# Create your views here.

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def TeacherView(request):
	username = request.data.get("username")
	usr = user.objects.get(email='username')
	cnt = model_to_dict(usr)
	print(cnt)
	content = {'message': 'Hello, World!'}
	return Response(content)

def ClassHistory(request):
    return

def StudentHistory(request):
    return

def getImage(request):
    return

