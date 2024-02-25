# URL configuration guide and example imports for Django's URL routing
# Import the admin module to enable the admin interface
from django.contrib import admin
# Import path for routing and include for including other URLconfs
from django.urls import path, include

# urlpatterns: A list of URL patterns to route URLs to their corresponding views
urlpatterns = [
    # Route for Django's built-in admin interface. Accessible at '/admin/'
    path('admin/', admin.site.urls),

    # Include the blog app's URLs. This delegates URL handling for the path "" (root) to blog.urls
    path("", include("blog.urls")),

    # Route for django-summernote, a Django app for Summernote rich text editor. Accessible at '/summernote/'
    path('summernote/', include('django_summernote.urls')),

    # Include URLs from django-allauth for authentication handling. This includes routes for login, logout, and registration
    path("accounts/", include("allauth.urls")),
]
