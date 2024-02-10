from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(
        attrs={'class':'name','id':'uName'}
    ))
    rating = forms.IntegerField(max_value=5, min_value=1,help_text="Rating must be lessthan 5")
    comment=forms.CharField(widget=forms.Textarea, help_text="Enter your feedback!")