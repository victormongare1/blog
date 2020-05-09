import urllib.request,json
from .models import Quote

quote_url=None
def configure_request(app):
  '''
  function to configure url globally
  '''
  global quote_url
  quote_url = app.config['QUOTE_URL']

def get_quote():
  '''
  function that returns a json response to url request
  '''
  get_quote_url = quote_url
  print(get_source_url)
  with urllib.request.urlopen(get_quote_url) as url:
    get_quote_data = url.read()
    get_quote_response = json.loads(get_quote_data)

    quote_results = None

    if get_quote_response:
      quote_results_list = get_quote_response
      quote_results = process_results(quote_results_list)


  return quote_results