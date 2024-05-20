import os
import django
import json


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    django.setup()
    from products.models import Brand
    with open('brand.json', 'r', encoding='utf-8') as json_file:
        data_list = json.load(json_file)
    for entry in data_list:
        fields = entry.get("fields", {})
        brand_instance = Brand(**fields)
        brand_instance.save()
    print('Brands saved to the Products table.')


if __name__ == "__main__":
    main()
