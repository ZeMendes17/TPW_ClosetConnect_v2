"""
URL configuration for TPW_project_2_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # REST API
    path('ws/users', views.get_users),
    path('ws/user', views.get_user),
    path('ws/products', views.get_products),
    path('ws/followed_products', views.get_followed_products),
    path('ws/explore_products', views.get_explore_products),
    path('ws/remove_comment/<int:comment_id>', views.delete_comment),
    path('ws/add_comment', views.add_comment),
    path('ws/update_user/<int:user_id>', views.update_user),
    path('ws/update_profile/<int:user_id>', views.update_profile),
    path('ws/delete_user/<int:user_id>', views.delete_user),
    path('ws/favorites', views.get_favorites),
    path('ws/favorite_products/<int:user_id>', views.get_favorite_products),
    path('ws/add_favorite', views.add_favorite),
    path('ws/remove_favorite/<int:product_id>', views.remove_favorite),
    path('ws/user/followers/<int:user_id>', views.get_user_followers),
    path('ws/user/following/<int:user_id>', views.get_user_following),
    path('ws/followers/<int:user_id>', views.get_followers),
    path('ws/follow_user/<int:user_id>', views.follow_user),
    path('ws/unfollow_user/<int:user_id>', views.unfollow_user),
    path('ws/add_product_to_cart', views.post_item_cart),
    path('ws/delete_product/<int:product_id>', views.delete_product),
    path('ws/user/products/<int:user_id>', views.get_user_products),
    path('ws/user/sell/<int:product_id>', views.sell_product),
    path('ws/product/<int:product_id>', views.get_product),
    path('ws/product/favorites/<int:product_id>', views.get_product_favorites),
    path('ws/seller/<int:product_id>', views.seller),
    path('ws/update_product/<int:product_id>', views.update_product),
    path('ws/user/<int:user_id>', views.get_user_by_id),
    path('ws/delete_user/<int:user_id>', views.delete_user),
    path('ws/user/<str:username>', views.get_user_with_username),
    path('ws/user/comments/<int:user_id>', views.get_user_comments),
    path('ws/cart', views.get_cart),
    path('ws/update_cart', views.update_cart),
    path('ws/process_payment', views.post_order),
    path('ws/add_product', views.add_product),

    ## Authentication
    path('ws/register', views.registerREST),
    path('ws/login', views.loginREST),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
