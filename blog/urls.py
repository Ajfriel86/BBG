from . import views  # Import views module
from django.urls import path  # Import path function from django.urls module
from .views import *  # Import all views from views module
from .views import CustomSignupView  # Import CustomSignupView from views module
from django.conf import settings  # Import settings from django.conf module
# Import static function from django.conf.urls.static module
from django.conf.urls.static import static
# Import TemplateView from django.views.generic module
from django.views.generic import TemplateView
# Import comment_delete function from views module
from .views import comment_delete

# Define urlpatterns, a list of URL patterns
urlpatterns = [
    # Home page URL pattern mapped to CombinedHomeView
    path('', views.CombinedHomeView.as_view(), name='home'),
    # Contact page URL pattern mapped to contact_view
    path('contact/', contact_view, name='contact'),
    # Post detail page URL pattern with slug parameter mapped to PostDetail view
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    # URL pattern for liking a post with slug parameter mapped to PostLike view
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # URL pattern for deleting a comment with comment_id parameter mapped to comment_delete view
    path('comment/<int:comment_id>/delete/',
         comment_delete, name='comment_delete'),
    # URL pattern for user signup mapped to CustomSignupView
    path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    # URL pattern for registration success page mapped to registration_success template
    path('registration/success/', TemplateView.as_view(
        template_name='registration_success.html'), name='registration_success'),
]
