from googleapiclient.discovery import build

api_key = "AIzaSyDyejqwjpN248pJrZT3oRN6SoCKjwprbHw" 
cse_id = "161bdd12fdd194cd5"  

def google_search(query):
    try:
        # Initialize the API client
        service = build("customsearch", "v1", developerKey=api_key)
        
        # Make the search request
        res = service.cse().list(q=query, cx=cse_id).execute()
        
        # Extract and return the results
        results = res.get("items", [])
        if not results:
            return "No results found."
        
        # Return the first result's title and link
        first_result = results[0]
        title = first_result.get("title")
        link = first_result.get("link")
        return f"Title: {title}\nLink: {link}"
    
    except Exception as e:
        return f"An error occurred: {e}"    
