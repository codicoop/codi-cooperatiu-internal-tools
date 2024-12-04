from django import forms


class FlowBiteTimeInput(forms.TimeInput):
    input_type = "time"


class FlowBiteDateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)
