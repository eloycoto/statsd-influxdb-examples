from rest_framework import routers
from polls.views import QuestionViewSet, ChoicesViewSet

router = routers.DefaultRouter()
router.register('/question', QuestionViewSet)
router.register('/choices', ChoicesViewSet)
