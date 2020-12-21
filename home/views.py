from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request , 'index.html')

def remove_punk(request):
    text = request.GET.get('text')
    check_box_remove_punk = request.GET.get('remove_punk' ,'off')
    uppercase = request.GET.get('uppercase' , 'off')
    lowercase = request.GET.get('lowercase' , 'off')
    new_line = request.GET.get('newline' , 'off')
    extra_space = request.GET.get('extraspace' , 'off')
    capitalize = request.GET.get('capitalize' , 'off')

    analyzed = ''
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    word_count = text.count(' ')
    charecter_count = len(text)


    if check_box_remove_punk == 'on':
        for charecter in text:
            if charecter not in punctuations:
                analyzed = analyzed + charecter 
        text = analyzed
                

    if uppercase =='on':
        analyzed = text.upper()
        text = analyzed

    

    if lowercase == 'on':
        analyzed = text.lower()
        text = analyzed

    if new_line == 'on':
        tmp = text.split()
        analyzed = ' '.join(tmp)
        text = analyzed

    if extra_space == 'on':
        tmp = text.split()
        analyzed = ' '.join(tmp)
        text = analyzed

    if capitalize =="on":
        analyzed = text.capitalize()
        text = analyzed

    if check_box_remove_punk != 'on' and uppercase != 'on' and lowercase != 'on' and new_line != 'on' and extra_space != 'on' and capitalize !='on':
        return HttpResponse('<h1>Select any of oporations</h1><a href="/"><button>Go to home</button></a>')

    return render(request, 'index.html' , context={'result' : analyzed , 'word_count':word_count , 'charecter_count': charecter_count})