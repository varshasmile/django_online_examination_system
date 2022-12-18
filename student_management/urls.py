from django.urls import path, include
from .import views
from django.contrib import admin

urlpatterns = [
    path('', views.register, name='register'), # should be homepage
    path('login/', views.login, name='login'),
    path('home/', views.student_home, name='student_home'),
    path('logout/', views.logout_view, name='logout'),
    path('Questions/<int:qno>', views.exam_home, name='exam_home'),
    path('admin/', admin.site.urls),
    path('examadmin/',include('admin_dash.urls'),)
]