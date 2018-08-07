from django import forms
from rater.ratings import RATING_CHOICES


class RateNameForm(forms.Form):
    rating =  forms.ChoiceField(choices=RATING_CHOICES,
                                label='',
                                initial='',
                                widget=forms.Select(),
                                required=True)
    starred = forms.BooleanField()
