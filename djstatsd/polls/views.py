from rest_framework import viewsets
from rest_framework.exceptions import ParseError
from polls.models import Question, Choice
from polls.serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.queryset


class ChoicesViewSet(viewsets.ModelViewSet):
    model = Choice
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
