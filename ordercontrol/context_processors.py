from .models import OrderWindow

def order_status(request):
    order_window = OrderWindow.objects.first()
    return {'order_window': order_window}