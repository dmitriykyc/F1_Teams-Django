from django.urls import path

from . import views
from .api import views as views_api

urlpatterns = [
    path("", views.IndexCommand.as_view(), name='index_page'),
    path("<slug:slug>/", views.Command.as_view(), name='command'),
    path("review/<int:pk>/", views.AddReview.as_view(), name='add_review'),
    path("api_comands/", views_api.CommandsListView.as_view(), name='api_commands')
]
