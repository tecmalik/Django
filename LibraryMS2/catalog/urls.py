from django.urls import path, include
from rest_framework import routers

from . import views
from .views import BookViewSet, BookImageViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet, basename='books')


router.register('images', BookImageViewSet, basename='book-images')
print(router.urls)

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
]

