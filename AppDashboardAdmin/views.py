from django.shortcuts import render, get_object_or_404, redirect
from App.models import Articulo
from AppPedidos.models import Pedido, DetallePedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404

# Create your views here.

@login_required
def inicio(request):

    #!AGREGAR LA INFORMACION A LA PANTALLAD E INICIO
    productos = Articulo.objects.all()
    cantidad_Producto = productos.count()

    pedidos = Pedido.objects.all()
    cantidad_pedidos = pedidos.count()

    detalle = DetallePedido.objects.all()


    ctx = {
        'producto_cant':cantidad_Producto,
        'pedidos_cant': cantidad_pedidos,
        'pedidos':pedidos,
        'detalle':detalle,
    }

    return render(request,'dash_admin/inicio.html',ctx)

@login_required
def usuarios(request):

    usuarios = User.objects.all()

    ctx = {'usuarios':usuarios}

    return render (request,'dash_admin/usuarios.html',ctx)

@login_required
def productos(request):

    productos = Articulo.objects.all()
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(productos,5)
        productos = paginator.page(page)
    except:
        raise Http404

    ctx = {
        'entity':productos,
        'paginator': paginator
    }

    if request.method != 'POST':
        return render(request,'dash_admin/productos.html',ctx)
    else:
        imagen = request.FILES.get('imagen')
        nombre = request.POST['nombre']
        descipcion = request.POST['desc']
        seccion = request.POST['seccion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        objProducto = Articulo.objects.create(
            imagen = imagen,
            nombre = nombre,
            descripcion = descipcion,
            precio = precio,
            seccion = seccion,
            stock = stock,
        )
        objProducto.save()

        messages.success(request,'Producto creado correctamente')

        return redirect(to='admin_page:productos')

def user_edit(request, id):
    if id != "":
        producto = Articulo.objects.get(id = id)
        context = {"producto": producto}
        return render(request, "dash_admin/modificar.html", context)
    else:
        context = {"mensaje": "Error, usuario no encontrado"}
        return render(request, "dash_admin/productos.html", context)
    
@login_required
def modificar_producto(request,id):

    if request.method != 'POST':
        return render(request,'dash_admin/productos.html')
    else:


        imagen = request.FILES.get('imagen')
        nombre = request.POST['nombre']
        descipcion = request.POST['desc']
        seccion = request.POST['seccion']
        precio = request.POST['precio']
        stock = request.POST['stock']

        objProducto = get_object_or_404(Articulo, id=id)

        objProducto.imagen = imagen
        objProducto.nombre = nombre
        objProducto.descripcion = descipcion
        objProducto.precio = precio
        objProducto.seccion = seccion
        objProducto.stock = stock

        objProducto.save()

        productos = Articulo.objects.all()
        page = request.GET.get('page',1)

        try:
            paginator = Paginator(productos,5)
            productos = paginator.page(page)
        except:
            raise Http404

        ctx = {
            'entity':productos,
            'paginator': paginator
        }

        messages.success(request,'Modificado correctamente')

        return render(request,'dash_admin/productos.html',ctx)


@login_required
def eliminar(request,id):

    producto = get_object_or_404(Articulo, id=id)
    producto.delete()
    messages.success(request,'Eliminado correctamente')

    return redirect(to='admin_page:productos')

def eliminar_usuario(request,id):

    user = get_object_or_404(User, id=id)
    user.delete()
    messages.success(request,'Usuario eliminado correctamente')

    return redirect(to='admin_page:usuarios')


def salir(request):

    logout(request)

    return redirect('index')



        