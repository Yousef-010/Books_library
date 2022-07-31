from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('book_store/', BookListView.as_view(), name='book_list'),
    path('book_store/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('book_store/create/', BookCreateView.as_view(), name='book_create'),
    path('book_store/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('book_store/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]