from django.contrib import admin
from .models import Banner, SecaoEnsino, Projeto, Agendamento

class BannerAdmin(admin.ModelAdmin):
    list_display = ('texto_principal', 'texto_secundario', 'imagem')

class SecaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem')

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'imagem')

class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'data', 'hora', 'status')  # Remova 'unidade' aqui, se existia
    readonly_fields = ('data', 'hora')  # Remova 'unidade' aqui, se existia
    list_filter = ('status',)  # Remova 'unidade' aqui, se existia

admin.site.register(Banner, BannerAdmin)
admin.site.register(SecaoEnsino, SecaoEnsinoAdmin)
admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Agendamento, AgendamentoAdmin)
