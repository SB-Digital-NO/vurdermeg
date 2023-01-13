"""Views for teacherapp."""
from datetime import datetime

from baseapp.models import Assessment, AssessmentGroup
from django.views.generic import ListView


class TeacherHome(ListView):
    template_name = "t_home.html"

    def get_queryset(self):
        # modifiserer metoden som henter queryset-objektet som skal oversettes til SQL-statements.
        self.now = datetime.now()
        return Assessment.objects.filter(group_id__members=self.request.user).filter(
            expiry_time__gt=self.now
        )
