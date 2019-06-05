from django.shortcuts import render, get_object_or_404
from .models import CarMake, CarModel, Review
from .forms import CarMakeForm
from .forms import CarModelForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'carapp/index.html')

def getCarMakes (request):
    carmakes_list=CarMake.objects.all()
    return render(request, 'carapp/carmake.html' ,{'carmakes_list' : carmakes_list})

def getCarModels(request):
    carmodels_list=CarModel.objects.all()
    return render(request, 'carapp/carmodel.html', {'carmodels_list' : carmodels_list})  

def carmodeldetails(request, id):
    model=get_object_or_404(CarModel, pk=id)
    return render(request, 'carapp/carmodeldetail.html',{'model': model})  

@login_required
def newCarMake(request):
    form=CarMakeForm
    if request.method=='POST':
         form=CarMakeForm(request.POST)
         if form.is_valid():
             post=form.save(commit=True)
             post.save()
             form=CarMakeForm()
    else:
        form=CarMakeForm()
    return render(request, 'carapp/newcarmake.html', {'form':form})  

@login_required
def newCarModel(request):
    form=CarModelForm
    if request.method=='POST':
         form=CarModelForm(request.POST)
         if form.is_valid():
             post=form.save(commit=True)
             post.save()
             form=CarModelForm()
    else:
        form=CarModelForm()
    return render(request, 'carapp/newcarmodel.html', {'form':form})

def logintext(request):
    return render(request,'carapp/logintext.html')

def logouttext(request):
    return render(request,'carapp/logouttext.html')
