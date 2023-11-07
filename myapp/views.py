from django.shortcuts import render, get_object_or_404
from .models import Tour, Agency, Reservation, Review
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from .forms import ReservationForm
from django.shortcuts import render
from .models import Agency, Tour, User, Reservation, Review, Country


def tour_reserve(request, pk):
    return render(request, 'reserve_tour.html')



def tour_list_view(request):
    tours = Tour.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.users = request.user
            reservation.save()
            tour = form.cleaned_data['tour']
            tour.reservations.add(reservation)
    else:
        form = ReservationForm()
    return render(request, 'tour_list.html', {'tours': tours, 'form': form})


def tour_detail_view(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    return render(request, 'tour_detail.html', {'tour': tour})

def agency_detail_view(request, pk):
    agency = get_object_or_404(Agency, pk=pk)
    return render(request, 'agency_detail.html', {'agency': agency})

def reservation_detail_view(request, pk):
    reservation = get_object_or_404(Reservation, pk=pk)
    return render(request, 'reservation_detail.html', {'reservation': reservation})


def review_detail_view(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review_detail.html', {'review': review})

def tour_list_view(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'tour_list.html', context)

def sold_tours_view(request, country_id):
    country = Country.objects.get(pk=country_id)
    sold_tours = Tour.objects.filter(country=country)
    context = {
        'country': country,
        'sold_tours': sold_tours,
    }
    return render(request, 'sold_tours.html', context)


def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('tour_list')  # Перенаправляем пользователя на нужную страницу после регистрации
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def register_client(request):
    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Автоматически входит в систему после регистрации
            return redirect('home')  # Перенаправление на главную страницу или другую страницу
    else:
        form = ClientRegistrationForm()
    return render(request, 'registration/register_client.html', {'form': form})


def add_review(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.tour = tour
            review.users = request.user
            review.save()
            return redirect('tour_detail', pk=pk)
    else:
        form = ReviewForm()
    
    return render(request, 'add_review.html', {'form': form, 'tour': tour})


    