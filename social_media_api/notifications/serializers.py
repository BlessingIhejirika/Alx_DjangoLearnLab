from rest_framework import serializers
from .models import Notification
from accounts.serializers import UserSerializer
from posts.serializers import PostSerializer


class NotificationSerializer(serializers.ModelSerializer):
    recipient = UserSerializer(read_only=True)
    actor = UserSerializer(read_only=True)
    target = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            'id',
            'recipient',
            'actor',
            'verb',
            'is_read',
            'timestamp',
            'target',
        ]
        read_only_fields = fields

    def get_target(self, obj):
        if not obj.target:
            return None

        if obj.content_type.model == 'post':
            return {
                'type': 'post',
                'data': PostSerializer(obj.target).data
            }

        return {
            'type': obj.content_type.model,
            'id': obj.object_id
        }
