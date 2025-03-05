from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView 
from rest_framework_simplejwt import views as jwt_views
from .views import signup, user_login, home, adicionar_produto, editar_produto, excluir_produto, ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('accounts/login/', RedirectView.as_view(url='/login/', permanent=True)),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('', home, name='home'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('adicionar/', adicionar_produto, name='adicionar_produto'),
    path('editar/<int:id>/', editar_produto, name='editar_produto'),
    path('excluir/<int:id>/', excluir_produto, name='excluir_produto'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/', include(router.urls)),
]