from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    print("from main:", request.session.get("pics"))
    if "pics" not in request.session:
        request.session["pics"] = []
    context = {"pictures": request.session["pics"]}
    return render(request, "index.html", context)

# def upload(request):
#     if request.method == "POST":
#         file = request.FILES["file"]
#         file_type = str(type(file))[1:-1]
#         print(file_type)
#         return HttpResponse(f"Yo! '{str(file_type)}'")

def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        myfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(f"apps/upload_file/static/upload_file/uploads/{myfile.name}", myfile)
        pic_list = request.session["pics"]
        pic_list.append(myfile.name)
        request.session["pics"] = pic_list
        uploaded_file_url = fs.url(filename)
        return redirect("/")
        # return render(request, 'core/simple_upload.html', {
        #     'uploaded_file_url': uploaded_file_url
        # })
    # return render(request, 'core/simple_upload.html')
    return render(request, 'core/simple_upload.html')

def clear(request):
    request.session.clear()
    return redirect("/")