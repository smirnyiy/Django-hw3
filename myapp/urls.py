from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail
from .views import my_view
from .views import TemplIf
from .views import view_for
from .views import index, about
from .views import user_order, order_full

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('user/<int:user_id>/', user_order, name='user_orders'),
    path('order/<int:order_id>/', order_full, name='order_full'),
]
