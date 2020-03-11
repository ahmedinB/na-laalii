from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from library.models import bookdata
 # Create your views here.
def comment(request):
    if request.method == 'LIBRARY':
        comment(
            title=request.LIBRARY.get('title')
            # detail=request.LIBRARY.get('detail')
            # detail=request.LIBRARY.get('detail')   
         )
        if form.is_valid():
            post=form.save(commit=false)
            post.save()
    # return HttpResponseRedirect('')
    return HttpResponse("fuck you go back")

def main(request):
    # return HttpResponse("trail")
    img=bookdata.objects.all()
    return render(request,'library/temp.html',{"img":img})
from reportlab.pdfgen import canvas
from django.http import HttpResponse
def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'
    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response

def detail(request,id):
    query = request.GET.get('id')
    detail=bookdata.objects.get(id=id)

    return HttpResponse("this has id of bhjvgh")
def home(request):
    query=request.GET.get('name')
    message= "hello {} i am learning django".format(query)
    template="library/home.html"
    context={
        'message':message,
    }
    return render(request,template,context)  
def conda(request):
    template="library/staticsam.html"
  
    return render(request,template)  