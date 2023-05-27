from django.urls import path
from diary import views

urlpatterns = [
    path('', views.ContactListView.as_view(), name='diarylist'),
    path('new/', views.ContactCreateView.as_view(), name='newcontact'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(), name='updatecontact'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(), name='deletecontact'),
]
