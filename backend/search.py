class Search():

    def __init__(self, links):
        self.links = links
        self.inverted_index = self.build_index(links)

    def build_index(self,data):
        inverted_index = {}
        for entry in data:
            title = entry['title'].split('(')[0]
            title_words = title.split()
            for word in title_words:
                if word in inverted_index:
                    inverted_index[word] = inverted_index[word] + [entry]
                else :
                    inverted_index[word]= [entry]
        return inverted_index

    def inverted_index_search(self,search_term):
        try:
            results = self.inverted_index[search_term]
            return results
        except:
            return []

    def list_search(self,search_term):
        results = []
        for data in self.links:
            data_entries = set(data.values())
            for entry in data_entries:
                if search_term in entry:
                    results = results = results + [data]
                    break
        return results
