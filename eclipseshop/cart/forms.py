from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label='')
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    # Styles for quantity from login page if it will be used sometimes
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'u-border-3 u-border-grey-70 u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-input-1',
                                       'style': 'margin:5px; display: none;'
                                       })
