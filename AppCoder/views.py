from django.shortcuts import render
from django.http import HttpResponse

from AppCoder.models import Curso
from AppCoder.models import Pintura

from AppCoder.models import Empleados
from django.core import serializers

from AppCoder.forms import CursoFormulario
from AppCoder.forms import EmpleadosFormulario
from AppCoder.forms import PinturaFormulario



from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
def inicio(request):
    return render(request, 'AppCoder/inicio.html')



def terminos(request):
    return render(request, 'AppCoder/terminos.html')



def privacy(request):
    return render(request, 'AppCoder/privacy.html')

def buscar(request):
    codigo_views=request.GET['codigo']
    cursos_todos=Curso.objects.filter(codigo=codigo_views)
    return render(request,"AppCoder/resultadoCurso.html",{"codigo":codigo_views,"cursos":cursos_todos})

def buscarpintu(request):
    codigo_views=request.GET['codigo_2']
    cursoss_todoss=Pintura.objects.filter(codigo_2=codigo_views)
    return render(request,"AppCoder/resultadoPintura.html",{"codigo_2":codigo_views,"pinturas":cursoss_todoss})


def buscarempleado(request):
    Cedula_views=request.GET['Cedula']
    cursosss_todoss=Empleados.objects.filter(Cedula=Cedula_views)
    return render(request,"AppCoder/resultadoEmpleado.html",{"Cedula":Cedula_views,"empleadoss":cursosss_todoss})


def buscarcurso(request):
    return render(request, 'AppCoder/busquedaCurso.html')


def productos(request):
    return render(request, 'AppCoder/productos.html')

def cursos(request):
    if request.method == "POST":
            miFormulario=CursoFormulario(request.POST) #Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                    informacion=miFormulario.cleaned_data
                    curso = Curso(codigo=informacion["codigo"],
                    Nombre_Titanio=informacion["Nombre_Titanio"],
                    Titanio=informacion["Titanio"],
                    Nombre_Amarillo_Bayer=informacion["Nombre_Amarillo_Bayer"],
                    Amarillo_Bayer=informacion["Amarillo_Bayer"],
                    Nombre_Amarillo_Vivo=informacion["Nombre_Amarillo_Vivo"],
                    Amarillo_Vivo=informacion["Amarillo_Vivo"],
                    Nombre_Amarillo_AL90=informacion["Nombre_Amarillo_AL90"],
                    Amarillo_AL90=informacion["Amarillo_AL90"],   
                    Nombre_Azul=informacion["Nombre_Azul"],
                    Azul=informacion["Azul"],
                    Nombre_Rojo_Bayer=informacion["Nombre_Rojo_Bayer"],
                    Rojo_Bayer=informacion["Rojo_Bayer"],
                    Nombre_Rojo_Vivo=informacion["Nombre_Rojo_Vivo"],
                    Rojo_Vivo=informacion["Rojo_Vivo"],
                    Nombre_Negro=informacion["Nombre_Negro"],
                    Negro=informacion["Negro"],
                    Nombre_Tinta_Azul=informacion["Nombre_Tinta_Azul"],
                    Tinta_Azul=informacion["Tinta_Azul"],
                    Nombre_Tinta_Verde=informacion["Nombre_Tinta_Verde"],
                    Tinta_Verde=informacion["Tinta_Verde"],
                    Nombre_Tinta_Roja=informacion["Nombre_Tinta_Roja"],
                    Tinta_Roja=informacion["Tinta_Roja"],
                    Nombre_Tinta_Violeta=informacion["Nombre_Tinta_Violeta"],
                    Tinta_Violeta=informacion["Tinta_Violeta"],
                    Nombre_Tinta_Fucsia=informacion["Nombre_Tinta_Fucsia"],
                    Tinta_Fucsia=informacion["Tinta_Fucsia"],
                    Agua=informacion["Agua"],
                    Resina=informacion["Resina"],
                    Talco=informacion["Talco"],
                    Arena=informacion["Arena"],
                    Celulosa=informacion["Celulosa"],
                    Cuarzo=informacion["Cuarzo"],
                    AntiBacterial=informacion["AntiBacterial"],
                    AntiEspumante=informacion["AntiEspumante"]
                    )
                    curso.save()
                    return render(request, "AppCoder/inicio.html")
    else:
        miFormulario=CursoFormulario()

    return render(request, 'AppCoder/cursos.html',{"miFormulario":miFormulario})

