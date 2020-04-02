from django.views.generic import *
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.template.loader import render_to_string
from weasyprint import HTML, CSS

from django.core.files.storage import FileSystemStorage


from cvdata.forms import *
from cvdata.models import *


# from .models import CVData




class CVDataView(FormView):
    template_name = 'cvdata/cvdata.html'
    form_class = CVDataForm
    success_url = reverse_lazy('cvdata:test')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        if form.is_valid():
            form.save()
        return super().form_valid(form)





def html_to_pdf_view(request):
    cv = CVData.objects.last()
    print(cv)
    html_string = render_to_string('cvdata/pdf_templates.html', {'cv': cv})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response