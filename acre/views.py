from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Capitulo,  Dominio, Seccion, Wiki
from django.contrib.auth import authenticate, login, logout
import random
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def home(request):
    capitulo = Capitulo.objects.last()
    products = list(Capitulo.objects.all())

    products = random.sample(products, 3)
    contexto = {"Capitulo" : capitulo,
                "Random" : products
                }
    return render(request,'acre/home.html',contexto)

def reproductor(request, id):
    capitulo = Capitulo.objects.get(idcapitulo = id)
    
    
    contexto = {"Capitulo" : capitulo,
                
                }
    return render(request,'acre/reproductor.html',contexto)    

def hollowknight(request):
    
    return render(request,'acre/hollowknight.html')

def hollowplay(request):
    capitulo = Capitulo.objects.all().order_by('numcapitulo').filter(seccion_id= 3 , dominio_id = 1 )
    contexto = {"Capitulo" : capitulo}
    
    return render(request,'acre/allholplay.html', contexto)

def demons(request):
    capitulo = Capitulo.objects.all().order_by('numcapitulo').filter(dominio_id = 3 )
    contexto = {"Capitulo" : capitulo}
    
    return render(request,'acre/demonsoul.html', contexto)    

def hollowlore(request):
    capitulo = Capitulo.objects.all().order_by('numcapitulo').filter(seccion_id= 2 , dominio_id = 1 )
    contexto = {"Capitulo" : capitulo}
    
    return render(request,'acre/lorehollow.html', contexto)

def hollplay13(request, id):
    video = Capitulo.objects.get(idcapitulo = id)
    
    wiki = Wiki.objects.get(capitulo_id = id)
    contexto = {"Capitulo" : video,
                 "Wiki" : wiki,
               }
    return render (request,'acre/loreplay13.html', contexto)

def soulsborne(request):
    
    return render(request,'acre/soulsborne.html')

def inicioses(request):

    return render(request, 'acre/iniciosesion.html')    

def listado(request):
    capitulo = Capitulo.objects.all().order_by('numcapitulo')
    contexto = {"Capitulo" : capitulo}
    return render(request, 'acre/listadovideos.html', contexto)  

def lista_dominio(request):
    dominio = Dominio.objects.all()
    seccion = Seccion.objects.all()
    capitulo = Capitulo.objects.all()
    contexto = {"lista_dominio" : dominio , "lista_seccion" : seccion, "lista_cap" : capitulo}
    return render(request, 'acre/formregistro.html', contexto) 


def guardar_capitulo(request):
    n_idcap = request.POST['idcap']
    n_nomcap = request.POST['nomcapi']
    n_numcap = request.POST['numcap']
    n_urlcap = request.POST['urlcap']
    n_img = request.FILES['imagen']
    dominio_m = request.POST['dominio']
    dominio_m2 = Dominio.objects.get(iddominio = dominio_m) 
    seccion_m= request.POST['seccion']
    seccion_m2 = Seccion.objects.get(idseccion = seccion_m) 
    Capitulo.objects.create(idcapitulo = n_idcap, nomcapitulo = n_nomcap, numcapitulo = n_numcap, url = n_urlcap,imgcap = n_img, seccion = seccion_m2,  dominio = dominio_m2)
    
    #creo un mensaje para mostrar en mi formulario
    messages.success(request,'Capitulo Registrado Correctamente')

    return redirect('registro')


def eliminar_video(request, id):
    video = Capitulo.objects.get(idcapitulo = id) #obtengo la mascota a elminar
    video.delete() #elimino el objeto de la BD
    messages.success(request,'capitulo eliminado')

    return redirect('listado')

def modificar(request, id):
    video1 = Capitulo.objects.get(idcapitulo = id) #aqui obtenermos los datos completos de la mascota a modificar
    dominio1 = Dominio.objects.all() #obtengo todas las razas disponibles
    seccion1 = Seccion.objects.all()
    contexto = {
        "capitulo_modificar" : video1,
        "dominio_capitulo" : dominio1,
        "seccion_capitulo" : seccion1
    }

    return render(request,'acre/formulario_modificar.html', contexto)


def modificar_capitulo(request):
    n_idcap = request.POST['id']
    n_nomcap = request.POST['nombre']
    n_numcap = request.POST['numero']
    n_urlcap = request.POST['url']
    n_img = request.FILES['imag']
    dominio_m = request.POST['dominio']
    dominio_m2 = Dominio.objects.get(iddominio = dominio_m) 
    seccion_m= request.POST['seccion']
    seccion_m2 = Seccion.objects.get(idseccion = seccion_m)
    video_m= Capitulo.objects.get(idcapitulo = n_idcap)
    video_m.idcapitulo = n_idcap
    video_m.nomcapitulo = n_nomcap
    video_m.numcapitulo = n_numcap
    video_m.url = n_urlcap
    video_m.imgcap = n_img
    video_m.dominio = dominio_m2
    video_m.seccion = seccion_m2
    video_m.save() #update

    messages.success(request,'Capitulo Modificado')
    return redirect('listado')


def form_login(request):
    return render(request,'acre/iniciosesion.html')

def login_view(request):
    u = request.POST['username']
    c = request.POST['password']
    user = authenticate(username = u, password = c)

    if user is not None:
        if user.is_active:
            login(request,user)
            #messages.success(request,'Login Realizado')
            return redirect('home')
        else:
            messages.error(request,'Usuario inactivo')
    else:
        messages.error(request,'Usuario o Contraseña incorrecta')
    
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('home')
 

    