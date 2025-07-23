"""
WSGI config for the Quiz PortoEx application.

This module contains the WSGI application used by the production server.
"""

# Import the application from app.py
from app import app

# This is the application object that will be used by any WSGI server
application = app
