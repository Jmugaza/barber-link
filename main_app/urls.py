from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('barbers/', views.barbers_index, name='index'),
    path('barbers/<int:barber_id>/', views.barbers_detail, name='detail'),
    path('barbers/create/', views.BarberCreate.as_view(), name='barbers_create'),
    path('barbers/<int:pk>/update/', views.BarberUpdate.as_view(), name='barbers_update'),
    path('barbers/<int:pk>/delete/', views.BarberDelete.as_view(), name='barbers_delete'),
    path('reviews/', views.ReviewList.as_view(), name='reviews_index'),
    path('barbers/<int:barber_id>/reviews/create/', views.ReviewCreate.as_view(), name='reviews_create'),
    path('barbers/<int:barber_id>/reviews/<int:pk>/update/', views.ReviewUpdate.as_view(), name='reviews_update'),

]