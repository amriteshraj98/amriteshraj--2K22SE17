from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recognition.urls')),  # Include the recognition app's URLs at the root
]
