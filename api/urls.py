

from django.urls import path
from . import views
urlpatterns = [
    #path('', views.apiOverview, name='apiOverview'),
    path('book-list/', views.listBook, name='book-list'),
    path('book-view/<int:pk>', views.viewBook, name='book-view'),
    path('book-create/', views.createBook, name='book-create'),
    path('book-update/<int:pk>', views.updateBook, name='book-update'),
    path('book-delete/<int:pk>', views.deleteBook, name='book-delete'),
]
