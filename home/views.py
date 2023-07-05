from django.shortcuts import  render, redirect,HttpResponse
from home import forms
from django.contrib.auth import login
from django.contrib import messages
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Profile
import pdfkit
from django.template import loader
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import ParagraphStyle
from django.conf import settings
from qrcode import *
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.shortcuts import render
from io import StringIO
from io import BytesIO




from django.http import HttpResponse

from django.template.loader import get_template

from xhtml2pdf import pisa
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from django.db.models import Sum
from django.shortcuts import render, redirect
from .forms import ProfileForm
from django.contrib import messages

from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
  
      
       
    
    return render(request, 'index..html')


@login_required(login_url='login/')
def create_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'create_profile.html', context)



# import pdfkit
# from django.template.loader import render_to_string
# from django.db import models
# from django.http import HttpResponse

# def generate_pdf(request):
#     # Get the data from the database
#     data = Profile.objects.()
#     # Define the context for the template
#     context = {'data': data}
#     # Render the template as a string
#     html = render_to_string('resume.html', context)
#     # Define the options for wkhtmltopdf
#     options = {
#         'page-size': 'A4',
#         'margin-top': '0mm',
#         'margin-right': '0mm',
#         'margin-bottom': '0mm',
#         'margin-left': '0mm',
#     }
#     # Generate the PDF using pdfkit
#     pdf = pdfkit.from_string(html, False, options)
#     # Set the response headers
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="example.pdf"'
#     # Return the response
#     return response

# def resume(request,id):
#     # Get data from the database
#     queryset = Profile.objects.filter(user=request.user) 

#     # Get the template
#     template = get_template('resume.html')

#     # Create the PDF object
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="my_pdf.pdf"'
#     p = canvas.Canvas(response, pagesize=letter)

#     # Draw things on the PDF. Here's where the PDF generation happens.
#     # See the ReportLab documentation for the full list of functionality.
#     textobject = p.beginText()
#     textobject.setTextOrigin(inch, 11*inch)
#     textobject.setFont("Helvetica-Bold", 14)
#     textobject.textLines("My PDF Document")
#     p.drawText(textobject)

#     # Render the template with the data
#     context = {'profile': queryset}
#     html = template.render(context)
#     result = StringIO()
#     pdf = pisa.pisaDocument(StringIO(html), result)

#     # Close the PDF object cleanly, and we're done.
#     p.showPage()
#     p.save()

#     # Return the PDF as a file download
#     response.write(result.getvalue())
#     return response

def resume(request,id):
    profile = Profile.objects.filter(user=request.user)
    for i in profile:
        
      print("xxxxxxxxxxxxxxxxxxxxxxxxx",i.name,i.id)
      data=i.name,i.id
    #data="rashidkHan1234"
    print(data)
    img=make(data)
    img.save('static/images/test.png')

    template_path = 'resumee.html'

    context = {'profile': profile}

    response = HttpResponse(content_type='application/pdf')

    response['Content-Disposition'] = 'filename="profile.pdf"'

    template = get_template(template_path)

    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response









@login_required(login_url='login/')
def profile(request):
      
     if request.method == 'POST':
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        
        contact = Contact(name=name, subject=subject, email=email, message=message)
        contact.save()
        messages.success(request, 'Contact saved successfully.')
        
    

     return render(request,'index.html')
 

class CustomerRegisterView(View):
    def get(self,request):
        form=forms.CustomerRegistrationForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):

        form=forms.CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Your Acount Created Succfully')
            form.save()
        return render(request,'register.html',{'form':form})
# def resume(request, id):
#     profile = Profile.objects.filter(user=request.user)
    
#     template = loader.get_template('resume.html')

#     html = template.render({'profile': profile})
#     options = {
#         'page-size': 'Letter',
#         'encoding': 'UTF-8',
#     }
    
#     pdf = pdfkit.from_string(html, False, options)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
#     return response

@login_required(login_url='login/')
def list(request):
    # profile = Profile.objects.filter(user=request.user)
    profile=Profile.objects.filter(user=request.user)
    print(profile)
    return render(request,'list.html',{'profile':profile})