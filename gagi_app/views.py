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
    attractions = Attractions.objects.filter(activity_status=True)
    
    context = {
        'attractions': attractions,
        'attractions_count': attractions.count(),
        'attraction_examples': attractions[:3],  # Берем первые 3 аттракциона из базы
        'ticket_types': TicketTypes.objects.all(),
    }
    return render(request, 'page2.html', context)

def page3(request):
    return render(request, 'page3.html')

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

def page4(request):
    ticket_types = TicketTypes.objects.all()

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
    }
    return render(request, 'page4.html', context)

