# OnlineShopping
Online Shopping Using Python Django Framework
I have learned django from Django 2 by Example, published by Packt and implement it.

Instructions and Navigations
All of the code is organized into folders. Each folder starts with a number followed by the application name. For example, Chapter01.

The code will look like the following:


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
