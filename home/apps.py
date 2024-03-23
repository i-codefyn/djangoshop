from django.conf import settings
from django.core.checks import Warning, register
from django.urls import path
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class HomeConfig(OscarConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"

    verbose_name = _("home")

    namespace = "home"

    def ready(self):
        self.home_page_view = get_class("home.views", "HomePageView")
        self.feedback_view = get_class("home.views", "FeedBackFormView")
        self.contact_view = get_class("home.views", "ContactFormView")
        # self.subscribe_view = get_class("home.views", "SubscribeFormView")
        self.faq_view = get_class("home.views", "FaqsView")
        self.terms_view = get_class("home.views", "TermsView")
        # self.disclamer_view = get_class("home.views", "DisclamerView")
        # # self.detail_view = get_class('home.views', 'StoreDetailView')

    def get_urls(self):
        urls = [
            path("", self.home_page_view.as_view(), name="index"),
            # path("subcribe/", self.subscribe_view.as_view(), name="subscribe"),
            path("feedback/", self.feedback_view.as_view(), name="feedback"),
            path("contact/", self.contact_view.as_view(), name="contact"),
            path("faqs/", self.faq_view.as_view(), name="faq"),
            path("terms/", self.terms_view.as_view(), name="terms"),
            # path("disclamer/", self.disclamer_view.as_view(), name="disclamer"),
            # # path(
            # #     "<slug:dummyslug>/<int:pk>/", self.detail_view.as_view(), name="detail"
            # ),
        ]
        return self.post_process_urls(urls)
