from django.urls import path
from libraryapp.settings import STATIC_URL,DEBUG,STATIC_ROOT,MEDIA_ROOT,MEDIA_URL
from . import views
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name="index"),
    path('upload',views.upload,name="upload"),
    path('update/<int:pk>',views.update,name="update"),
    path('delete/<int:pk>',views.delete,name="delete"),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)