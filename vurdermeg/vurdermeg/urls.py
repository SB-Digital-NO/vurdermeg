from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baseapp.urls')),
    path('teacher/', include('teacherapp.urls')),
    path('student/', include('studentapp.urls'))
]
