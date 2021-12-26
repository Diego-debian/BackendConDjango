from django.conf.urls import url 
from restService import views 
 
""" Locals URLs """
urlpatterns = [ 
    url(r'^api/object$', views.object_list), #get y post object
    url(r'^api/feed$', views.feed_list), #get y post feed
    url(r'^api/author$', views.author_list), #get y post author
    url(r'^api/link$', views.link_list), #get y post link
    url(r'^api/result$', views.result_list), #get y post result
    url(r'^api/genre$', views.genre_list), #get y post genre
    url(r'^api/top50$', views.consultas_list), #Get top50 songs
    url(r'^api/search_autores$', views.author_search), #Get search authors
    url(r'^api/resultChange/(?P<pk>[0-9]+)$', views.cambiar_resultado), #Get, Put y Delete results by id
]