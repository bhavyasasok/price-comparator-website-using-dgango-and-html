import requests
from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = "Convert all product prices from USD to INR"

    def get_exchange_rate(self):
        """Fetch the latest USD to INR exchange rate."""
        try:
            response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
            data = response.json()
            return data["rates"]["INR"]  # Get INR conversion rate
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Error fetching exchange rate: {e}"))
            return None

    def handle(self, *args, **kwargs):
        exchange_rate = self.get_exchange_rate()
        if not exchange_rate:
            self.stderr.write(self.style.ERROR("Could not fetch exchange rate. Exiting."))
            return

        products = Product.objects.all()
        updated_count = 0

        for product in products:
            if product.price and product.price > 0:  # Ensure price exists
                new_price = round(float(product.price) * exchange_rate, 2)  # Convert Decimal to float before multiplication
                product.price = new_price
                product.save()
                updated_count += 1

        self.stdout.write(self.style.SUCCESS(f"Updated {updated_count} product prices to INR!"))
