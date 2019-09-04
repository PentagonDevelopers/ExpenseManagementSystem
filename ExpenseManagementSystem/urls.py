from django.contrib import admin
from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from expense import views as expense_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', expense_views.home, name='home'),
    path('dashboard/', expense_views.dashboard, name='dashboard'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', user_views.register, name='register'),
    path('expense/new/', expense_views.ExpenseCreateView.as_view(template_name='expense/expense_form.html'),
         name='expense-create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
