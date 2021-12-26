from rest_framework import serializers 
from restService.models import *
 
""" Modelo para serializar el objeto """
class objectSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Object
        fields = ( 'id', ) 

""" Modelo para serializar el feed """
class feedSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Feed
        fields = ( 'object', 'title', 'id', 'copyright', 'country', 'icon', 'updated' ) 


""" Modelo para serializar el author """
class authorSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Author
        fields = ('feed', 'name', 'url' ) 


""" Modelo para serializar el links """
class linksSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Links
        fields = ('feed', 'selfs') 


""" Modelo para serializar el result """
class resultSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Results
        fields = ( 'feed',  'artistName',
                 'id' , 'name' , 
                 'releaseDate','kind',
                  'artistId', 'artistUrl', 
                  'contentAdvisoryRating', 
                  'artworkUrl100', 'url'
                  ) 

""" Modelo para serializar el genre """
class genresSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Genres
        fields = ('results', 
                'genreId',
                'name',
                'url'
                ) 
