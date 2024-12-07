import requests

def google_search(query):
    api_key = "AIzaSyDyejqwjpN248pJrZT3oRN6SoCKjwprbHw"  # Your Google API Key
    cx = "161bdd12fdd194cd5"  # Your Custom Search Engine ID

    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        search_results = response.json()

        # Extract the top 5 search results
        results = []
        for item in search_results.get("items", []):
            title = item["title"]
            link = item["link"]
            results.append(f"{title}: {link}")

        return "\n".join(results)  # Return search result as a string
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"
