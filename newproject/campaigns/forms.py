from django import forms
from .models import CampaignFundRaiser

class NewCampaignForm(forms.ModelForm):
    # about = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
    #         ),
    # )

    class Meta:
        model = CampaignFundRaiser
        fields = ['title','category','goal','day','short_description', 'about','campaign_image']