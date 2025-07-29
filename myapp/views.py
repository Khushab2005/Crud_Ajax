from django.shortcuts import render,HttpResponse,get_object_or_404
from myapp.models import *
from django.http import JsonResponse
# Create your views here.
def home_page(request):
    return render(request,'home.html')

def display(request):

    data = Employe.objects.all()
    result = []
    for i in data:
        result.append({
            'id':i.id,
            'name' : i.name,
            'email' : i.email,
            'gender':i.gender,
            'department':i.department,
            'images': i.images.url if i.images else "",
            
        })
    return JsonResponse({'data':result})
    
    
def insert(request):
    
    print("1")
    if request.method == 'POST':
        print("2")
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        department = request.POST['department']
        images = request.FILES.get('images')
        
        Employe.objects.create(
            name = name,
            email = email,
            gender = gender,
            department = department,
            images = images 
        )
        
    return HttpResponse("data insert successully !")

def deletes(request):
    id = request.GET.get('id')  # ✅ Get 'id' from GET parameters
    if id:
        data = get_object_or_404(Employe, id=id)
        data.delete()
    return HttpResponse("Data deleted successfully!")

def employeid(request):
    eid = request.GET.get('sid')
    try:
        emp = Employe.objects.get(pk=eid)
        return JsonResponse({
            'data': [{
                'id': emp.id,
                'name': emp.name,
                'email': emp.email,
                'gender': emp.gender,
                'department': emp.department,
                'images': emp.images.url if emp.images else ""
            }]
        })
    except Employe.DoesNotExist:
        return JsonResponse({'error': 'Employee not found'}, status=404)

def updates(request):
    data1 = Employe.objects.get(pk= request.POST['id'])
    data1.name = request.POST['name']
    data1.email = request.POST['email']
    data1.gender = request.POST['gender']
    data1.department = request.POST['department']
    data1.images = request.FILES.get('images')
    data1.save()
    return HttpResponse("Student updated !!!!")




