from django.contrib import admin
from django.urls import path, include
from formapi.views import FormModelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', FormModelView.as_view())
]
