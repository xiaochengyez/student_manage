from django.shortcuts import render

# Create your views here.
def report(request):
    return render(request, 'tester/test_report.html')

def case(request):
    return render(request, 'tester/test_case.html')

def interface(request):
    return render(request, 'tester/test_inerface.html')