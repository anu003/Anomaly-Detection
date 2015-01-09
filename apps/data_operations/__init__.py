from apps.data_operations.create_data import CreateData
import settings

__author__ = 'cenk'

if __name__ == "__main__":
    klass = CreateData(**{'log_active': settings.LOG})
    # klass.command()
    klass.write_to_csv()