def pinturas(request):
    if request.method == "POST":
            miFormulari=PinturaFormulario(request.POST) #Aqui me llega la informacion del html
            print(miFormulari)

            if miFormulari.is_valid:
                    informacion=miFormulari.cleaned_data
                    pintura = Pintura(codigo_2=informacion["codigo_2"],
                    Nombre_Titanio_2=informacion["Nombre_Titanio_2"],
                    Titanio_2=informacion["Titanio_2"],
                    Nombre_Amarillo_Bayer_2=informacion["Nombre_Amarillo_Bayer_2"],
                    Amarillo_Bayer_2=informacion["Amarillo_Bayer_2"],
                    Nombre_Amarillo_Vivo_2=informacion["Nombre_Amarillo_Vivo_2"],
                    Amarillo_Vivo_2=informacion["Amarillo_Vivo_2"],
                    Nombre_Amarillo_AL90_2=informacion["Nombre_Amarillo_AL90_2"],
                    Amarillo_AL90_2=informacion["Amarillo_AL90_2"],   
                    Nombre_Azul_2=informacion["Nombre_Azul_2"],
                    Azul_2=informacion["Azul_2"],
                    Nombre_Rojo_Bayer_2=informacion["Nombre_Rojo_Bayer_2"],
                    Rojo_Bayer_2=informacion["Rojo_Bayer_2"],
                    Nombre_Rojo_Vivo_2=informacion["Nombre_Rojo_Vivo_2"],
                    Rojo_Vivo_2=informacion["Rojo_Vivo_2"],
                    Nombre_Negro_2=informacion["Nombre_Negro_2"],
                    Negro_2=informacion["Negro_2"],
                    Nombre_Tinta_Azul_2=informacion["Nombre_Tinta_Azul_2"],
                    Tinta_Azul_2=informacion["Tinta_Azul_2"],
                    Nombre_Tinta_Verde_2=informacion["Nombre_Tinta_Verde_2"],
                    Tinta_Verde_2=informacion["Tinta_Verde_2"],
                    Nombre_Tinta_Roja_2=informacion["Nombre_Tinta_Roja_2"],
                    Tinta_Roja_2=informacion["Tinta_Roja_2"],
                    Nombre_Tinta_Violeta_2=informacion["Nombre_Tinta_Violeta_2"],
                    Tinta_Violeta_2=informacion["Tinta_Violeta_2"],
                    Nombre_Tinta_Fucsia_2=informacion["Nombre_Tinta_Fucsia_2"],
                    Tinta_Fucsia_2=informacion["Tinta_Fucsia_2"],
                    Agua_2=informacion["Agua_2"],
                    Resina_2=informacion["Resina_2"],
                    Talco_2=informacion["Talco_2"],
                    Celulosa_2=informacion["Celulosa_2"],
                    AntiBacterial_2=informacion["AntiBacterial_2"],
                    AntiEspumante_2=informacion["AntiEspumante_2"]
                    )
                    pintura.save()
                    return render(request, "AppCoder/inicio.html")
    else:
        miFormulari=PinturaFormulario()

    return render(request, 'AppCoder/pinturas.html',{"miFormulari":miFormulari})

def profesores(request):
    return HttpResponse('vista de profesores')
    
def cursosapi(request):
    cursos_todos=Curso.objects.all()
    return HttpResponse(serializers.serialize('json',cursos_todos))



def empleadoss(request):
    if request.method == "POST":
            miFormular=EmpleadosFormulario(request.POST) #Aqui me llega la informacion del html
            print(miFormular)

            if miFormular.is_valid:
                    informacion=miFormular.cleaned_data
                    empleados = Empleados(Cedula=informacion["Cedula"],
                    Nombres=informacion["Nombres"],
                    Apellidos=informacion["Apellidos"],
                    Cargo=informacion["Cargo"],
                    Año_Nacimiento=informacion["Año_Nacimiento"],
                    RH=informacion["RH"]
                    )
                    empleados.save()
                    return render(request, "AppCoder/inicio.html")
    else:
        miFormular=EmpleadosFormulario()

    return render(request, 'AppCoder/empleadoss.html',{"miFormular":miFormular})


