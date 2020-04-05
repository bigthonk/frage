class Search():

    def __init__(self, links):
        self.links = links
        self.inverted_index = self.build_index(links)

    def build_index(self,data):
        inverted_index = {}
        for entry in data:
            for term in entry.values():
                inverted_index[term]=entry
        return inverted_index

    def inverted_index_search(self,search_term):
        results = [self.inverted_index[search_term]]
        return results

    def list_search(self,search_term):
        results = []
        for data in self.links:
            data_entries = set(data.values())
            for entry in data_entries:
                if search_term in entry:
                    results = results = results + [data]
                    break
        return results
