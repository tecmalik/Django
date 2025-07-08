from djoser.serializers import UserCreateSerializer as  BaseuserCreateSerializer
from rest_framework.generics import CreateAPIView


class UserCreateAPIView(CreateAPIView):
    class Meta(BaseuserCreateSerializer.Meta):
        fields = BaseuserCreateSerializer.Meta.fields + ['password','username','email','last_name','phone','first_name']