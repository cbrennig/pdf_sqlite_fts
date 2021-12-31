from database.query import FullTextSearch
FTS = FullTextSearch()

search_term = input('search term: ')
start = time.time()
print(FTS.query(search_term))