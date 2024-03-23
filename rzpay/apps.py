from django.conf import settings
from django.core.checks import Warning, register
from django.urls import path
from django.utils.translation import gettext_lazy as _
from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class RzpayConfig(OscarConfig):
    # default_auto_field = "django.db.models.BigAutoField"
    # name = "rzpay"
    name = "rzpay"
    verbose_name = _("Rzpay")
    namespace = "rzpay"

    def ready(self):
        self.success_view = get_class("rzpay.views", "SuccessResponseView")
        self.cencel_view = get_class("rzpay.views", "CancelResponseView")
        self.payment_view = get_class("rzpay.views", "PaymentView")

    def get_urls(self):
        urls = [
            path(
                "preview/<int:basket_id>/",
                self.success_view.as_view(),
                name="razorpay-success-response",
            ),
            path(
                "cancel/<int:basket_id>/",
                self.cencel_view.as_view(),
                name="razorpay-cancel-response",
            ),
            path(
                "payment/",
                self.payment_view.as_view(),
                name="razorpay-direct-payment",
            ),
        ]
        return self.post_process_urls(urls)
