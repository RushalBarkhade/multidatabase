class Router:
    def db_for_read(self, model, **hints):
        return 'read_db'