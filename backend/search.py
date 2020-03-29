link1 = {
    "url":"https://cvs.com",
    "title":"cvs",
    "about":"Local health spot",
    "tags":"cvs, drugstore, cvs health"
}

link2 = {
    "url":"https://reddit.com",
    "title":"reddit",
    "about":"Front page of the internet",
    "tags":"liberal content, memes"
}

links = [link1,link2]

def search(search_term:str):
    inverted_index = {}
    for link in links:
        for term in link.values():
            print(term)
            inverted_index[term]=link
    results = [inverted_index[search_term]]
    print(results)
    return results


