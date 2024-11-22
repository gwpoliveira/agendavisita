from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings
from .models import Banner, SecaoEnsino, Projeto, Agendamento
from .forms import BannerForm, SecaoEnsinoForm, ProjetoForm, AgendamentoForm
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required  # Apenas usuários do staff podem acessar
def painel_controle(request):
    return render(request, 'painel_controle.html')
def landing_page(request):
    banner = Banner.objects.first()
    secoes_ensino = SecaoEnsino.objects.all()
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_sucesso')  # Redireciona para uma página de sucesso
    else:
        form = AgendamentoForm()

    context = {
        'banner': banner,
        'secoes_ensino': secoes_ensino,
        'projetos': projetos,
        'form': form,  # Inclui o formulário no contexto
    }
    return render(request, 'landing_page.html', context)

def agendar_visita(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento = form.save()
            # Envio de email de confirmação
            send_mail(
                'Confirmação de Agendamento',
                f"Olá {agendamento.nome}, seu agendamento foi confirmado para {agendamento.data} às {agendamento.hora}.",
                settings.DEFAULT_FROM_EMAIL,
                [agendamento.email],
            )
            return redirect('agendamento_sucesso')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento.html', {'form': form})

def agendamento_sucesso(request):
    return render(request, 'agendamento_sucesso.html')

# Views para Banners
@staff_member_required
def lista_banners(request):
    banners = Banner.objects.all()
    return render(request, 'lista_banners.html', {'banners': banners})
@staff_member_required
def adicionar_banner(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_banners')
    else:
        form = BannerForm()
    return render(request, 'form_banner.html', {'form': form, 'titulo': 'Adicionar Banner'})
@staff_member_required
def editar_banner(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=banner)
        if form.is_valid():
            form.save()
            return redirect('lista_banners')
    else:
        form = BannerForm(instance=banner)
    return render(request, 'form_banner.html', {'form': form, 'titulo': 'Editar Banner'})
@staff_member_required
def excluir_banner(request, pk):
    banner = get_object_or_404(Banner, pk=pk)
    if request.method == 'POST':
        banner.delete()
        return redirect('lista_banners')
    return render(request, 'banners/confirmar_exclusao.html', {'banner': banner})

# Views para Seções de Ensino
@staff_member_required
def lista_secoes(request):
    secoes = SecaoEnsino.objects.all()
    return render(request, 'lista_secoes.html', {'secoes': secoes})
@staff_member_required
def adicionar_secao(request):
    if request.method == 'POST':
        form = SecaoEnsinoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_secoes')
    else:
        form = SecaoEnsinoForm()
    return render(request, 'form_secao.html', {'form': form, 'titulo': 'Adicionar Seção'})
@staff_member_required
def editar_secao(request, pk):
    secao = get_object_or_404(SecaoEnsino, pk=pk)
    if request.method == 'POST':
        form = SecaoEnsinoForm(request.POST, request.FILES, instance=secao)
        if form.is_valid():
            form.save()
            return redirect('lista_secoes')
    else:
        form = SecaoEnsinoForm(instance=secao)
    return render(request, 'form_secao.html', {'form': form, 'titulo': 'Editar Seção'})
@staff_member_required
def excluir_secao(request, pk):
    secao = get_object_or_404(SecaoEnsino, pk=pk)
    if request.method == 'POST':
        secao.delete()
        return redirect('lista_secoes')
    return render(request, 'confirmar_exclusao.html', {'secao': secao})


# Views para Projetos
@staff_member_required
def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'lista_projetos.html', {'projetos': projetos})
@staff_member_required
def detalhes_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})
@staff_member_required
def adicionar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()
    return render(request, 'form_projeto.html', {'form': form, 'titulo': 'Adicionar Projeto'})
@staff_member_required
def editar_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'form_projeto.html', {'form': form, 'titulo': 'Editar Projeto'})
@staff_member_required
def excluir_projeto(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == 'POST':
        projeto.delete()
        return redirect('lista_projetos')
    return render(request, 'excluir_projeto.html', {'projeto': projeto})

# Views para Agendamentos
@staff_member_required
def lista_agendamentos(request):
    agendamentos = Agendamento.objects.all()
    return render(request, 'lista_agendamentos.html', {'agendamentos': agendamentos})
@staff_member_required
def adicionar_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')
    else:
        form = AgendamentoForm()
    return render(request, 'form_agendamento.html', {'form': form, 'titulo': 'Adicionar Agendamento'})

def agendar_visita(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_sucesso')
    else:
        form = AgendamentoForm()
    return render(request, 'nome_do_template.html', {'form': form})

@staff_member_required
def editar_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('lista_agendamentos')  # Redireciona para a lista de agendamentos
    else:
        form = AgendamentoForm(instance=agendamento)
    return render(request, 'editar_agendamento.html', {'form': form})
@staff_member_required
def excluir_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('lista_agendamentos')  # Redireciona para a lista de agendamentos
    return render(request, 'confirmar_exclusao.html', {'agendamento': agendamento})
