from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import current_user, UserViewSet, GetUser, GetProduct
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('current_user/', current_user),
    path('', include(router.urls)),
    path('get-user/', GetUser.as_view(), name='getuser'),
    path('get-product/', GetProduct.as_view(), name='getproduct'),

]