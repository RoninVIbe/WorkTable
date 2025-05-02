from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from core.views import document_list, download_document
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', document_list, name='document_list'),
    path('documents/download/<int:document_id>/', download_document, name='download_document'),
    path('documents/download/<int:document_id>/', views.download_document, name='download_document'),
    path('', views.home, name='home'),
    path('projects/', views.project_list, name='project_list'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('documents/', views.document_list, name='document_list'),
    path('messages/', views.message_list, name='message_list'),
]

# добавляем медиафайлы
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
