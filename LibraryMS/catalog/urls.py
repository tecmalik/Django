from django.urls import path, include
from rest_framework import routers

from . import views
from .views import BookViewSet, BookImageViewSet

from rest_framework_nested import routers

router = routers.DefaultRouter()

# from google search drf nested router
router.register('books', BookViewSet, basename='books')

router.register('images', BookImageViewSet, basename='book-images')
print(router.urls)

book_images_router = routers.NestedDefaultRouter(router, 'books', lookup='book')

book_images_router.register('images', BookImageViewSet, basename='book-images')

urlpatterns = [

    path("",include(router.urls)),
    path("authors/<int:pk>/",views.AddAuthorView.as_view(), name ="add_author"),
    # path ("",views.get_books),
    # path ("add/authors/",views.add_author, name="add_author"),
    # path ("get/authors/",views.add_author, name="get_authors"),
    # path("update/authors/<int:pk>/",views.update_author, name="update_author"),
    # path ("delete/authors/<int:pk>/",views.delete_author, name="delete_author"),
    path("authors/",views.AddAuthorView.as_view(), name="get_authors_detail"),
    path("authors/<int:pk>/",views.GetUpdateDeleteAuthorView.as_view()),
    path("images/<int:pk>/", views.image_details, name="details-image"),

    path ("greet/<name>",views.greet),

    path("borrow-books/<int:pk>/", views.borrow_book, name="details-book"),
]

