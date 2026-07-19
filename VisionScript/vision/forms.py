from django import forms
from vision.models import ImageModel


class ImgaeUploadForm(forms.ModelForm):

    class Meta:

        model = ImageModel

        fields=['image']

        widgets = {
            "image":forms.FileInput(attrs={"class":"py-3 px-4 block w-full border-2 border-gray-200 rounded-md text-sm focus:border-blue-500 focus:ring-blue-500 shadow-sm"}),

            
          
        }