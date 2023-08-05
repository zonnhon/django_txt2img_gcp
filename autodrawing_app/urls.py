from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.index, name='index'),
# ]
urlpatterns = [
    # path('<str:tag>', views.index, name='index'),
    path('', views.page1_view, name='news'),
    path('news', views.page1_view, name='news'),
    path('game', views.page2_view, name='game'),
    path('comic', views.page3_view, name='comic'),
    path('news/update_content/', views.update_content),
    path('game/update_content/', views.update_content),
    path('comic/update_content/', views.update_content),

]
