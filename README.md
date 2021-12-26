# BackendConDjango
Backend con Django
## INSTALACIÓN
<p> La aplicación esta probada en el sistema operativo linux.
abr una terminal o gitbash si esta esta en windows.</p>
<p> Escriba el comando </p>
<li> git clone https://github.com/Diego-debian/BackendConDjango.git </li>
<p> entre a la carpeta que clono de github </p>
<li> cd BackendConDjango </li>
<p> luego cree una instancia de virtualenv </p>
<li>  python3 -m venv venvRoot </li>
active la instancia
<li> source venvRoot/bin/activate </li>
<p> Una vez iniciada la instancia debe instalar el archivo de requerimientos. </p>
<li> python3 -m pip install -r requirements.txt </li>
<p>ingrese a la carpeta root </p>
<li> cd root </li>
<p>realice las migraciones de laas bases de datos de django </p>
<li>python3 manage.py makemigrations </li>
<li>python3 manage.py makemigrations restService </li>
<li>python3 manage.py migrate </li>
<li>python3 manage.py migrate restService </li>
<p> Una vez terminadas las migraciones estamos listos para  iniciar el servidor</p>
<li>python3 manage.py runserver 8080 </li>

<p><h4> Abra su navegador en la dirección http://localhost:8080</h4></p>

![image](https://user-images.githubusercontent.com/7892120/147413140-755df5ca-b49f-4bcc-94e2-146986be831d.png) 

## Pruebas rest con postman
### Prueba 1  
<li> localhost:8080/api/object</li>
<li> { "id": "feed"}  </li>
<p> imagen </p>
![image](https://user-images.githubusercontent.com/7892120/147414163-daf142fd-bf72-47e5-9a0b-5330bd7f31dc.png)

### Prueba 2

<li>  localhost:8080/api/feed</li>
<li> {
    "object": "feed", 
    "title": "Top Songs", 
    "id": "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json", 
    "copyright": "Copyright © 2021 Apple Inc. All rights reserved.", 
    "country": "us", 
    "icon": "https://www.apple.com/favicon.ico", 
    "updated": "Sun, 26 Dec 2021 15:59:01 +0000" }
</li>
<p> imagen </p>

![image](https://user-images.githubusercontent.com/7892120/147413874-d6666d4e-3da4-4bf5-9cba-fe2b97b9126c.png)

### Prueba 3

<li>   localhost:8080/api/author</li>
<li>{
    "feed": "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json", 
    "name": "Apple",
    "url": "https://www.apple.com/" }
</li>
<p> imagen </p>
![image](https://user-images.githubusercontent.com/7892120/147413967-e8b5fbbb-a72a-49a6-81ed-ad06af0b9096.png)

### Prueba 4

<li>    localhost:8080/api/link </li>
<li>{
    "feed": "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json", 
    "selfs": "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"}
</li>
<p> imagen </p>
![image](https://user-images.githubusercontent.com/7892120/147413989-52cee4be-11a4-41cd-bd09-1866edf404c8.png)

### Prueba 5

<li>     localhost:8080/api/result </li>
<li>{"feed": "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json", "artistName": "Mariah Carey", "id": "585972803", "name": "All I Want For Christmas Is You", "releaseDate": "1994-10-29", "kind": "songs", "artistId": "91853", "artistUrl": "https://music.apple.com/us/artist/mariah-carey/91853", "contentAdvisoryRating": "", "artworkUrl100": "https://is4-ssl.mzstatic.com/image/thumb/Music124/v4/c6/b7/27/c6b727f7-3a32-6b43-cee2-05bb71daf1cf/dj.itfmdeif.jpg/100x100bb.jpg", "url": "https://music.apple.com/us/album/all-i-want-for-christmas-is-you/585972750?i=585972803"}
</li>
<p> imagen </p>
![image](https://user-images.githubusercontent.com/7892120/147414024-7090921e-146d-4bc2-973e-ffc886d13d98.png)


### Prueba 6

<li>      localhost:8080/api/genre </li>
<li>{
    "results": ["585972803"], "genreId": "34", "name": "Music", "url": "https://itunes.apple.com/us/genre/id34" }
</li>
<p> imagen </p>

![image](https://user-images.githubusercontent.com/7892120/147414096-83ba8f40-ae37-47c3-947d-de5960251961.png)
