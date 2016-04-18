from dal import autocomplete
from crispy_forms.bootstrap import InlineField

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Button, HTML
from crispy_forms.bootstrap import FormActions
from django import forms
from django.contrib.auth.models import User
from stockplot.models import Stock, Depot, DepotContent

# form for selecting stock in stockplot.
class StockForm(forms.ModelForm):
    # form for selecting stock with autocomplete from database
    select_stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(url='/stockapp/stock-autocomplete')
    )
    select_method = forms.ChoiceField(
        choices = (
            ("plot", "Plot"),
            ("movingAverage", "Moving Average"),
            ("exponentialAverage", "Exponential Moving Average"),
        ),
        label = "Select Plot Method",
    )
    days = forms.IntegerField()

    class Meta:
        model = Stock
        fields = ()

    def __init__(self, *args, **kwargs):
        super(StockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            HTML('<div class="form-group"><label>Select Stock:</label></div>'),
            InlineField('select_stock', css_class = 'input-sm'),
            HTML('<div class="form-group"><label>Select Method:</label></div>'),
            InlineField('select_method', css_class = 'input-sm'),
            InlineField('days', css_class = 'input-sm'),
            FormActions(
                Submit('Plot', 'Go', css_class = 'btn-plot btn-sm'),
            ),
        )

    def clean(self):
        pass

# form for selecting depot:
class DepotForm(forms.ModelForm):
    # form for selecting depot with autocomplete from database
    select_depot = forms.ModelChoiceField(
        queryset=Depot.objects.all(),
        widget=autocomplete.ModelSelect2(url='/depot/depot-autocomplete')
    )
    depot_name = forms.CharField(max_length = 100, help_text='Depot name')
    depot_value = forms.IntegerField(help_text='Money')

    def __init__(self, *args, **kwargs):
        super(DepotForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            HTML('<div class="form-group"><label>Select Depot:</label></div>'),
            'select_depot',
            FormActions(
                Submit('Select Depot', 'Select', css_class = 'btn-default btn-sm'),
            ),
            HTML('<div class="form-group"><label>or create depot:</label></div>'),
            InlineField('depot_name', css_class ='input-sm'),
            InlineField('depot_value', css_class = 'input-sm'),
            FormActions(
                Submit('Create Depot', '+', css_class = 'btn-default btn-sm')
            ),
        )

    class Meta:
        model = Depot
        fields = ()

# form for buying stock.
'''class BuyStockForm(forms.ModelForm):
    # form for selecting stock with autocomplete from database
    select_stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(url='/stockapp/stock-autocomplete')
    )
    amount = forms.IntegerField()
    class Meta:
        model = Stock
        fields = ()

    def __init__(self, *args, **kwargs):
        super(BuyStockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            HTML('<div class="form-group"><label>Select Stock:</label></div>'),
            'select_stock',
            InlineField('amount', css_class = 'input-sm'),
            FormActions(
                Submit('Buy Stock', 'Buy', css_class = 'btn-plot btn-sm'),
            )
        )'''

class BuyStockForm(forms.ModelForm):
    # form for selecting stock with autocomplete from database
    select_stock = forms.ModelChoiceField(
        queryset=Stock.objects.all(),
        widget=autocomplete.ModelSelect2(url='/stockapp/stock-autocomplete')
    )
    amount = forms.IntegerField()
    fees = forms.IntegerField()
    class Meta:
        model = Stock
        fields = ()

    def __init__(self, *args, **kwargs):
        super(BuyStockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'select_stock',
            'amount',
            'fees',
            #FormActions(
            #    Submit('Buy Stock', 'Buy', css_class = 'btn-plot btn-sm'),
            #)
        )

# form for selling stock in depot.
class SellStockForm(forms.ModelForm):
    # form for selecting stock with autocomplete from database
    amount = forms.IntegerField()
    select_stockmarket = forms.ChoiceField(
        choices = (
            ("FRA", "Frankfurt"),
            ("LON", "London"),
            ("NYC", "New York"),
        ),
        label = "Select Stock Market",
    )

    def __init__(self, *args, **kwargs):
        #super(SellStockForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #self.helper.form_class = 'form-inline'
        #self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.layout = Layout(
            #HTML('<div class="form-group"><label>Select Stock:</label></div>'),
            'amount',
            #HTML('<div class="form-group"><label>Select Method:</label></div>'),
            'select_stockmarket',
            FormActions(
                Submit('Sell', 'Sell', css_class = 'btn-plot btn-sm'),
            ),
        )


# form for user profile:
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',]
