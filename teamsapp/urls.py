from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexCommand.as_view(), name='index_page'),
    path("<slug:slug>/", views.Command.as_view(), name='command'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review')
]
