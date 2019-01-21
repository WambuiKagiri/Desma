from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import generic

#imported forms
from .forms import subscribe_form
from .forms import list_form
from .forms import customer_form
from .forms import booking_form

#imported models
from .models import subscriber
from .models import listings_waiting_list
from .models import customer
from .models import booked_viewings
from .models import properties



import re

from django.db.models import Q

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term        
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

class HomePageView(TemplateView):
	def get(self, request, **kwargs):
		propertyy = properties.objects.all()
		# print (propertyy)
		return render(request, 'index.html', {'propertyy':propertyy})

	

class SearchPageView(TemplateView):
	def get(self,request, **kwargs):
		return render(request, 'searchresults.html')

	def post(self, request, **kwargs):
		if request.method == 'POST':
			form = subscribe_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('success/')

		else:
			return render(request, 'success.html', {'form':form})

	def search(request):
		query_string = ""
		found_entries = None
		if ('q' in request.GET) and request.GET['q'].strip():
			query_string = request.GET['q']
			entry_query = get_query(query_string, ['rent_buy', 'property_type','location'])
			found_entries = Entry.objects.filter(entry_query).order_by('-property_id')
		return render_to_response('searchresults.html',
                          { 'query_string': query_string, 'found_entries': found_entries },
                          context_instance=RequestContext(request))



class AboutPageView(TemplateView):
	def get(self, request, **kwargs): 
		return render(request, 'about.html', context=None)
		
class ContactPageView(TemplateView):
	def get(self, request, **kwargs): 
		return render(request, 'contact.html', context=None)

	def post(self,request, **kwargs):
		if request.method == 'POST':
			form = customer_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/success/')

		else:
			return render(request, 'success.html', {'form':form})	

class ListPropertyPageView(TemplateView):
	def get(self, request, **kwargs): 
		return render(request, 'ListProperty.html', context=None)

	def post(self,request, **kwargs):
		if request.method == 'POST':
			form = list_form(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('/success/')

		else:
			return render(request, 'success.html', {'form':form})

class PropertyPageView(TemplateView):
	def get(self, request, property_title, **kwargs): 
		propertyy = properties.objects.all().filter(property_title=property_title)
	
		return render(request, 'property.html', {'propertyy':propertyy})	
	def index(request):
		'Display map'
		return render(request, 'property.html', {})

class SuccessPageView(TemplateView):
 	def get(self, request, **kwargs): 
 		return render(request, 'success.html', context=None)
		
class BookViewingPageView(TemplateView):
 	def get(self, request, property_title, **kwargs):
 		propertyy = properties.objects.all().filter(property_title=property_title) 
 		return render(request, 'BookViewing.html', {'propertyy':propertyy})
 	def test_session(request):
 		request.session.set_test_cookie()
 		return HttpResponse('/success/')

 	def post(self,request, **kwargs):
 		if request.method=='POST':
 			form = booking_form(request.POST)
 			if form.is_valid():
 				form.save()
 				return HttpResponseRedirect('/success/')
 		else:
 			return render(request,'BookViewing.html',{'form':form})
 			
class LatestPageView(TemplateView):
	def get(self, request, **kwargs):
		propertyy = properties.objects.all()
		return render(request, 'index.html', {'propertyy':propertyy})