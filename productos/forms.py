from django import forms
from .models import Categoria, Producto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la categoría'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la categoría', 'rows': 3}),
        }

class ProductoForm(forms.ModelForm):
    eliminar_imagen = forms.BooleanField(required=False, initial=False)
    
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'disponible', 'categoria', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'step': '0.01'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': '0'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'categoria': forms.Select(attrs={'class': 'form-select', 'required': False}),
            'imagen': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }
    
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser mayor que cero.")
        return precio
    
    def save(self, commit=True):
        producto = super().save(commit=False)
        
        # Manejar la eliminación de la imagen si se marca la casilla
        eliminar_imagen = self.cleaned_data.get('eliminar_imagen', False)
        if eliminar_imagen and producto.imagen:
            # Guardar la referencia para eliminarla después
            imagen_anterior = producto.imagen
            producto.imagen = None
            if commit and imagen_anterior:
                # Eliminar el archivo físico
                imagen_anterior.delete(save=False)
        
        if commit:
            producto.save()
        
        return producto