from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q # new
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from .forms import MachineForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView


from .models import Machines

class SearchResultsView(ListView):
	model = Machines
	template_name = 'search_results.html'

	def get_queryset(self):
		query_hostname = self.request.GET.get('q_hostname')
		
		query_ipv4 = self.request.GET.get('q_ipv4')
		query_location = self.request.GET.get('q_location')
		query_ipv6 = self.request.GET.get('q_ipv6')
		query_os = self.request.GET.get('q_os')
		query_physical_virtual = self.request.GET.get("q_physical_virtual")
		query_owner = self.request.GET.get('q_owner')
		query_administrator = self.request.GET.get('q_administrator')
		query_uofa_tag = self.request.GET.get('q_uofa_tag')
		query_model = self.request.GET.get('q_model')
		query_processor = self.request.GET.get('q_processor')
		query_ram = self.request.GET.get('q_ram')
		query_storage = self.request.GET.get('q_storage')
		query_gpu = self.request.GET.get('q_gpu')
		query_serial_number = self.request.GET.get('q_serial_number')
		query_status = self.request.GET.get('q_status')
		query_rack = self.request.GET.get('q_rack')
		query_powerup = self.request.GET.get('q_powerup')
		query_support = self.request.GET.get('q_support')
		query_department = self.request.GET.get('q_department')
		query_srit_access = self.request.GET.get('q_srit_access')
		query_comments = self.request.GET.get('q_comments')



		return Machines.objects.filter(
			Q(hostname__icontains=query_hostname) &
			Q(ipv4__icontains=query_ipv4) &
			Q(last_known_location__icontains=query_location) &
			Q(ipv6__icontains=query_ipv6) &
			Q(operating_system__icontains=query_os) &
			Q(physical_virtual_machine__icontains=query_physical_virtual) &
			Q(owner__icontains=query_owner) &
			Q(administrator__icontains=query_administrator) &
			Q(u_of_a_tag_number__icontains=query_uofa_tag) &
			Q(make_model__icontains=query_model) &
			Q(processor__icontains=query_processor) &
			Q(ram_gb_field__icontains=query_ram) &
			Q(storage_space_gb_field__icontains=query_storage) &
			Q(gpu__icontains=query_gpu) &
			Q(serial_number__icontains=query_serial_number) &
			Q(status__icontains=query_status) &
			Q(rack_number__icontains=query_rack) &
			Q(power_up__icontains=query_powerup) &
			Q(support_team__icontains=query_support) &
			Q(department__icontains=query_department) &
			Q(srit_access__icontains=query_srit_access) &
			Q(comments__icontains=query_comments)
		)

@login_required
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

#here the machine pk is now its HOSTNAME instead of the DB's primary is a STR of number lettering
#gotta work this out

@login_required
def machine_add(request):
	if request.method == "POST":
		form = MachineForm(request.POST)
		if form.is_valid:
			machine = form.save(commit=False)
			machine.id_machine = machine.hostname
			machine.save()
			return redirect('machine_edit', pk=machine.pk)
	else:
		form = MachineForm()
	return render(request, 'machine_add.html', {'form': form})

def machine_delete(request, pk):
	machine = get_object_or_404(Machines, pk=pk)
	if request.method == "POST":
		machine.delete()
		return HttpResponseRedirect(request.POST.get('next', '/'))


