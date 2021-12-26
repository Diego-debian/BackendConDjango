from django.db import models


""" Tabla objeto """
class Object(models.Model):
    id = models.CharField(max_length=(100), primary_key=True, blank=False, null= False)
    class Meta:
        verbose_name = 'object'
        verbose_name_plural = 'objects'
        ordering = ['id']
    def __str__(self):
        return self.id

""" Tabla feed """
class Feed(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    title = models.CharField( 'title', max_length=(100), blank=False, null= False)
    id = models.CharField('id',  primary_key=True, max_length=(200))
    copyright = models.CharField('copyright', max_length=(200), blank=False, null= False)
    country = models.CharField('country', max_length=(100), blank=False, null= False)
    icon = models.CharField('icon', max_length=(200), blank=False, null= False)
    updated = models.CharField('updated', max_length=150, blank=False, null= False)
    class Meta:
        verbose_name = 'feed'
        verbose_name_plural = 'feeds'
        ordering = ['title']    
    def __str__(self):
        return self.title

""" Tabla Author """
class Author(models.Model):
    feed = models.ForeignKey(Feed, on_delete= models.CASCADE)
    name = models.CharField('name', max_length=(200), blank=False, null= False)
    url = models.CharField('url', max_length=(200), blank=False, null= False)
    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['id']
    def __str__(self):
        return self.name

""" Tabla links """
class Links(models.Model):
    feed = models.ForeignKey(Feed, on_delete= models.CASCADE)
    selfs = models.CharField(max_length=(200), blank=False, null= False)    
    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
        ordering = ['selfs']        

    def __str__(self):
        return str(self.selfs)

""" Tabla results """
class Results(models.Model):
    artistName =  models.CharField('artistName', max_length=(200), blank=False, null= False)
    id = models.IntegerField(primary_key=True, blank=False, null= False)
    name = models.CharField('name', max_length=(200), blank=False, null= False)
    releaseDate = models.DateField('releaseDate', blank=False, null= False)
    kind = models.CharField('kind', max_length=(200), blank=False, null= False)
    artistId = models.IntegerField('artistId',  blank=False, null= False)
    artistUrl = models.CharField('artistUrl', max_length=(200), blank=False, null= False)
    contentAdvisoryRating = models.CharField( max_length=(100), blank=True)
    artworkUrl100 = models.CharField('artworkUrl100', max_length=(200), blank=False, null= False)
    url = models.CharField('url', max_length=(200), blank=False, null= False)
    feed = models.ForeignKey(Feed, on_delete= models.CASCADE)
    class Meta:
        verbose_name = 'result'
        verbose_name_plural = 'results'
     #   ordering = ['id']        
    def __str__(self):
        return self.artistName

""" Tabla generos """
class Genres(models.Model):    
    genreId = models.IntegerField('genreId',  blank=False, null= False)
    name = models.CharField('name', max_length=(200), blank=False, null= False)
    url = models.CharField('url', max_length=(200), blank=False, null= False)    
    results = models.ManyToManyField(Results)
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['id']
        
    def __str__(self):
        return str(self.genreId)