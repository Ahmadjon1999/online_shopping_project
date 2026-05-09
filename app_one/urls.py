from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views



urlpatterns = [

    path(route="", view=views.home_page, name="index"),
    path(route="products/", view=views.products, name="products"),
    path(route="login/", view=views.user_login, name="login"),
    path(route="logout/", view=views.user_logout, name="logout"),
    path(route="registration/", view=views.register, name="register"),

    path(route="Cart-Products/", view=views.cart, name="cart"),
    path(route="profile_page/",  view=views.profile_info, name="profile"),
    path(route="delete_product/<int:product_id>/", view=views.delete_product, name="delete_product"),
    path(route="prod_detail/<uuid:product_id>/", view=views.prod_detail, name="prod_detail"),
    path(route="Transactions/", view=views.transaction, name="transactions"),
    path(route="buy/", view=views.buy, name="buy"),
    path(route="delete_transactions/", view=views.delete_transactions, name="delete_transactions")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

