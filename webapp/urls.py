from django.urls import path
from webapp.products import update_product, add_product
from webapp.views import product_list, product_detail
from webapp.products import delete_product
from webapp.products import confirm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', product_list, name='main'),
    path('product/', product_list),
    path('product/add/', add_product, name='create_view'),
    path('product/<int:pk>/detail', product_detail, name='product_detail'),
    path('product/<int:pk>/update/', update_product, name='update_view'),
    path('product/<int:pk>/delete/', delete_product, name='delete_product'),
    path('product/<int:pk>/delete/confirm', confirm, name='confirm')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
