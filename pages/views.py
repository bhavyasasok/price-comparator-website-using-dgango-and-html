from django.shortcuts import redirect, render
from product.models import Order, Product  # Ensure Order and Product are imported
from django.db.models import Q, Max, Sum
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CreateUserForm
from product.models import Customer


# Create your views here.

def home_page_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, defaults={})  # ✅ Fixed syntax
        cartTotal = order.orderitem_set.aggregate(sum=Sum('quantity'))['sum'] or ''
    else:
        cartTotal = ''

    context = {'cartTotal': cartTotal}
    return render(request, "home.html", context)

def help_page_view(request, *args, **kwargs):
    return render(request, "help.html")

def cheapest_price_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, defaults={})  # ✅ Fixed syntax
        items = order.orderitem_set.all()
        cartTotal = order.orderitem_set.aggregate(sum=Sum('quantity'))['sum'] or ''
    else:
        items = []
        cartTotal = ''
    
    context = {'items': items, 'cartTotal': cartTotal, 'order': order}
    return render(request, "cheapest_price.html", context)

def login_page_view(request, *args, **kwargs):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    return render(request, "login.html")

def register_page_view(request, *args, **kwargs):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            Customer.objects.create(user=new_user, name=new_user.username)  # Fixed `name`
            return redirect('login')

    context = {'form': form}
    return render(request, "register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def basket_page_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, defaults={})  # ✅ Fixed syntax
        items = order.orderitem_set.all()
        cartTotal = order.orderitem_set.aggregate(sum=Sum('quantity'))['sum'] or ''
    else:
        items = []
        cartTotal = ''
    
    context = {'items': items, 'cartTotal': cartTotal}
    return render(request, "basket.html", context)

def contents_page_view(request, *args, **kwargs):
    # Search items by name, store, and category
    products = Product.objects.all()
    
    if 'q' in request.GET:
        q = request.GET['q']
        products = products.filter(Q(name__icontains=q) | Q(store__icontains=q) | Q(category__icontains=q))
    
    # Price range filtering
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    if min_price.isdigit():
        min_price = int(min_price)
    else:
        min_price = 0

    if max_price.isdigit():
        max_price = int(max_price)
    else:
        max_price = Product.objects.aggregate(Max('price'))['price__max'] or 0

    products = products.filter(price__range=(min_price, max_price))

    # Store filtering
    stores = {'Tesco', 'Morrisons', 'Waitrose', 'Sainsburys'}
    selected_stores = {store for store in stores if request.GET.get(store)}

    if selected_stores:
        products = products.filter(store__in=selected_stores)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, _ = Order.objects.get_or_create(customer=customer, defaults={})  # ✅ Fixed syntax
        items = dict(order.orderitem_set.values_list('product_id', 'quantity'))
        cartTotal = order.orderitem_set.aggregate(sum=Sum('quantity'))['sum'] or ''
    else:
        items = {}
        cartTotal = ''

    context = {'products': products.order_by('name', 'price'), 'items': items, 'cartTotal': cartTotal}
    return render(request, "contents.html", context)
