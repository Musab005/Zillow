URL = "https://www.zillow.com/async-create-search-page-state"


def new_url(query, new_page_number):
    query['searchQueryState']['pagination']['currentPage'] = new_page_number
    return query
