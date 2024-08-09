from django import forms
from django.template import Context, Template

from flowbite_classes.forms import BooleanBoundField, CharBoundField


class CharForm(forms.Form):
    """
    Example form that uses forms.CharField.
    """

    char_field = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "Text 1",
                "autocomplete": "text",
            }
        ),
        help_text="Help for char_field",
    )


class BooleanForm(forms.Form):
    boolean_field = forms.BooleanField(widget=forms.CheckboxInput, help_text="Help boolean_field")


def test_monkey_patching_applied_to_charfield():
    """
    Verifies that the monkey patching applied to forms.CharField works correctly.
    """
    template = Template(
        """
        {{ form }}
        """
    )
    form_instance = CharForm()
    html = template.render(Context({"form": form_instance}))

    # Verify that only one input is rendered
    assert html.count("<input") == 1

    # Verify that the base classes have been applied
    assert CharBoundField.base_classes in html, "Base classes were not applied correctly."

    # Verify that the no-error classes have been applied
    assert CharBoundField.no_error_classes in html, "No-error classes were not applied correctly."


def test_monkey_patching_applied_to_booleanfield():
    """
    Verifies that the monkey patching applied to forms.CharField works correctly.
    """
    template = Template(
        """
        {{ form }}
        """
    )
    form_instance = BooleanForm()
    html = template.render(Context({"form": form_instance}))

    # Verify that only one input is rendered
    assert html.count("<input") == 1

    # Verify that the base classes have been applied
    assert BooleanBoundField.base_classes in html, "Base classes were not applied correctly."

    # Verify that the no-error classes have been applied
    assert BooleanBoundField.no_error_classes in html, "No-error classes were not applied correctly."
