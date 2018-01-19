from django.conf.urls import include, url
from core.views import *
from django.contrib import admin


urlpatterns = [
	url(r'^$', dashboard),
	url(r'^dashboard/', dashboard),
	url(r'^login', login),
	url(r'^logout/', logout),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^campus/novo', add_Campus, name = "add_Campus"),
	url(r'^professores$', professors_list),
	url(r'^professores/novo$', professors_add),
]