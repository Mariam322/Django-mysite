from django.forms import ModelForm
from .models import Produit
from .models import Commande
class ProduitForm(ModelForm):
    class Meta:
        model = Produit
        fields = "__all__" #pour tous les champs de la table

class CommandeForm(ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"

 