from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/users/login')
def cadastro(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ReservaForm()
    context = {'form': form}
    return render(request, 'reservas/cadastro.html', context)

@login_required(login_url='/users/login')
def listar(request):
    reservas = Reserva.objects.all().order_by("data")
   
    nome = request.GET.get('nome')
    quitado = request.GET.get('quitado')
    valor = request.GET.get('valor')
    data = request.GET.get('data')
    
    # filtar nomes
    if nome:
        reservas = reservas.filter(nome__icontains=nome)
    
    # filtra o status da reserva
    if quitado:
        if quitado == 'quitado':
            reservas = reservas.filter(quitado=True)
        elif quitado == 'nao_quitado':
            reservas = reservas.filter(quitado=False)
    
    # filtrar o valor do stand
    if valor:
        reservas = reservas.filter(stand__valor=float(valor))

    
    # filtrar data da reserva
    if data:
        reservas = reservas.filter(data=data)
    
    # paginação
    p = Paginator(reservas, 5)  # 5 reservas por página
    page = request.GET.get('page')  # Obter o número da página
    r_paginadas = p.get_page(page)
    
    context = {'reservas': r_paginadas}
    return render(request, "reservas/listar.html", context)


@login_required(login_url='/users/login')
def excluir(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("listar")


@login_required(login_url='/users/login')
def atualizar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    
    if request.method == "POST":
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect("listar")
    else:
        form = ReservaForm(instance=reserva)
    
    context = {'form': form, 
               'reserva': reserva}
    return render(request, "reservas/cadastro.html", context)


@login_required(login_url='/users/login')
def detalhes(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, "reservas/detalhes.html", context)