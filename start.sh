#!/bin/bash

gunicorn --bind 0.0.0.0:443 --workers 3 'flask_app:app'