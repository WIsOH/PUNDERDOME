from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

# Create your views here.

def get_name(request):
	if request.metho == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('outpun.html')
	else:
		form = NameForm()

	return render(request, 'index.html', {'form': form})
