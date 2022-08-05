# RECORD APP LEVEL URLS


from django.urls import path
from .views import *
urlpatterns = [
  path('', homePageView, name='home'),
  path('allrecords', recordView, name='allrecords'),
  path('addnew', add_Record, name='addnew'),
  path('datefilter', dateRangeView, name='datefilter'),
  path('update_record/<str:pk>/', update_items, name="update_items"),
  path('delete_items/<str:pk>/', delete_items, name="delete_items"),
  path('view_items/<str:pk>/', view_items, name="view_items"),
  path('idea', ideaPageView, name='idea'),
]