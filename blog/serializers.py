from blog.models import post
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= post
        fields= ( 'title', 'text','created_date','published_date','image')