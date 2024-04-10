from django.urls import reverse_lazy
from decimal import Decimal

from django.views.generic import FormView

from veggie_recipe_book.unit_converter.forms import UnitConverterForm

CONVERSION_RATES = {
    'gram': {
        'milligram': Decimal('1000'),
        'ounce': Decimal('0.03527396'),
        'pound': Decimal('0.00220462')
    },
    'milligram': {
        'gram': Decimal('0.001'),
        'ounce': Decimal('0.00003527396'),
        'pound': Decimal('0.00000220462')
    },
    'milliliter': {
        'teaspoon': Decimal('0.202884'),
        'tablespoon': Decimal('0.067628'),
        'cup': Decimal('0.00422675'),
        'ounce': Decimal('0.033814'),
        'liter': Decimal('0.001')
    },
    'teaspoon': {
        'tablespoon': Decimal('0.333333'),
        'cup': Decimal('0.0208333'),
        'ounce': Decimal('0.166667')
    },
    'tablespoon': {
        'teaspoon': Decimal('3'),
        'cup': Decimal('0.0625'),
        'ounce': Decimal('0.5')
    },
    'cup': {
        'teaspoon': Decimal('48'),
        'tablespoon': Decimal('16'),
        'ounce': Decimal('8'),
        'pint': Decimal('0.5'),
        'liter': Decimal('0.236588'),
    },
    'ounce': {
        'teaspoon': Decimal('6'),
        'tablespoon': Decimal('2'),
        'cup': Decimal('0.125'),
        'pint': Decimal('0.0625'),
        'liter': Decimal('0.0295735'),
        'gram': Decimal('28.3495')
    },
    'pound': {
        'gram': Decimal('453.592'),
        'ounce': Decimal('16')
    },
    'pint': {
        'cup': Decimal('2'),
        'ounce': Decimal('16'),
        'liter': Decimal('0.473176'),
    },
    'liter': {
        'cup': Decimal('4.22675'),
        'ounce': Decimal('33.814'),
        'pint': Decimal('2.11338'),
    }
}


class UnitConverterView(FormView):
    template_name = 'unit_converter/converter.html'
    form_class = UnitConverterForm
    success_url = reverse_lazy('converter_view')

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        from_unit = form.cleaned_data['from_unit']
        to_unit = form.cleaned_data['to_unit']

        try:
            conversion_result = self.convert_units(amount, from_unit, to_unit)
            return self.render_to_response(self.get_context_data(form=form, conversion_result=conversion_result))
        except ValueError as e:
            return self.render_to_response(self.get_context_data(form=form, error_message=str(e)), status=400)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['conversion_result'] = kwargs.get('conversion_result')
        context['error_message'] = kwargs.get('error_message')
        return context

    @staticmethod
    def convert_units(amount, from_unit, to_unit):
        if from_unit == to_unit:
            return amount

        if from_unit in CONVERSION_RATES and to_unit in CONVERSION_RATES[from_unit]:
            conversion_rate = CONVERSION_RATES[from_unit][to_unit]
            return amount * conversion_rate
        elif to_unit in CONVERSION_RATES and from_unit in CONVERSION_RATES[to_unit]:
            conversion_rate = Decimal('1') / CONVERSION_RATES[to_unit][from_unit]
            return amount * conversion_rate
        else:
            raise ValueError('Sorry, this conversion is not supported')
