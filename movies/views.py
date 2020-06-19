from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie, Genre, Review, Comment
from .forms import MovieForm, ReviewForm, CommentForm
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.db.models import Avg


def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'movies' : movies,
        'page_obj' : page_obj,
    }
    return render(request, 'movies/index.html', context)

@login_required
def create(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm()
        context = {
            'form': form
        }
        return render(request, 'movies/forms.html', context)
    else:
        return redirect('movies:index')

@login_required
def update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user.is_staff:
        if request.method == "POST":
            form = MovieForm(request.POST, instance=movie)
            if form.is_valid():
                form.save()
                return redirect('movies:detail', movie.pk)
        else:
            form = MovieForm(instance=movie)
        context = {
            'form' : form
        }
        return render(request, 'movies/forms.html', context)

@login_required
def delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.user.is_staff:
        movie.delete()
    return redirect('movies:index')

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    total = movie.like_users.all().count()
    male = movie.like_users.all().filter(gender='M').count()
    female = movie.like_users.all().filter(gender='F').count()
    liked_50 = movie.like_users.all().filter(age__gte=50).count()
    liked_40 = movie.like_users.all().filter(age__gte=40).filter(age__lt=50).count()
    liked_30 = movie.like_users.all().filter(age__gte=30).filter(age__lt=40).count()
    liked_20 = movie.like_users.all().filter(age__gte=20).filter(age__lt=30).count()
    liked_10 = movie.like_users.all().filter(age__lt=20).count()
    context = {
        'movie' : movie,
        'total' : total,
        'male' : male,
        'female' : female,
        'liked_50' : liked_50,
        'liked_40' : liked_40,
        'liked_30' : liked_30,
        'liked_20' : liked_20,
        'liked_10' : liked_10, 
    }
    return render(request, 'movies/detail.html', context)

def like(request, pk):
    user = request.user
    movie = get_object_or_404(Movie, pk=pk)
    if movie.like_users.filter(pk=user.pk).exists():
        movie.like_users.remove(user)
        liked = False
    else:
        movie.like_users.add(user)
        liked = True

    context = {
        'liked': liked,
        'count': movie.like_users.count(),
    }
    return JsonResponse(context)

@login_required
def reviews_create(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.movie = movie
            review.save()
        return redirect('movies:reviews_detail', movie.pk, review.pk)
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'movies/review_forms.html', context)

def reviews_detail(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm()
    context = {
        'review' : review,
        'movie' : movie,
        'form' : form,
    }
    return render(request, 'movies/review_detail.html', context)

@login_required
def reviews_update(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            form = ReviewForm(request.POST, instance = review)
            if form.is_valid():
                review = form.save()
                return redirect('movies:reviews_detail', movie.pk, review.pk)
        else:
            form = ReviewForm(instance = review)
        context = {
            'form': form
        }
        return render(request, 'movies/review_forms.html', context)
    else:
        return redirect('movies:reviews_detail', movie.pk, review.pk)

@login_required
def reviews_delete(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.user == request.user:
        review.delete()
    return redirect('movies:detail', movie.pk)

@login_required
def review_like(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(id=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('movies:reviews_detail', pk, review_pk)

@login_required
def review_hate(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    if review.hate_users.filter(id=request.user.pk).exists():
        review.hate_users.remove(request.user)
    else:
        review.hate_users.add(request.user)
    return redirect('movies:reviews_detail', pk, review_pk)

@require_POST
@login_required
def comment_create(request, pk, review_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('movies:reviews_detail', pk, review_pk)


@login_required
def comment_delete(request, pk, review_pk, comment_pk):
    movie = get_object_or_404(Movie, pk=pk)
    review = get_object_or_404(Review, pk=review_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('movies:reviews_detail', pk, review_pk)

@login_required
def recommend2(request):
    review=Review.objects.all()

    if request.user.review_set.all():
        avg_rate = request.user.review_set.all().aggregate(Avg('rank'))
        movie_list=Movie.objects.filter(vote_average__gte=avg_rate['rank__avg']-1).filter(vote_average__lte=avg_rate['rank__avg']+1)
        context={
            'movie_list':movie_list,
            'avg_rate':avg_rate,
        }
        return render(request,'movies/recommend2.html', context)
    else:
        age = request.user.age
        if age <= 10:
            genre = get_object_or_404(Genre, name='Animation')
        elif age < 20:
            genre = get_object_or_404(Genre, name='Action')
        elif age < 30:
            genre = get_object_or_404(Genre, name='Romance')
        elif age < 40:
            genre = get_object_or_404(Genre, name='Drama')
        elif age >= 40:
            genre = get_object_or_404(Genre, name='Family')
        context = {
            'genre' : genre
        }
        return render(request, 'movies/recommend.html', context)