from django.urls import path
from .views import home, blog, author, delete_blog, delete_author

urlpatterns = [
    path('', home, name='homepage'),
    path('blog/', blog, name='blogs'),
    path('author/', author, name='author'),
    path('delete-blog/<int:id>/',delete_blog, name='deleteblog' ),
    path('delete-author/<int:id>/',delete_author, name='deleteauthor' ),

]
