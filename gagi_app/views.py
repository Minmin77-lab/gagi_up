from django.shortcuts import render
from .models import Attractions, TicketTypes, Staff, SituationStage
from django.utils import timezone
from datetime import timedelta

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
    }
    return render(request, 'page1.html', context)

def page2(request):
    # Малая площадка
    small_attractions = Attractions.objects.filter(playground_type='small', activity_status=True)
    
    context = {
        'attractions': small_attractions,
        'attractions_count': small_attractions.count(),
        'attraction_examples': small_attractions[:3],  # Берем первые 3 аттракциона из базы
        'ticket_types': TicketTypes.objects.all(),
    }
    return render(request, 'page2.html', context)

def page3(request):
    # Большая площадка  
    big_attractions = Attractions.objects.filter(playground_type='big', activity_status=True)
    
    context = {
        'attractions': big_attractions,
        'attractions_count': big_attractions.count(),
        'attraction_examples': big_attractions[:3],  # Берем первые 3 аттракциона из базы
        'ticket_types': TicketTypes.objects.all(),
    }
    return render(request, 'page3.html', context)

def page4(request):
    # Страница покупки билетов
    ticket_types = TicketTypes.objects.all()
    
    # Создаем данные для билетов на основе реальных типов билетов
    billet_data = []
    for ticket_type in ticket_types[:2]:  # Берем первые 2 типа билетов
        billet_data.append({
            'title': f'{ticket_type.get_name_display()} билет',
            'price': f'{ticket_type.price} ₽',
            'time': 'с 10.00 до 20.00',
            'image': 'snow.png' if ticket_type.name == 'child' else 'kino.png',
            'type': ticket_type.name,
            'description': ticket_type.description or f'Билет типа {ticket_type.get_name_display()}'
        })
    
    context = {
        'ticket_types': ticket_types,
        'billet_data': billet_data,
    }
    return render(request, 'page4.html', context)