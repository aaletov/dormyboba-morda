.PHONY: django-models
django-models:
	poetry run python3 manage.py inspectdb sent_token > invite/models.py
