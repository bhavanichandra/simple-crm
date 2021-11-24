class MarketingCloudRoutes:
    """
    This router is to control the database operations that will be done when using migrate commands.
    """
    route_app_labels = {'admin', 'auth', 'contenttypes', 'sessions', 'core'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read user_management models go to user_management.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'audit'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write user_auth models go to user_management.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'audit'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user_management app is involved.
        """
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the user_auth app only appears in the 'user_management'
        database.
        """
        if app_label in self.route_app_labels:
            return db == 'audit'
        return None