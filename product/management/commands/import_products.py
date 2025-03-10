import csv
import os
from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = "Import products from a CSV file into the database"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def clean_price(self, price):
        """Convert price string to a float, removing currency symbols."""
        if not price or price.strip() in ["—", ""]:
            return 0.00  # Default value for missing prices
        try:
            return float(price.replace("$", "").replace(",", "").strip())  # Remove $ and commas
        except ValueError:
            return 0.00  # Default to 0.00 if conversion fails

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs["csv_file"]

        if not os.path.exists(csv_file_path):
            self.stderr.write(self.style.ERROR(f"File not found: {csv_file_path}"))
            return

        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            products_added = 0

            for row in reader:
                try:
                    # Ensure only required fields are used
                    product_id = row.get("Product ID", "").strip()
                    name = row.get("Product Name", "").strip()
                    price = self.clean_price(row.get("Price", ""))
                    
                    # Skip rows without essential data
                    if not product_id or not name:
                        self.stdout.write(self.style.WARNING(f"Skipping row with missing ID or name: {row}"))
                        continue

                    # Create or update product
                    product, created = Product.objects.update_or_create(
                        product_id=product_id,
                        defaults={
                            "name": name,
                            "price": price,
                        }
                    )

                    if created:
                        products_added += 1

                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error processing row: {row}, {e}"))

        self.stdout.write(self.style.SUCCESS(f"Import complete! {products_added} new products added."))
