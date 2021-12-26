import json
from django.shortcuts import render

from django.http.response import JsonResponse, HttpResponse
from restService.form import feedForm, objectForm
from restService.models import  *
from restService.serializers import  *
from django.core import serializers
from restService.form import *
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
from django.db import connection

      
    
"""Función para hacer get y post al objeto principal en la lista"""
@api_view(['GET', 'POST'])
def object_list(request):
    if request.method == 'GET':
        objects = Object.objects.all()        
        id = request.query_params.get('id', None)
        if id is not None:
            objects = objects.filter(title__icontains=id)        
        object_serializer = objectSerializer(objects, many=True)
        return JsonResponse(object_serializer.data, safe=False)
    elif request.method == 'POST':
        object_data = JSONParser().parse(request)
        object_serializer = objectSerializer(data=object_data)
        if object_serializer.is_valid():
            object_serializer.save()
            return JsonResponse(object_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(object_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

"""Función para hacer get y post a los feed"""
@api_view(['GET', 'POST'])
def feed_list(request):
    if request.method == 'GET':
        feeds = Feed.objects.all()        
        id = request.query_params.get('id', None)
        if id is not None:
            feeds = feeds.filter(title__icontains=id)
        feed_serializer = feedSerializer(feeds, many=True)
        return JsonResponse(feed_serializer.data, safe=False)
    elif request.method == 'POST':
        feed_data = JSONParser().parse(request)
        feed_serializer = feedSerializer(data=feed_data)
        if feed_serializer.is_valid():
            feed_serializer.save()
            return JsonResponse(feed_serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            print("Por aca")
        return JsonResponse(feed_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Función para hacer get y post a los author"""
@api_view(['GET', 'POST'])
def author_list(request):
    if request.method == 'GET':
        authors = Author.objects.all()        
        id = request.query_params.get('id', None)
        if id is not None:
            authors = authors.filter(title__icontains=id)        
        author_serializer = authorSerializer(authors, many=True)
        return JsonResponse(author_serializer.data, safe=False)
    elif request.method == 'POST':
        author_data = JSONParser().parse(request)
        author_serializer = authorSerializer(data=author_data)
        if author_serializer.is_valid():
            author_serializer.save()
            return JsonResponse(author_serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            print("Por aca")
        return JsonResponse(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Funnción para hacer get y post a los links"""
@api_view(['GET', 'POST'])
def link_list(request):
    if request.method == 'GET':
        links = Links.objects.all()        
        id = request.query_params.get('id', None)
        if id is not None:
            links = links.filter(title__icontains=id)        
        link_serializer = linksSerializer(links, many=True)
        return JsonResponse(link_serializer.data, safe=False)
    elif request.method == 'POST':
        link_data = JSONParser().parse(request)
        link_serializer = linksSerializer(data=link_data)
        if link_serializer.is_valid():
            link_serializer.save()
            return JsonResponse(link_serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            print("Por aca")
        return JsonResponse(link_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Función para hacer get y post a los results"""
@api_view(['GET', 'POST'])
def result_list(request):
    if request.method == 'GET':
        results = Results.objects.all()        
        id = request.query_params.get('id', None)
        if id is not None:
            results = results.filter(title__icontains=id)
        result_serializer = resultSerializer(results, many=True)
        return JsonResponse(result_serializer.data, safe=False)
    elif request.method == 'POST':
        result_data = JSONParser().parse(request)
        result_serializer = resultSerializer(data=result_data)
        if result_serializer.is_valid():
            result_serializer.save()
            return JsonResponse(result_serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            print("Por aca")
        return JsonResponse(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""Función para hacer get y post a los genres"""
@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genres.objects.raw('select * from restService_genres')
        id = request.query_params.get('id', None)
        if id is not None:
            genres = genres.filter(title__icontains=id)
        genre_serializer = genresSerializer(genres, many=True)
        return JsonResponse(genre_serializer.data, safe=False)
    elif request.method == 'POST':
        genre_data = JSONParser().parse(request)
        genre_serializer = genresSerializer(data=genre_data)
        if genre_serializer.is_valid():
            genre_serializer.save()
            return JsonResponse(genre_serializer.data, status=status.HTTP_201_CREATED) 
        else: 
            print("Por aca")
        return JsonResponse(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Función que devuelve las primeras 50 canciones"""
@api_view(['GET'])
def consultas_list(request):
    if request.method == 'GET':
        ress = Results.objects.all()[:50]    
        try:
            JSON = []
            for res in ress:
                misGeneros = Genres.objects.filter(results = res.id)
                contextoGL = []
                for m in misGeneros:
                    contextoGD = {"genreId":m.genreId, "name": m.name, "url": m.url }
                    contextoGL.append(contextoGD)
                contexto = {
                                #"feed": res.feed, 
                                "artistName": res.artistName, 
                                "id": res.id, 
                                "name": res.name,
                                "releaseDate": str(res.releaseDate),
                                "kind":res.kind,
                                "artistId": res.artistId, 
                                "artistUrl": res.artistUrl,
                                "contentAdvisoryRating": res.contentAdvisoryRating, 
                                "artworkUrl100": res.artworkUrl100, 
                                "genres": contextoGL,
                                "url": res.url
                                }

                JSON.append(contexto)
            print("-----------------",JSON,"----------------------")      
            return HttpResponse(JSON.parse, content_type="application/json")            


        except:
            print("Fallo")
            return HttpResponse(json.dumps(JSON), content_type="application/json")
        
   
"""Función que ordena por author"""
@api_view(['GET'])
def author_search(request):
    if request.method == 'GET':        
        try:            
            result = Results.objects.raw('select * from restService_results ORDER BY artistName')        
            Authores = []
            for i in result: 
                rs =  Results.objects.filter(artistName = str(i))
                #rs = Results.objects.raw('select * from restService_results WHERE artistName ='+ str(i) )            
                #print("----------->Author: ", i) 
                canciones = { "Author": i.artistName,
                    "tema": "" 
                }           
                cancion = []
                for r in rs:
                    cancion.append(r.name)
                canciones["tema"] = cancion
                Authores.append(canciones)
            OBJETOS = {"Busqueda_Autores": Authores}
            print(json.dumps(OBJETOS))
            return HttpResponse(json.dumps(OBJETOS), content_type="application/json")            
        except:
            print("Fallo")
            return HttpResponse(json.dumps(OBJETOS), content_type="application/json")


"""Función para hacer get y put y delete a los results"""
@api_view(['GET', 'PUT', 'DELETE'])
def cambiar_resultado(request, pk):
    try: 
        result = Results.objects.get(pk=pk) 
    except Results.DoesNotExist: 
        return JsonResponse({'message': 'The Results does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    #Get by ID
    if request.method == 'GET': 
        result_serializer = resultSerializer(result) 
        return JsonResponse(result_serializer.data) 
    #Put by ID
    elif request.method == 'PUT': 
        result_data = JSONParser().parse(request) 
        result_serializer = resultSerializer(result, data=result_data) 
        if result_serializer.is_valid(): 
            result_serializer.save() 
            return JsonResponse(result_serializer.data) 
        return JsonResponse(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    #Delete by ID
    elif request.method == 'DELETE': 
        result.delete() 
        return JsonResponse({'message': 'Results was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# url de la petición get
urlGet = 'index.html'
# url de la petición post
urlPost = 'crearResult.html'

""" --- Función que realiza un get sobre cada tabla del modelo. --- """
""" --- la función devuelve la petición, la url para la consulta --- """
""" --- y el contexto ---"""
def genericAll(request):
    object = Object.objects.all()
    feed = Feed.objects.all()
    author = Author.objects.all()
    links = Links.objects.all()
    results = Results.objects.all()
    genre = Genres.objects.all()
        
    contexto = {
        'object': object,
        'feed': feed,
        'author': author,
        'links': links,
        'results': results,
        'genre': genre,
    }
    print("----------imprime el contexto de la consulta-------", contexto  )
    return render(request, urlGet , contexto)



def genericNew(request):
    print(request)
    if (request.method== 'GET'):
        formsGet = {
            'form0': objectForm(),
            'form1': feedForm(),
            'form2': authorForm(),
            'form3': feedForm(),
            'form4': resultForm(),
            'form5': genreForm(),
        }
        contexto = formsGet.copy()

    elif (request.method== 'POST'):
        formsPost = {
            'form0': objectForm(request.POST),
            'form1': feedForm(request.POST),
            'form2': authorForm(request.POST),
            'form3': linksForm(request.POST),
            'form4': resultForm(request.POST),
            'form5': genreForm(request.POST),
        }
        contexto = formsPost.copy()
        for form in formsPost:          
            if formsPost[form].is_valid():
                try:
                    formsPost[form].save()
                    print("-- se guardo --", form)

                except:
                    print("-- No se pudo guardar --", form)


    
    return render(request, urlPost , contexto)