#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os  # Import os module
import sys  # Import sys module


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                          'BBG.settings')  # Set default Django settings module
    try:
        # Import execute_from_command_line function
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Raise ImportError if Django is not installed or not available
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)  # Execute Django management commands


if __name__ == '__main__':
    main()  # Run main function if the script is executed directly
