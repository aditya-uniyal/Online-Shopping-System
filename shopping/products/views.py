from django.shortcuts import render

# Create your views here.
def cap(request):
	context = {}
	template = 'cap.html'
	return render(request,template,context)


def glass(request):
	context = {}
	template = 'glass.html'
	return render(request,template,context)


def jackets(request):
	context = {}
	template = 'jackets.html'
	return render(request,template,context)


def jeans(request):
	context = {}
	template = 'jeans.html'
	return render(request,template,context)


def shoes(request):
	context = {}
	template = 'shoes.html'
	return render(request,template,context)


def slippers(request):
	context = {}
	template = 'slippers.html'
	return render(request,template,context)


def tshirt(request):
	context = {}
	template = 'tshirt.html'
	return render(request,template,context)

	
def watch(request):
	context = {}
	template = 'watch.html'
	return render(request,template,context)
