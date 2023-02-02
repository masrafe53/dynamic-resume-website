from . import views
from django.urls import path
from .views import work
from .views import blog
from .views import home


urlpatterns = [
    path('',views.home,name = 'home'),
    path('blog/',views.blog,name = 'blog'),
    path('work/<int:id>',views.work,name = 'work'),
    path('service/,<int:id>',views.service,name='service'),

]