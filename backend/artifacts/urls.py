from django.urls import path
from . import views

urlpatterns = [
    # vue.js에서 id num을 준다
    path('<str:artifact_id>/', views.artifact_detail),
    path('<str:artifact_id>/like/', views.artifact_like),
    path('<str:artifact_id>/resemble/', views.artifact_resemble),
    # path('<str:artifact_id>/wordcloud/', views.wordcloud),
]