"""
URL configuration for OurSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
    path("accounts/", include("accounts.urls")),  # TODO WHICH ONE
    # path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),

    # will change this to accounts
    path('admin/', admin.site.urls),  # the og admin site
    # path('accounts/', include('accounts.urls')),
    path('movies/', include('movies.urls')),
path('cart/', include('cart.urls')),
]
# added the last one, now it finally broke
# okay it looks like its working again

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
