from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator

# Create your views here.
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


def listar(request):
    reservas = Reserva.objects.all().order_by("data")
    
    # Filtrar por nome, se fornecido
    nome = request.GET.get('nome')
    if nome:
        reservas = reservas.filter(nome__icontains=nome)
    
    # Filtrar por quitado ou não, se fornecido
    quitado = request.GET.get('quitado')
    if quitado:
        if quitado == 'quitado':
            reservas = reservas.filter(quitado=True)
        elif quitado == 'nao_quitado':
            reservas = reservas.filter(quitado=False)
    
    # Filtrar por valor do stand, se fornecido
    # Filtrar por valor do stand, se fornecido
    valor = request.GET.get('valor')
    if valor:
        reservas = reservas.filter(stand__valor=float(valor))

    
    # Filtrar por data da reserva, se fornecido
    data = request.GET.get('data')
    if data:
        reservas = reservas.filter(data=data)
    
    # Configurar a paginação
    paginator = Paginator(reservas, 5)  # 5 reservas por página
    page = request.GET.get('page')  # Obter o número da página
    reservas_paginadas = paginator.get_page(page)
    
    context = {'reservas': reservas_paginadas}
    return render(request, "reservas/listar.html", context)


def excluir(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect("listar")

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

def detalhes(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, "reservas/detalhes.html", context)