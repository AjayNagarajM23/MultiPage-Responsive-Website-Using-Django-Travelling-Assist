from django.urls import path, include
from NammaUttaraKannada import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='index'),
                  path('index', views.index, name='index'),
                  path('about', views.about, name='about'),
                  path('gallery', views.gallery, name='gallery'),
                  path('signin', views.signin, name='signin'),
                  path('signup', views.signup, name='signup'),
                  path('book', views.book, name='book'),
                  path('contact', views.contact, name='contact')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
