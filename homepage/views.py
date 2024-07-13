from django.shortcuts import render,redirect,get_object_or_404
from .models import Dictionary
from .forms import DictionaryForm,DictionaryForm2
from django.core.paginator import Paginator

def dictionary_list(request):
    query = request.GET.get('q', '')  # Get the search query from URL parameter 'q'
    if query:
        # If there is a query, filter Dictionary objects where 'word' contains (case-insensitive) the query
        results = Dictionary.objects.filter(word__icontains=query)
    else:
        # If there is no query, return an empty queryset (no results)
        results = Dictionary.objects.none()
    
    # At this point, 'results' contains either a filtered queryset based on the search query,
    # or an empty queryset if no search query was provided.
    
    # Typically, this function would then pass 'results' to a template for rendering.
    # For example:
    # return render(request, 'template_name.html', {'results': results})
    

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



# Define the view function for editing a dictionary entry
def edit_dictionary(request, id):
    # Retrieve the Dictionary entry with the given id or return a 404 error if not found
    entry = get_object_or_404(Dictionary, pk=id)

    # Check if the request method is POST, which means the form has been submitted
    if request.method == 'POST':
        # Create a form instance with the POST data and the specific entry to be updated
        form = DictionaryForm2(request.POST, instance=entry)
        # Check if the form data is valid
        if form.is_valid():
            # Save the updated entry to the database
            form.save()
            # Redirect to the 'dictionary_list' view after saving
            return redirect('dictionary_list')
    else:
        # If the request method is not POST, create a form instance for the existing entry without any changes
        form = DictionaryForm2(instance=entry)

    # Render the 'edit_list.html' template with the form and entry context
    return render(request, 'edit_list.html', {'form': form, 'entry': entry})





