from django.shortcuts import render
from .form import WeldNumberForm
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context


# Create your views here.


def index(request):
    form_class = WeldNumberForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            qc_person = request.POST.get(
                'qc_person'
                , '')
            dpl_number = request.POST.get(
                'dpl'
                , '')
            weld_number = request.POST.get(
                'weld_number'
                , '')
            xray_status = request.POST.get(
                'xray_status'
                , '')
            status = request.POST.get(
                'status'
                , '')
            return redirect('/weldNumber/',)

    return render(request, '/home/swapnil/PycharmProjects/weldingqc/weldTracker/templates/weldTracker/weldNumber.html', {
        'weld_form': form_class,
    })