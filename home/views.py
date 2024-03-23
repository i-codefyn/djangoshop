from django.views import generic
from oscar.core.loading import get_class, get_model
from django.utils import timezone

# revers and redirect
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

# messages
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# validation
from django.core.exceptions import ValidationError

# settingd imports
from django.conf import settings
from . import app_setting

# mail
from django.core.mail import EmailMultiAlternatives  # form html send
from django.core.mail import send_mail

# template rendering
from django.template.loader import render_to_string
from django.utils.html import strip_tags

Product = get_model("catalogue", "product")
ConditionalOffer = get_model("offer", "ConditionalOffer")

ContactUs = get_model("home", "ContactUs")
Feedback = get_model("home", "FeedBack")
Subscribe = get_model("home", "Subscribe")
SiteData = get_model("home", "SiteData")
AboutCompany = get_model("home", "AboutCompany")
KeywordDiscription = get_model("home", "KeywordDiscription")
Faq = get_model("home", "Faq")
ContactForm = get_class("home.form", "ContactForm")
FeedBackForm = get_class("home.form", "FeedBackForm")
SubscribeForm = get_class("home.form", "SubscribeForm")

SLIDER_MAX_PRODUCTS = 10


class FaqsView(generic.ListView):
    """FAQs Views"""

    PAGE_TITLE = "FAQs"
    template_name = "home/faqs." + app_setting.TEMPLATE_EXTENSION
    # paginate_by = 100  # if pagination is desired
    model = Faq
    context_object_name = "faq"
    extra_context = {
        "page_tite": PAGE_TITLE,
        "app_data": SiteData.objects.all(),
        "company_data": AboutCompany.objects.all(),
    }


class ContactFormView(generic.FormView):
    template_name = "home/contact_us." + app_setting.TEMPLATE_EXTENSION
    form_class = ContactForm
    PAGE_TITLE = "Contact Us"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super(ContactFormView, self).get_context_data(**kwargs)
        form = self.form_class()
        context["app_data"] = SiteData.objects.all()
        context["company_data"] = AboutCompany.objects.all()
        context["key"] = KeywordDiscription.objects.all()
        context["form"] = form

        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Thank You For Writting Us !")
        return reverse("home:contact")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        name = form.cleaned_data["name"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        form.save()
        context = {
            "title": "Thank you for Writting Us!",
            "content": "Thank you for your feedback !",
        }
        from_mail = settings.EMAIL_HOST_USER
        template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
        to_mail = email
        subject = "Thank you for Writting Us!"
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """

        errors = form.errors
        context = {
            "form": form,
            "app_data": SiteData.objects.all(),
            "company_data": AboutCompany.objects.all(),
            "key": KeywordDiscription.objects.all(),
            "page_title": "Contact_Us",
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class FeedBackFormView(generic.FormView):
    template_name = "home/feedback." + app_setting.TEMPLATE_EXTENSION
    form_class = FeedBackForm
    PAGE_TITLE = "Feedback"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super(FeedBackFormView, self).get_context_data(**kwargs)
        form = self.form_class()
        context["app_data"] = SiteData.objects.all()
        context["company_data"] = AboutCompany.objects.all()
        context["key"] = KeywordDiscription.objects.all()
        context["form"] = form

        return context

    def get_success_url(self):
        messages.success(self.request, "Successfully Submitted")
        return reverse("home:feedback")

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        email = form.cleaned_data["email"]
        form.save(commit=False)
        context = {"title": "Feedback", "content": "Thank you for your feedback !"}
        from_mail = settings.EMAIL_HOST_USER
        template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
        to_mail = email
        subject = "Thank you for Feedback!"
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors
        context = {
            "form": form,
            "errors": errors,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class HomePageView(generic.TemplateView):
    template_name = "home/index." + app_setting.TEMPLATE_EXTENSION
    form_class = SubscribeForm
    PAGE_TITLE = "HomePage"
    extra_context = {
        "page_title": PAGE_TITLE,
    }

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        form = self.form_class()
        products_featured = Product.objects.filter(featured=True)[:SLIDER_MAX_PRODUCTS]
        products_popular = Product.objects.filter(popular=True)[:SLIDER_MAX_PRODUCTS]
        top_seller = Product.objects.filter(top_seller=True)[:SLIDER_MAX_PRODUCTS]
        all_products = Product.objects.all()[:SLIDER_MAX_PRODUCTS]
        offer = ConditionalOffer.objects.all()
        context["app_data"] = SiteData.objects.all()
        context["company_data"] = AboutCompany.objects.all()
        context["key"] = KeywordDiscription.objects.all()
        context["faq"] = Faq.objects.all()
        context["products_featured"] = products_featured
        context["products_popular"] = products_popular
        context["offer"] = offer
        context["best_seller"] = top_seller
        context["all_products"] = all_products
        context["form"] = form

        return context

    def get_success_url(self):
        messages.success(self.request, "Successfully Subscribed")
        return reverse("home:index")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status
        code along with name of the user
        """
        email = form.cleaned_data["email"]
        form.save(commit=False)
        context = {"title": "Subscribe", "content": "Thank you to Subscribe !"}
        from_mail = settings.EMAIL_HOST_USER
        template_name = "email/emails." + app_setting.TEMPLATE_EXTENSION
        to_mail = email
        subject = "Thank you to Subscribe!"
        SendHTMLMail(subject, context, template_name, to_mail, from_mail)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors
        products_featured = Product.objects.filter(featured=True)[:SLIDER_MAX_PRODUCTS]
        products_popular = Product.objects.filter(popular=True)[:SLIDER_MAX_PRODUCTS]
        top_seller = Product.objects.filter(top_seller=True)[:SLIDER_MAX_PRODUCTS]
        all_products = Product.objects.all()[:SLIDER_MAX_PRODUCTS]
        offer = ConditionalOffer.objects.all()

        context = {
            "form": form,
            "errors": errors,
            "app_data": SiteData.objects.all(),
            "company_data": AboutCompany.objects.all(),
            "key": KeywordDiscription.objects.all(),
            "faq": Faq.objects.all(),
            "products_featured": products_featured,
            "products_popular": products_popular,
            "offer": offer,
            "best_seller": top_seller,
            "all_products": all_products,
            "form": form,
        }
        for error in errors:
            messages.error(self.request, f"Please Check - {error} & Try Again ")
            return render(self.request, self.template_name, context)


class TermsView(generic.TemplateView):
    template_name = "home/terms_conditions.html"

    def get_context_data(self, **kwargs):
        context = super(TermsView, self).get_context_data(**kwargs)

        context["app_data"] = SiteData.objects.all()
        context["company_data"] = AboutCompany.objects.all()
        context["key"] = KeywordDiscription.objects.all()

        return context


# def send_email(request):
#     return render_to_response('oscar/customer/emails/commtype_registration_body.html')


# def print_page(request):
#     return render_to_response('oscar/partials/print_page_pdf.html')
def SendHTMLMail(subject, context, template_name, to_mail, from_mail):
    """Html Send Through Email"""
    context = context
    subject = subject
    html_content = render_to_string(template_name, context)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject, text_content, from_mail, [to_mail])
    email.attach_alternative(html_content, "text/html")
    return email.send()
