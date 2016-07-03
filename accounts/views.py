from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from djangorestframework_camel_case.render import CamelCaseJSONRenderer
from rest_framework import viewsets

from accounts.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    renderer_classes = (CamelCaseJSONRenderer,)
