from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import (
    FirstView,
    ProductsList,
    ProductDetail,
    ProductCreate,
    ProductUpdate,
    ProductDelete
)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', FirstView.as_view(), name='first_view'),
                  path('produce_shelf/', ProductsList.as_view(), name='produce_shelf'),
                  path('produce_detail/<int:pk>/', ProductDetail.as_view(), name='produce_detail'),
                  path('produce_create/', ProductCreate.as_view(), name='produce_create'),
                  path('product_delete/<int:pk>/', ProductDelete.as_view(), name='produce_delete'),
                  path('product_update/<int:pk>/', ProductUpdate.as_view(), name='produce_update'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
