from .models import User
from .serializers import UserModelSerializer
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import renderers


class UserCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [renderers.JSONRenderer, renderers.BrowsableAPIRenderer]
