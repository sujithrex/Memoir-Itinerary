#PRIME URLS


from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),   
    path('accounts/', include('registration.backends.default.urls')),
    path('', include('record.urls')), # new

]
