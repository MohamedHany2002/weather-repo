from django import forms 



class WeatherForm(forms.Form):
    temp = forms.FloatField(required=True, min_value=19, max_value=28)
    hum = forms.FloatField(required=True, min_value=35, max_value=65)

    # def clean_temp(self):
    #     temp=self.cleaned_data.get('temp')
    #     if temp<19 and temp>28:
    #         raise forms.ValidationError('temprature must be between 19 and 28')
    #     return temp

    # def clean_temp(self):
    #     hum=self.cleaned_data.get('hum')
    #     if hum<35 and hum>65:
    #         raise forms.ValidationError('humidity must be between 35 and 65')
    #     return hum