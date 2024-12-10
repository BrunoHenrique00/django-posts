from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'title', 'content', 'created_datetime']
        read_only_fields = ['id', 'username', 'created_datetime']  # Prevent updates to these fields

    def update(self, instance, validated_data):
        # Only allow title and content to be updated
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
