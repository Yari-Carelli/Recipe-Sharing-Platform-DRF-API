from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:

        model = Event
        fields = [
            'id', 'owner', 'title', 'content', 'date', 'time',
            'location', 'price', 'event_link', 'created_at',
            'updated_at', 'is_owner', 'profile_id', 'profile_image',
        ]
