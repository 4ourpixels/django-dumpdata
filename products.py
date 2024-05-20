import os
import django
import json


def main():
    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Initialize Django
    django.setup()
    from products.models import Product, Type, Brand

    # Read the JSON data from the file
    with open('serialized_products.json', 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)

    # Create instances of Products and save them to the database
    for entry in data_list:
        fields = entry.get("fields", {})

        # Remove foreign key fields from the fields dictionary
        brand_id = fields.pop("brand")
        type_id = fields.pop("type")

        # Fetch the Brand instance
        try:
            brand_instance = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            print(f"Brand with id {brand_id} does not exist.")
            continue

        # Fetch the Type instance
        try:
            type_instance = Type.objects.get(id=type_id)
        except Type.DoesNotExist:
            type_instance = Type.objects.get(id=1)
            continue

        # Create the Product instance
        product_instance = Product(
            brand=brand_instance,
            type=type_instance,
            **fields
        )
        product_instance.save()

    print('Products saved to the database.')


if __name__ == "__main__":
    main()
