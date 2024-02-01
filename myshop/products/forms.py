from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField()
    rating = forms.IntegerField(max_value=5, min_value=1,help_text="Rating must be lessthan 5")
    comment=forms.CharField(widget=forms.Textarea, help_text="Enter your feedback!")