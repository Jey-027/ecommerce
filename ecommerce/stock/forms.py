from django import forms
from .models import Products, purchase, Pizza, Topping


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

class ProductSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['data-sku'] = value.instance.codigo
        return option

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = purchase
        fields = ['sku', 'quantity', 'customer_name', 'comments']
        widgets = {'sku': ProductSelect}


class ToppingSelect(forms.Select):
    def create_option(self, name, value, label, selected, index, subindex=None, attrs=None):
        option = super().create_option(name, value, label, selected, index, subindex, attrs)
        if value:
            option['attrs']['data-price'] = value.instance.price  #este seria el valor que envio a la base de datos
        return option

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping']
        widgets = {'topping': ToppingSelect}

        
