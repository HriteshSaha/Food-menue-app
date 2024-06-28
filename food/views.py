from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import itemForm
from django.views.generic.list import ListView
from django.views .generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.


'''def index(request): # function based view for food list
    item_lst = Items.objects.all()
    # template = loader.get_template('food/index.html') # this line is not required if we directly use render() instead of HttpResponce(template.render(context, request))
    context = {
        'item_lst':item_lst
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html', context)'''

class Index_ClassBased(ListView): # Class based view for food list
    model = Items
    template_name = 'food/index.html'
    context_object_name = 'item_lst'

'''def details(request, item_id): # function based view for food details
    item = Items.objects.get(id= item_id)
    context = {
        'item':item
    }
    return render(request, 'food/detail.html', context)'''


class Detail_ClassBased(DetailView): # Class based view for food details
    model = Items
    template_name = "food/detail.html"


def mainpage(request): # index page
    return HttpResponse("<h2>This is the home page</h2>")

def add_item(request): # function based view for add item
    form = itemForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect("food:index")
    return render(request, 'food/item-form.html', {'form':form})

class CreateItem(CreateView):
    model = Items
    fields = ['item_name', 'item_desc', 'item_price', 'item_img']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


def update_item(request, id):
    item = Items.objects.get(id = id)
    form = itemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'item':item, 'form':form})

def delete_item(request, id):
    item = Items.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/delete-conf.html', {'item':item})