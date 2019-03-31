import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from catalog.models import Book, Author, BookInstance, Genre, Instagram, Verification
from catalog.forms import RenewBookForm, GetInstaUsername, Verificati

from multiprocessing import Pool

import sys
sys.path.insert(0, 'C:/Users/b_ozelsel/Documents/Follower/InstaPy')

from . import auth

@login_required
def index(request):

    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_books_with_h = Book.objects.filter(title__exact='Huseyin').count()    
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    
    context = {
        'num_books'                 : num_books,
        'num_instances'             : num_instances,
        'num_instances_available'   : num_instances_available,
        'num_authors'               : num_authors,
        'books_with_h'              : num_books_with_h,
        'num_visits'                : num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book

class BookDetailView(generic.DetailView):
    model = Book   

class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author     

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')

class LoanedBooksAllListView(PermissionRequiredMixin,generic.ListView):
    """Generic class-based view listing all books on loan. Only visible to users with can_mark_returned permission."""
    model = BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name ='catalog/bookinstance_list_borrowed_all.html'
    paginate_by = 10
    
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact='o').order_by('due_back')


@permission_required('catalog.can_mark_returned')
def renew_book_librarian(request, pk):
    """View function for renewing a specific BookInstance by librarian."""
    book_instance = get_object_or_404(BookInstance, pk = pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = form.cleaned_data['renewal_date']
            #quickstart.login("kodlamasanati", "berkemust02")
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date,})

    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
    
@login_required
def getusername(request):

    model = Instagram()

    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = GetInstaUsername(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            model.instauser = form.cleaned_data['instausername']
            model.instapass = form.cleaned_data['instapassword']
            model.user = request.user.username
            #pool = Pool(processes=1)
            #pool.map(quickstart.login, "asd")
            auth.Insta().login_user(form.cleaned_data['instausername'], form.cleaned_data['instapassword'])
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('index') )

    # If this is a GET (or any other method) create the default form
    else:
        form = GetInstaUsername()

    return render(request, 'catalog/instaloginpage.html', {'form':form})

def instaverif(request):

    model = Verification()

    if request.method == 'POST':

        form = Verificati(request.POST)

        if form.is_valid():
            model.verification = form.cleaned_data['verif']
            auth.Insta().verification("girisimsanati", form.cleaned_data['verif'])

            return HttpResponseRedirect(reverse('index'))
    
    else:
        form = Verificati()
    
    return render(request, 'catalog/instaverifpage.html', {'form':form})
