from django.urls import path
from .views import note_list, note_detail,query_notes



urlpatterns = [
    
    path('notes/', query_notes, name='query_notes'),  
    path('notes/',note_list,name='note_list'),
    path('notes/<int:pk>/', note_detail, name='note_detail'),
]
