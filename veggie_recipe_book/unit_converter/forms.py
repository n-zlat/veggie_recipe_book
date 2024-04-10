from django import forms


class UnitConverterForm(forms.Form):
    MAX_AMOUNT_DIGITS = 10
    AMOUNT_DECIMAL_PLACES = 2

    MEASUREMENT_UNITS = (
        ('gram', 'Gram'),
        ('milligram', 'Milligram'),
        ('milliliter', 'Milliliter'),
        ('liter', 'Liter'),
        ('teaspoon', 'Teaspoon'),
        ('tablespoon', 'Tablespoon'),
        ('cup', 'Cup'),
        ('ounce', 'Ounce'),
        ('pound', 'Pound'),
    )

    amount = forms.DecimalField(min_value=0,
                                max_digits=MAX_AMOUNT_DIGITS,
                                decimal_places=AMOUNT_DECIMAL_PLACES,
                                )
    from_unit = forms.ChoiceField(choices=MEASUREMENT_UNITS,
                                  )
    to_unit = forms.ChoiceField(choices=MEASUREMENT_UNITS,
                                )
