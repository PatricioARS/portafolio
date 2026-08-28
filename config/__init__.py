import django.db.backends.mysql.base

django.db.backends.mysql.base.DatabaseWrapper.check_database_version_supported = lambda self: None