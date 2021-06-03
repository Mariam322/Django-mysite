from django.db import models
from datetime import date

# Create your models here.
class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballe')]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    emballage=models.OneToOneField('Emballage',on_delete=models.CASCADE,null=True)
    img=models.ImageField(blank=True,default=" ")
    Commande=models.ManyToManyField('Produit')
    
    fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return (self.libelle+" "+self.description+" "+str(self.prix))
class Emballage(models.Model):
    COUL_CHOICES=[('bl','blanc'),('rg','rouge'),('ble','bleu'),('vr','vert'),('muli','multicolore')]
    matiere=models.CharField(max_length=20)
    couleur=models.CharField(max_length=20,default='transparant',choices=COUL_CHOICES)

    def __str__(self):
        return self.matiere+" "+self.couleur
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100,default="", editable=False)
    email=models.CharField(max_length=100,default=" ")
    tel=models.CharField(max_length=9,default=" ")
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+self.tel

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100,default=" ")
    def __str__(self):
        return "objet ProduitNC : %s"%(self.Duree_garantie)


class Commande(models.Model):
    Duree_garantie = models.CharField(max_length=100)
    dateCde = models.DateField(null=True,default=date.today)
    totalCde = models.DecimalField(max_digits=10,decimal_places=3)
    produits = models.ManyToManyField('Produit')
    def __str__(self):
        return ("duree garantie : {} date Cde : {} totalcde: {} ").format(self.Duree_garantie,self.dateCde,self.totalCde)