def leer_cursos(request):
    cursos_all = Curso.objects.all()
    return HttpResponse(serializers.serialize('json', cursos_all))


def crear_curso(request):
    curso=Curso(codigo=199,                    
                    Nombre_Titanio='y69',
                    Titanio=2000,
                    Nombre_Amarillo_Bayer='y500',
                    Amarillo_Bayer=300,
                    Nombre_Amarillo_Vivo='y60',
                    Amarillo_Vivo=6,
                    Nombre_Amarillo_AL90='y30',
                    Amarillo_AL90=61,   
                    Nombre_Azul='b50',
                    Azul=20,
                    Nombre_Rojo_Bayer='r60',
                    Rojo_Bayer=1,
                    Nombre_Rojo_Vivo='r9',
                    Rojo_Vivo=60,
                    Nombre_Negro='n60',
                    Negro=7,
                    Nombre_Tinta_Azul='b65',
                    Tinta_Azul=20,
                    Nombre_Tinta_Verde='g99',
                    Tinta_Verde=2,
                    Nombre_Tinta_Roja='r30',
                    Tinta_Roja=92,
                    Nombre_Tinta_Violeta='v62',
                    Tinta_Violeta=3,
                    Nombre_Tinta_Fucsia='f30',
                    Tinta_Fucsia=10,
                    Agua=60,
                    Resina=3000,
                    Talco=200,
                    Arena=250,
                    Celulosa=600,
                    Cuarzo=60,
                    AntiBacterial=60,
                    AntiEspumante=20)
    curso.save()
    return HttpResponse(f'Curso {curso.codigo} ha sido creado')


def editar_curso(request):
    nombre_consulta= 'CursoTest'
    Curso.objects.get(Nombre_Titanio=nombre_consulta).update(Nombre_Titanio='NombrenuevoCursoTest')
    return HttpResponse(f'Curso {nombre_consulta} ha sido actualizado')


def eliminar_curso(request):
    nombre_nuevo='NombrenuevoCursoTest'
    curso= Curso.objects.get(Nombre_Titanio=nombre_nuevo)
    curso.delete()
    return HttpResponse(f'Curso {nombre_nuevo} ha sido eliminado')


#CRUD create read uptdate CRUD

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView


#Graniplas 

class CursoList(ListView):
    model = Curso
    template = 'AppCoder/curso_list.html'
    
class CursoCreate(CreateView):
    model = Curso
    fields= '__all__'
    success_url='/AppCoder/curso/list/'
    
class CursoEdit(UpdateView):
    model = Curso
    fields= '__all__'
    success_url='/AppCoder/curso/list/'
    
class CursoDetail(DetailView):
    model = Curso
    template_name='AppCoder/curso_detail.html'
    
    
class CursoDelete(DeleteView):
    model = Curso
    #fields= '__all__'
    success_url='/AppCoder/curso/list/'
    
    
#Empleados


class EmpleadosList(ListView):
    model = Empleados
    template = 'AppCoder/empleados_list.html'
    
class EmpleadosCreate(CreateView):
    model = Empleados
    fields= '__all__'
    success_url='/AppCoder/empleados/list/'
    
class EmpleadosEdit(UpdateView):
    model = Empleados
    fields= '__all__'
    success_url='/AppCoder/empleados/list/'
    
class EmpleadosDetail(DetailView):
    model = Empleados
    template_name='AppCoder/empleados_detail.html'
    
    
class EmpleadosDelete(DeleteView):
    model = Empleados
    #fields= '__all__'
    success_url='/AppCoder/empleados/list/'
    
    
#Pintura



class PinturaList(ListView):
    model = Pintura
    template = 'AppCoder/pintura_list.html'
    
class PinturaCreate(CreateView):
    model = Pintura
    fields= '__all__'
    success_url='/AppCoder/pintura/list/'
    
class PinturaEdit(UpdateView):
    model = Pintura
    fields= '__all__'
    success_url='/AppCoder/pintura/list/'
    
class PinturaDetail(DetailView):
    model = Pintura
    template_name='AppCoder/pintura_detail.html'
    
    
class PinturaDelete(DeleteView):
    model = Pintura
    #fields= '__all__'
    success_url='/AppCoder/pintura/list/'