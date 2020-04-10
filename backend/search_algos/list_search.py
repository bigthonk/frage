from search_algos.base_search import BaseSearch

class List_Search(BaseSearch):

        def __init__(self, data):
            self.index = self.build_index(data)

        def build_index(self,data):
            return data

        def list_search(self,search_term):
            results = []
            for data in self.index:
                data_entries = set(data.values())
                for entry in data_entries:
                    if search_term in entry:
                        results = results = results + [data]
                        break
            return results

        def search(self, search_term):
            return self.list_search(search_term)
