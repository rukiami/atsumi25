from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
    """ログインフォーム"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        # 必要に応じて、'email', 'first_name', 'last_name' など他のフィールドを追加可能


class SearchForm(forms.Form):
    genre = forms.CharField(label='ジャンル', max_length=100, required=False)
    location = forms.CharField(label='場所', max_length=100, required=False)


from django import forms

class RestaurantSearchForm(forms.Form):
    genre = forms.CharField(required=False, label='ジャンル')
    location = forms.CharField(required=False, label='場所')
    date = forms.DateField(required=False, label='日付', widget=forms.TextInput(attrs={'type': 'date'}))

from .models import Restaurant

class RestaurantForm(forms.ModelForm):
    GENRE_CHOICES = [
        ('和食', '和食'),
        ('洋食', '洋食'),
        ('中華', '中華'),
        ('韓国', '韓国'),
        ('イタリアン', 'イタリアン'),
        ('カフェ', 'カフェ'),
       
        # 他のジャンルをここに追加
    ]

    PRICE_RANGE_CHOICES = [
        ('0-999円', '～￥999'),
        ('1000-1999円', '￥1000～￥1999'),
        ('2000-2999円', '￥2000～￥2999'),
        ('3000-3999円', '￥3000～￥3999'),
    
    # 他の価格帯を追加できます
]
    url = forms.URLField(required=False, label='ウェブサイトURL')  
    google_maps = forms.URLField(required=False, label='GoogleマップURL')
    # genre = forms.ChoiceField(choices=GENRE_CHOICES, label='ジャンル')

    class Meta:
        model = Restaurant
        fields = ['name', 'phone_number', 'location', 'genre', 'url', 'price_range', 'google_maps', 'photo']  
        # fields = ['name', 'address', 'genre', 'location', 'date_added', 'description', 'category', 'price_range', 'google_maps', 'photo']
        labels = {
            'name': '店舗名',
            # 'address': '住所',
            'phone_number': '電話番号', 
            'location': '場所',
            'genre': 'ジャンル',
            # 'description': '説明',
            # 'category': 'カテゴリ',
            'price_range': '価格帯',
            'url': 'ウェブサイトURL',  # これも追加
            'google_maps': 'Googleマップ',
            'photo': '写真'
            
        }   
    def __init__(self, *args, **kwargs):
        super(RestaurantForm, self).__init__(*args, **kwargs)
        self.fields['genre'] = forms.ChoiceField(choices=self.GENRE_CHOICES, label='ジャンル')
        self.fields['price_range'] = forms.ChoiceField(choices=self.PRICE_RANGE_CHOICES, label='価格帯')
from .models import Photo

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']     


# class EventForm(forms.ModelForm):
#    start_date = forms.IntegerField(required=True)
#    end_date = forms.IntegerField(required=True)
#    event_name = forms.CharField(required=True, max_length=32)         
#    location = forms.CharField(required=False, max_length=100)  # 場所を追加

# from .models import Event
# class EventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = ['event_name', 'start_date', 'end_date', 'location', 'genre', 'price_range']
#         widgets = {
#             'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
#             'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
#         }    