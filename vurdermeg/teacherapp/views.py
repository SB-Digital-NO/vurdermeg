"""Views for teacherapp."""
from datetime import datetime

from baseapp.models import Assessment
from django.views.generic import FormView, ListView


class TeacherHome(ListView):
    template_name = "t_home.html"

    def get_queryset(self):
        # modifies the method that retrives the queryset object used to create the SQL-statements.
        self.now = datetime.now()
        return Assessment.objects.filter(group_id__members=self.request.user).filter(
            expiry_time__gt=self.now
        )


class TeacherNewAssessment(FormView):
    pass
