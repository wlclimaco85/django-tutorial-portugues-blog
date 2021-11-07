"""tutorialdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from blog.views import ParceiroViewSet, PostViewSet, StatusMaquinasViewSet, XmlsViewSet
from users.views import UserViewSet
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



router = routers.DefaultRouter()
#router.register(r'blog', PostViewSet)
router.register(r'blog', PostViewSet, basename="Blog")
router.register(r'user', ParceiroViewSet)
router.register(r'parceiro', ParceiroViewSet)
router.register(r'xml', XmlsViewSet )
router.register(r'statusMaquinas', ParceiroViewSet )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
urlpatterns = [
    path("admin/", admin.site.urls),
    #path("blog/", include("blog.urls", namespace="blog")),
     path('', include(router.urls))
]
"""