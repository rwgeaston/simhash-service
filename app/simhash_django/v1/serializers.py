from rest_framework import serializers

from simhash_django.models import (
    SimHash,
)


class SimHashSerializer(serializers.ModelSerializer):
    nearest_duplicate = serializers.SlugRelatedField(read_only=True, slug_field='guid')
    nearest_reverse = serializers.SlugRelatedField(many=True, read_only=True, slug_field='guid')

    class Meta:
        model = SimHash
        exclude = (
            'id',
        )
