"""
URL configuration for conf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path,re_path
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.static import serve
from diplomat.views import set_language

from diplomat import views as diplomat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path("set_language/<str:language>", set_language, name="set-language"),

    # Chat API (til prefikssiz)
    path('api/chat/start/', diplomat_views.chat_start, name='chat_start'),
    path('api/chat/send/', diplomat_views.chat_send, name='chat_send'),
    path('api/chat/messages/', diplomat_views.chat_messages, name='chat_messages'),
    path('api/chat/admin-reply/', diplomat_views.chat_admin_reply, name='chat_admin_reply'),

    # Program Application API (til prefikssiz)
    path('api/program-application/', diplomat_views.program_application_submit, name='program_application_submit'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include('diplomat.urls')),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
)