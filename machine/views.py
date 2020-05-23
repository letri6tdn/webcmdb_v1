from django.shortcuts import render, get_object_or_404
from django.db.models import Q # new

from django.views.generic import TemplateView, ListView
from .forms import MachineForm


from .models import Machines

class SearchResultsView(ListView):
	model = Machines
	template_name = 'search_results.html'

	def get_queryset(self):
		query = self.request.GET.get('q_hostname')
		return Machines.objects.filter(Q(hostname__icontains=query))

def machine_edit(request, pk):
	machine = get_object_or_404(Machines, pk=pk)
	if request.method == "POST":
		form = MachineForm(request.POST, instance=machine)
		if form.is_valid():
			machine = form.save(commit=False)
			machine.save()

	else:
		form = MachineForm(instance=machine)
	return render(request, 'machine_edit.html', {'form': form})