from django import forms


class RatingForm(forms.Form):
    beer_id = forms.CharField()
    score = forms.CharField(max_length=1)