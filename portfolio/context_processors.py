from django.conf import settings

def notificacao_ms(request):
    context = {
        'NOTIFICACAO_MS_URL': getattr(settings, 'NOTIFICACAO_MS_URL', 'http://127.0.0.1:8001'),
        'NOTIFICACAO_MS_API_KEY': getattr(settings, 'NOTIFICACAO_MS_API_KEY', ''),
    }
    # Se o usuário estiver logado no portfólio, envia o ID dele para a API
    if request.user.is_authenticated:
        context['NOTIFICACAO_USER_ID'] = request.user.id
    return context