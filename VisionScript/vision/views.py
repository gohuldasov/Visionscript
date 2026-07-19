from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import JsonResponse
from vision.forms import ImgaeUploadForm

import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

def extract_text_from_image(image_path):
    
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text


class ImageUploadView(View):

    template_name = 'imageupload.html'

    template='txt.html'

    form_class = ImgaeUploadForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=self.form_class(request.POST,files=request.FILES)

        if form_instance.is_valid():

            image_instance=form_instance.save()

            image_path = image_instance.image.path

            extracted_text = extract_text_from_image(image_path)
            
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
                return JsonResponse({'extracted_text': extracted_text})

            return render(request, self.template, {'extracted_text': extracted_text})

        if request.headers.get('x-requested-with') == 'XMLHttpRequest' or 'application/json' in request.headers.get('accept', ''):
            return JsonResponse({'error': 'Invalid form submission', 'errors': form_instance.errors}, status=400)

        return render(request,self.template_name,{"form":form_instance})
    
class TextView(View):

    template_name='txt.html'

    def get(self,request,*args,**kwargs):

        return render(request,self.template_name)




        