from django.conf.urls import url, include
from MySite import views
from django.contrib import admin
from .views import SuccessPageView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'MySite'

urlpatterns = [
	url(r'^$', views.HomePageView.as_view(),name='index'),
	url(r'^admin/', admin.site.urls),
	url(r'^about/$', views.AboutPageView.as_view(),name='about'),
	url(r'^contact/$', views.ContactPageView.as_view(),name='contact'),
	url(r'^ListProperty/$', views.ListPropertyPageView.as_view(),name='list_property'),
	url(r'^property/$', views.PropertyPageView.as_view(),name='property'),
	url(r'^search/$', views.SearchPageView.as_view(),name='search'),
	url(r'^success/$', views.SuccessPageView.as_view(),name='success'),
	url(r'^property/(?P<property_title>[-\w]+)/BookViewing/$', views.BookViewingPageView.as_view()),
	url(r'^property/(?P<property_title>[-\w]+)/$', views.PropertyPageView.as_view( )),
	url(r'^Latest/(?P<property_title>[-\w]+)/$', views.LatestPageView.as_view(),name='latest'),
	
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

