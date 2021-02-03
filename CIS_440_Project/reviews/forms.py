#from django import forms
#from .models import Review

#class ReviewForm(forms.ModelForm):
#    def __init__(self, *args, user=None, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['reviews'].queryset = Review.objects.filter(user=user)

#    class Meta:
#        model = Review
#        fields = ['name', 'foods']


