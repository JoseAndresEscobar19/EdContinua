from django import forms
from .models import PlanAnualCompras, Partida
from datetime import date


def year_choices():
    return [(r, r) for r in range(1995, date.today().year+1)]


class PlanAnualComprasForm(forms.ModelForm):
    class Meta:
        model = PlanAnualCompras
        fields = '__all__'
        labels = {
            "codigo": "Código",
            "centro_costos": "Centro de Costos",
            "partida": "Partida Presupuestaria",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "Subtotal",
            "total": "Valor total",
            "fecha": "",
            "estado": "",
        }
        widgets = {
            "fecha": forms.DateInput(attrs={'readonly': True, 'class': 'form-control', "type": "date", "value": date.today}),
            "motivo_anular": forms.HiddenInput(),
            "fecha_envio": forms.HiddenInput(),
            "fecha_aprobado": forms.HiddenInput(),
            "año": forms.Select(choices=year_choices()),
            "estado": forms.TextInput(attrs={"readonly": True}),
        }

class PlanAnualComprasUpdateForm(forms.ModelForm):
    class Meta:
        model = PlanAnualCompras
        fields = '__all__'
        labels = {
            "codigo": "Código",
            "centro_costos": "Centro de Costos",
            "nombre":"Nombre",
            "partida": "Partida Presupuestaria",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "Subtotal",
            "total": "Valor total",
            "fecha": "",
            "estado": "",
        }
        widgets = {
            "fecha": forms.DateInput(attrs={'readonly': True, 'class': 'form-control', "type": "date"}),
            "motivo_anular": forms.Textarea(attrs={"class": "form-control", "rows": 2}),
            "fecha_envio": forms.HiddenInput(),
            "fecha_aprobado": forms.HiddenInput(),
            "año": forms.NumberInput(attrs={'readonly':True}),
            "estado": forms.TextInput(attrs={"readonly": True}),
            "centro_costos":forms.Select(attrs={"disabled": True}),
            "nombre":forms.TextInput(attrs={"readonly": True}),
        }


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'

        labels = {
            "egreso": "",
            "tipo_compra": "Tipo de Compra",
            "producto": "Descripción",
            "cantidad_anual": "Cantidad Anual",
            "unidad_medida": "Unidad de medida",
            "costo_unitario": "Costo Unitario",
            "subtotal": "",
            "total": "",
        }

        widgets = {
            "pac": forms.HiddenInput(),
            "egreso": forms.HiddenInput(),
            "producto": forms.HiddenInput(),
            "unidad_medida": forms.TextInput(attrs={'readonly':True}),
			"subtotal": forms.NumberInput(attrs={'readonly':True,'class':'text-right text-currency'}),
            "total": forms.NumberInput(attrs={'readonly':True,'class':'text-right text-currency'}),
        }
