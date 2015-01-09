from apps.data_operations.create_data import CreateData

__author__ = 'cenk'

if __name__ == "__main__":
    klass = CreateData(**{'log_active': True})
    # klass.command()
    klass.write_to_csv()