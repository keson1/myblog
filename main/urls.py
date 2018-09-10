from django.urls import path, re_path
import main.views
from main.uploads import upload_image

urlpatterns = [
    path('', main.views.index, name='index'),
    path('detail/<int:blog_id>/', main.views.detail, name='detail'),
    path('category/', main.views.category, name='category'),
    path('category/<int:category_id>/', main.views.category_detail, name='category_detail'),
    path('words/', main.views.words, name='words'),
    path('search/', main.views.search, name='search'),
    path('archives/', main.views.archives, name='archives'),
    path('profile/', main.views.profile, name='profile'),
    path('admin/upload/<str:dir_name>/', upload_image, name='upload_image'),
]