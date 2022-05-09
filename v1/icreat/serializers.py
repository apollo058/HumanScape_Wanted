from rest_framework import serializers
from .models import Icreat

class IcreatSerializer(serializers.ModelSerializer):
    '''
    작성자 : 남기윤
    '''
    class Meta:
        model = Icreat
        fields = (
            "subject","sub_num","period","boundary",
            "remark","institute","trial","goal_research",
            "meddept"
            )


class IcreatDeleteSerializer(serializers.ModelSerializer):
    '''
    작성자 : 남기윤
    '''

    class Meta:
        model = Icreat
        fields = ("is_active",)

