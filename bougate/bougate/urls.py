from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bouapp.admin import user_site

# changing Dashboard and login Heading
admin.site.site_header = "BOU Items/Property Registration System"
admin.site.site_title = "Welcome to the BOU property registration System"
admin.site.index_title = "Welcome to this Portal"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_site.urls),
    path('', include('bouapp.urls'))
]
urlpatterns += staticfiles_urlpatterns()
