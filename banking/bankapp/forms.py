from django import forms
from django.forms import TextInput,ChoiceField
from .models import NewMember,Branch

MATERIAL_CHOICES = [
    ('cheque','Cheque Book'),
    ('debit', 'Debit Card'),
    ('credit','Credit Card')
]
class NewMemberForm(forms.ModelForm):
    materials = forms.MultipleChoiceField(choices=MATERIAL_CHOICES,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = NewMember
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(),
            'dob' : forms.DateInput(attrs={'type':'date'}),
            'gender': forms.RadioSelect(),
            'email' :forms.EmailInput(),
            'materials' : forms.TextInput(),

            # 'country': forms.ChoiceField(attrs={'class': "php-email-form"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('branch_name')
            except (ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('branch_name')

