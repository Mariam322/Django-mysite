from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Produit
from .forms import ProduitForm
from .models import Commande
from .forms import CommandeForm
from django.shortcuts import redirect



def index1(request):
    list=Produit.objects.all()
    return render(request,'vitrine.html',{'list':list})
def index(request):
    template=loader.get_template('index.html')
    list= Produit.objects
    ts.all()
    return HttpResponse(template.render( {'list':list} ))
# def listeProduit(request):
#     return render(request,'magasin/majProduits.html')

def index2(request):
    if request.method == "POST":
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else:
        form = ProduitForm()
    return render(request,'majProduits.html',{'form':form})
def detail(request,id_article):
    article=Produit.objects.get(id=id_article)
    return render(request,'detail.html',{"article":article})
def cart(request):
    context = {}
    return render(request, 'cart.html', context)
def checkup(request):
    context = {}
    return render(request, 'checkup.html', context)

# def mesCommandes(request):
#     sauvegarde=False
#     form=CommandeForm(request.POST, request.FILES)
#     if form.is_valid():
#         cmd=Commande()
#         cmd.Duree_garantie=form.cleaned_data["Duree_garantie"]
#         cmd.dateCde=form.cleaned_data["dateCde"]
#         cmd.totalCde=form.cleaned_data["totalCde"]
#         form.save()
#         sauvegarde=True
#         return redirect('/magasin')
#     else:
#         form=CommandeForm()
#     return render(request,'commande.html',{'form':form})

def mesCommandes(request):
    if request.method == "POST":
        form = CommandeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/magasin')
    else:
        form = CommandeForm()
        return render(request,'commande.html',{'form':form})
