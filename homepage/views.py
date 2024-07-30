from django.shortcuts import render,redirect,get_object_or_404
from .models import Dictionary
from .forms import DictionaryForm,DictionaryForm2
from django.core.paginator import Paginator

def dictionary_list(request):
    query = request.GET.get('q', '')  
    if query:
        
        results = Dictionary.objects.filter(word__icontains=query)
    else:
        
        results = Dictionary.objects.none()

    paginator = Paginator(results,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'list.html', {'page_obj': page_obj, 'query': query})


def add_dictionary(request):
    if request.method == 'POST':
        form = DictionaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dictionary_list')
    else:
        form = DictionaryForm()

    return render(request,'add_list.html',{'form':form})
        


def delete_dictionary(request, id):
    entry = get_object_or_404(Dictionary, pk=id)
    entry.delete()
    return redirect('dictionary_list') 




def edit_dictionary(request, id):

    entry = get_object_or_404(Dictionary, pk=id)
    if request.method == 'POST':
        form = DictionaryForm2(request.POST, instance=entry)

        if form.is_valid():

            form.save()

            return redirect('dictionary_list')
    else:
        form = DictionaryForm2(instance=entry)


    return render(request, 'edit_list.html', {'form': form, 'entry': entry})





