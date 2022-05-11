from rest_framework import serializers
from v1.icreat.models import Icreat

class IcreatSerializers(serializers.ModelSerializer):

    # Date 포맷은 YYYY-MM-DD HH-MM-SS
    created_at = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')
    modified_at = serializers.DateTimeField(required=False, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        fields = '__all__'
        model = Icreat