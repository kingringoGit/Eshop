from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from store.middlewares.auth import auth_middleware
urlpatterns = [
   path('',views.Index.as_view(), name='home'),
   path('signup',views.Signup.as_view(),name='signup'),
   path('Login',views.Login.as_view(),name='login'),
   path('logout',views.logout,name='logout'),
   path('cart',views.Cart.as_view(),name='cart'),
   path('check-out',views.CheckOut.as_view(),name='checkout'),
   path('orders',auth_middleware(views.OrderView.as_view()),name='orders')
]
if settings.DEBUG:
   urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)