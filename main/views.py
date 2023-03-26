import base64
import io
import matplotlib.pyplot as plt

from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Articles, Plot



@login_required(login_url="/login")
def plot_stock_quantities(request):
    if request.method == 'POST':
        article_id = request.POST.get('article_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Retrieve data from the main_plots table
        data = Plot.objects.filter(article_id=article_id, date__gte=start_date, date__lte=end_date)

        # Extract the stock quantities and dates
        stock_quantities = [d.stock_quantity for d in data]
        dates = [d.date for d in data]

        # Create the plot
        plt.plot(dates, stock_quantities)
        plt.xlabel('Date')
        plt.ylabel('Stock Quantity')
        plt.title('Stock Quantities Plot')

        # Save the plot image to a buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        # Encode the plot image to base64 and include it in the context
        plot_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
        context = {'plot_stock_quantities': f'data:image/png;base64,{plot_image}'}

        return render(request, 'to_show/plots.html', context)

    return render(request, 'to_show/plots.html')


@login_required(login_url="/login")
def view_articles(request):
    query = request.GET.get('q')
    if query:
        table_data = Articles.objects.filter(article_label__icontains=query)
    else:
        table_data = Articles.objects.all()
    return render(request, 'to_show/articles.html', {'table_data': table_data})

@login_required(login_url="/login")
def view_plots(request):
    return render(request, 'to_show/plots.html')


def view_abouts(request):
    return render(request, 'main/abouts.html')


@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


