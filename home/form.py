from django.forms import ModelForm
from django import forms
from django.forms import TextInput, FileInput, EmailInput, Textarea, NumberInput
from .models import ContactUs, FeedBack, Subscribe

from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

import re

REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"


class SubscribeForm(ModelForm):
    """Subscribe form"""

    class Meta:
        model = Subscribe
        fields = ["email"]
        widgets = {
            "email": EmailInput(
                attrs={
                    "class": "form-control ",
                    "style": "",
                    "placeholder": "Your Email Address",
                    "id": "floatingInput",
                    "type": "email",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not re.match(REGEX, email):
            raise forms.ValidationError("Invalid email format")
        return email


class FeedBackForm(ModelForm):
    """Feedback form"""

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = FeedBack
        fields = ["email", "rating"]
        widgets = {
            "email": TextInput(
                attrs={
                    "class": "form-control ",
                    "style": "",
                    "placeholder": "Email",
                    "id": "floatingInput",
                }
            ),
            "rating": TextInput(
                attrs={
                    "class": "rate",
                    "style": "",
                    "placeholder": "rating",
                    "id": "floatingInput",
                    "type": "radio",
                }
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email and not re.match(REGEX, email):
            raise forms.ValidationError("Invalid email format")
        return email


class ContactForm(ModelForm):
    """contact form"""

    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

    class Meta:
        model = ContactUs
        fields = ["name", "email", "message"]
        widgets = {
            "name": TextInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:10px; color:blue; font-weight:500; ",
                    "placeholder": "Name",
                    "id": "floatingInput",
                }
            ),
            "email": EmailInput(
                attrs={
                    "class": "form-control",
                    "style": "padding-left:10px; color:blue; font-weight:500; ",
                    "placeholder": "Email",
                    "id": "floatingInput",
                    "type": "email",
                }
            ),
            "message": Textarea(
                attrs={
                    "class": "form-control ",
                    "style": "padding-left:10px; color:blue; font-weight:500; height:120px;",
                    "placeholder": "message",
                    "id": "floatingInput",
                }
            ),
        }
        # this function will be used for the validation

    def clean(self):
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
        # extract the username and text field from the data
        name = self.cleaned_data.get("name")
        email = self.cleaned_data.get("email")
        message = self.cleaned_data.get("message")

        # conditions to be met for the name length
        if len(name) < 5:
            self._errors["name"] = self.error_class(["Minimum 5 characters required"])
        if len(message) < 10:
            self._errors["message"] = self.error_class(
                ["Message Should Contain a minimum of 10 characters"]
            )
            # return any errors if found
        return self.cleaned_data
