from django.urls import path, include
from documents import views

urlpatterns = [
    path('documents/', views.document_list, name='document_list'),
    path('documents/<int:document_id>/', views.document_detail, name='document_detail'),
    path('documents/upload/', views.document_upload, name='document_upload'),
    path('documents/<int:document_id>/edit/', views.document_edit, name='document_edit'),
    path('documents/<int:document_id>/delete/', views.document_delete, name='document_delete'),
    path('notebook/', include('open_notebook.urls')),  # Added open-notebook URLs
]