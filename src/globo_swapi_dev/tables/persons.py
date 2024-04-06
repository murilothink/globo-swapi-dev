class Persons:
    def __init__(self, table_repository):
        self.table_repository = table_repository

 # Getter
    @property
    def table_repository(self):
        return self.table_repository

    # Setter
    @table_repository.setter
    def table_repository(self, new_df):
        self.table_repository = new_df