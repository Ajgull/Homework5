from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.FirstView.as_view(), name='first_view/'),

    path('produce_list_template_view/', views.ListView.as_view(), name='produce_list_template_view')
]
