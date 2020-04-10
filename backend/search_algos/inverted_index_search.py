from search_algos.base_search import BaseSearch

class Inverted_Index_Search(BaseSearch):

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
                results = self.index[search_term]
                return results
            except:
                return []

        def search(self,search_term):
            return self.inverted_index_search(search_term)
