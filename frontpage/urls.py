from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^howitworks/$', views.hiw, name='hiw'),
    url(r'^pricing/$', views.pricing, name='pricing'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    url(r'^upload/$', views.FileFieldView, name='FileFieldView'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^payment/$', views.payment_form, name='payment_form'),
    url(r'^checkout/$', views.checkout, name='checkout_page'),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)