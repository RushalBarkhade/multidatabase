from rest_framework.serializers import ModelSerializer
from website.models import Article

class ReadDBAPISerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class WriteDBAPISerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
