from django.contrib.auth.views import PasswordResetView
from django.utils import timezone
from django.http import HttpResponseForbidden
from datetime import timedelta

class RateLimitedPasswordResetView(PasswordResetView):
    def dispatch(self, request, *args, **kwargs):
        last_sent = request.session.get('last_password_reset_time')
        if last_sent:
            last_sent_time = timezone.datetime.fromisoformat(last_sent)
            if timezone.now() - last_sent_time < timedelta(minutes=2):  # limit to once every 2 minutes
                return HttpResponseForbidden("Too many reset requests. Try again later.")
        request.session['last_password_reset_time'] = timezone.now().isoformat()
        return super().dispatch(request, *args, **kwargs)
