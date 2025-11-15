from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Attractions, TicketTypes, Staff, SituationStage, Users
from django.utils import timezone
from datetime import timedelta
from django.contrib.sessions.backends.db import SessionStore

def page1(request):
    # Главная страница - все данные для page1.html
    small_attractions = Attractions.objects.filter(playground_type='small', activity_status=True)
    big_attractions = Attractions.objects.filter(playground_type='big', activity_status=True)
    
    # Берем реальные данные из базы для событий
    events_attractions = Attractions.objects.filter(activity_status=True)[:3]
    
    context = {
        # Основные счетчики
        'total_attractions': Attractions.objects.filter(activity_status=True).count(),
        'small_attractions_count': small_attractions.count(),
        'big_attractions_count': big_attractions.count(),
        
        # Популярные аттракционы для секции events
        'popular_attractions': Attractions.objects.filter(activity_status=True)[:3],
        
        # Данные для событий из базы данных
        'events': events_attractions,
        
        # Сотрудники для отображения
        'staff_members': Staff.objects.all()[:3],
        
        # Информация о пользователе
        'user': get_user_from_session(request),
    }
    return render(request, 'page1.html', context)

def page2(request):
    attractions = Attractions.objects.filter(activity_status=True)
    
    context = {
        'attractions': attractions,
        'attractions_count': attractions.count(),
        'attraction_examples': attractions[:3],
        'ticket_types': TicketTypes.objects.all(),
        'user': get_user_from_session(request),
    }
    return render(request, 'page2.html', context)

def page3(request):
    error_message = None
    success_message = None
    
    # Обработка входа
    if request.method == 'POST' and 'login' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                # Сохраняем пользователя в сессии
                request.session['user_id'] = user.id
                request.session['user_name'] = f"{user.name} {user.surname}"
                return redirect('page4')
            else:
                error_message = "Неверный пароль"
        except Users.DoesNotExist:
            error_message = "Пользователь не найден"
    
    # Обработка регистрации
    elif request.method == 'POST' and 'register' in request.POST:
        name = request.POST.get('reg_name')
        surname = request.POST.get('reg_surname')
        email = request.POST.get('reg_email')
        phone = request.POST.get('reg_phone')
        password = request.POST.get('reg_password')
        
        try:
            # Проверяем, нет ли уже пользователя с таким email
            if Users.objects.filter(email=email).exists():
                error_message = "Пользователь с таким email уже существует"
            else:
                # Создаем нового пользователя
                user = Users(
                    name=name,
                    surname=surname,
                    email=email,
                    phone_number=phone,
                    birth_date=timezone.now().date(),  # По умолчанию
                    created_at=timezone.now()
                )
                user.set_password(password)
                user.save()
                success_message = "Регистрация успешна! Теперь вы можете войти."
        except Exception as e:
            error_message = f"Ошибка при регистрации: {str(e)}"
    
    context = {
        'error_message': error_message,
        'success_message': success_message,
        'user': get_user_from_session(request),
    }
    return render(request, 'page3.html', context)

def page4(request):
    # Проверяем авторизацию
    user = get_user_from_session(request)
    if not user:
        return redirect('page3')
    
    # Страница покупки билетов
    ticket_types = TicketTypes.objects.all()
    
    # Обработка выбора билета
    selected_ticket_id = request.GET.get('ticket_id')
    selected_ticket = None
    
    if selected_ticket_id:
        try:
            selected_ticket = TicketTypes.objects.get(id=selected_ticket_id)
        except TicketTypes.DoesNotExist:
            selected_ticket = None
    
    context = {
        'ticket_types': ticket_types,
        'selected_ticket': selected_ticket,
        'user': user,
    }
    return render(request, 'page4.html', context)

def logout(request):
    # Выход пользователя
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['user_name']
    return redirect('page1')

# Вспомогательная функция для получения пользователя из сессии
def get_user_from_session(request):
    if 'user_id' in request.session:
        try:
            return Users.objects.get(id=request.session['user_id'])
        except Users.DoesNotExist:
            return None
    return None