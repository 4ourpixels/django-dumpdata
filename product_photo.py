import os
import django
import json


def main():
    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Initialize Django
    django.setup()
    from products.models import ProductPhoto, Brand

    # Read the JSON data from the file
    with open('product_photo.json', 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)

    # Create instances of Products and save them to the database
    for entry in data_list:
        fields = entry.get("fields", {})

        # Remove foreign key fields from the fields dictionary
        brand_id = fields.pop("brand", None)

        # Fetch the Brand instance
        try:
            brand_instance = Brand.objects.get(id=brand_id)
        except Brand.DoesNotExist:
            print(f"Brand with id {brand_id} does not exist.")
            continue

        # Create the Product instance
        product_photo_instance = ProductPhoto(
            brand=brand_instance,
            **fields
        )
        product_photo_instance.save()

    print('Product photos saved to the database.')


if __name__ == "__main__":
    main()
