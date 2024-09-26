from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from datetime import timedelta
from django.utils import timezone
from .models import Subscription
from .decorators import subscription_required

def activate_subscription(user, duration='month'):
    # Определяем дату окончания подписки
    now = timezone.now()
    if duration == 'month':
        end_date = now + timedelta(days=30)
    elif duration == 'year':
        end_date = now + timedelta(days=365)

    # Создаем или обновляем подписку
    if hasattr(user, 'subscription'):
        user.subscription.end_date = end_date
        user.subscription.save()
    else:
        Subscription.objects.create(user=user, end_date=end_date)

@login_required()
def profile_info(request):
    # Получаем связанный профиль пользователя
    user_profile = request.user.profile  # Получаем профиль
    user = request.user  # Получаем объект пользователя
    context = {
        'user_info': user,  # Передаем объект `User`
        'profile': user_profile,  # Отдельно передаем объект `Profile`
    }
    return render(request, 'profiles/profile.html', context)

@subscription_required
def premium_view(request):
    return render(request, 'GOS.html')

