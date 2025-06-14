from django.contrib.auth.views import PasswordResetView
from django.utils import timezone
from datetime import timedelta

class RateLimitedPasswordResetView(PasswordResetView):
    cooldown = timedelta(minutes=2)

    def form_valid(self, form):
        last = self.request.session.get('last_password_reset')
        now = timezone.now()
        if last:
            last_dt = timezone.datetime.fromisoformat(last)
            if now - last_dt < self.cooldown:
                # Too soon: add a non‑field error and re‑render form
                wait = int((self.cooldown - (now - last_dt)).total_seconds() // 60) + 1
                form.add_error(None, f"Please wait {wait} minute(s) before requesting again.")
                return self.form_invalid(form)
        # Record the timestamp and send email
        self.request.session['last_password_reset'] = now.isoformat()
        return super().form_valid(form)
