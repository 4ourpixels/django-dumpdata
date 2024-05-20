import os
import django


def main():
    # Set the Django settings module
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # Initialize Django
    django.setup()
    from rest_framework.renderers import JSONRenderer
    from myapp.serializers import ProductSerializer
    from myapp.models import Product

    def dump_products_to_json():
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_data = JSONRenderer().render(serializer.data)
        with open('serialized_products.json', 'wb') as f:
            f.write(json_data)
        print('Serializing completed')

    dump_products_to_json()


if __name__ == "__main__":
    main()
