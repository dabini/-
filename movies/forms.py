from django import forms
from .models import Movie, Review, Comment

REVIEW_POINT_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
)
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content', 'rank']
        labels = {
            'title' : '리뷰 제목',
            'content' : '영화 리뷰',
            'rank' : '평점',
        }
        widgets = {
            'rank' : forms.Select(choices=REVIEW_POINT_CHOICES)
        }
        help_texts = {
            'rank': '평점은 1부터 10까지 입력 가능합니다. ',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content' : '댓글',
        }
        help_texts = {
            'content': '댓글은 150자까지 입력가능합니다.',
        }