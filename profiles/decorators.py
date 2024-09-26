from django.http import HttpResponseForbidden
from functools import wraps

def subscription_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and hasattr(request.user, 'subscription') and request.user.subscription.is_active():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden('Доступ запрещен: требуется активная подписка')
    return _wrapped_view
