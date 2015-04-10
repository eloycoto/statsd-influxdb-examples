from polls.models import Question, Choice
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
