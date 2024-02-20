from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('home/page/', views.HomePageView.as_view(), name = 'home-page'),
    # path('detail/<int:id>/', views.details, name='detail')
    path('detail/page/<int:pk>/', views.DetailPageView.as_view(), name = 'detail'),
    path('search/', views.search, name = 'search'),
    path('contacts/create/', views.ContactCreateview.as_view(), name = 'create'),
    path('contact/update/<int:pk>/', views.ContactUpdateView.as_view(), name = 'update'),
    path('contact/delete/<int:pk>/', views.ContactDeleteView.as_view(), name = 'delete'),
    path('signup/', views.SignUpView.as_view(), name = 'signup')
]
