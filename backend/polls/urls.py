from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'polls'



# router = routers.DefaultRouter()
# router.register(r'questionlist', views.QuestionViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('questionlist/', views.question_list, name='question_list'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),

    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),


    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]