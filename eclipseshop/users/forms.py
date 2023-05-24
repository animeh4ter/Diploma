from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'u-border-3 u-border-grey-70 u-border-no-left u-border-no-right u-border-no-top u-custom-font u-grey-5 u-heading-font u-input u-input-rectangle u-input-1',
                                       'style': 'margin:20px;'
                                       })

