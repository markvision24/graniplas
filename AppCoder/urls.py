from django.urls import path
from AppCoder import views
from django.urls import path
urlpatterns = [
    path('', views.inicio,name='Inicio'),
    path('cursos/', views.cursos,name='Cursos'),
    path('profesores/', views.profesores),
    path('cursosApi/', views.cursosapi),
    path('busquedaCurso/', views.buscarcurso,name='BuscarCurso'),
    path('buscar/', views.buscar),
    path('pinturas/', views.pinturas,name='Pintura'),
    path('empleadoss/', views.empleadoss,name='Empleado'),
    path('buscarempleado/', views.buscarempleado),
    path('productos/', views.productos, name='Productos'),
    path('leercursos/', views.leer_cursos, name='Leer_cursos'),
    path('crearcurso/', views.crear_curso, name='Crear_curso'),
    path('editarcurso/', views.editar_curso, name='Editar_curso'),
    path('eliminarcurso/', views.eliminar_curso, name='Eliminar_Curso'),
    path('buscarpintu/', views.buscarpintu),
    # terminos y condiciones
    
    
    path('terminos/', views.terminos, name="Terminos"),
    path('privacy/', views.privacy, name="Privacy"),
    
    #crud graniplas
    path('curso/list/', views.CursoList.as_view(),name='List'),
    path('curso/create/', views.CursoCreate.as_view(),name='New'),
    path('curso/edit/<pk>', views.CursoEdit.as_view(),name='Edit'),
    path('curso/detail/<pk>', views.CursoDetail.as_view(),name='Detail'),
    path('curso/delete/<pk>', views.CursoDelete.as_view(),name='Delete'),
    
    #Empleados
    path('empleados/list/', views.EmpleadosList.as_view(),name='List2'),
    path('empleados/create/', views.EmpleadosCreate.as_view(),name='New2'),
    path('empleados/edit/<pk>', views.EmpleadosEdit.as_view(),name='Edit2'),
    path('empleados/detail/<pk>', views.EmpleadosDetail.as_view(),name='Detail2'),
    path('empleados/delete/<pk>', views.EmpleadosDelete.as_view(),name='Delete2'),
    
    #Pintura
    path('pintura/list/', views.PinturaList.as_view(),name='List3'),
    path('pintura/create/', views.PinturaCreate.as_view(),name='New3'),
    path('pintura/edit/<pk>', views.PinturaEdit.as_view(),name='Edit3'),
    path('pintura/detail/<pk>', views.PinturaDetail.as_view(),name='Detail3'),
    path('pintura/delete/<pk>', views.PinturaDelete.as_view(),name='Delete3'),
    

]
