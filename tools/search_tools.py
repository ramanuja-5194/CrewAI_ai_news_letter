# search_tools.py
import json
import os
import requests
from crewai.tools import BaseTool

class SearchTool(BaseTool):
    # NEW: Define the tool's name and description as class attributes
    name: str = "Search the internet"
    description: str = "Useful to search the internet about a given topic and return relevant results"

    def _run(self, query: str) -> str:
        """The main logic for the tool goes here."""
        print("Searching the internet...")
        top_result_to_return = 5
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query, "num": top_result_to_return, "tbm": "nws"})
        headers = {
            'X-API-KEY': os.environ['SERPER_API_KEY'],
            'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)

        # Check for results
        if 'organic' not in response.json() or not response.json()['organic']:
            return "Sorry, I couldn't find anything about that. There could be an error with your Serper API key or no results were found."

        results = response.json()['organic']
        string = []
        for result in results[:top_result_to_return]:
            try:
                date = result.get('date', 'Date not available')
                string.append('\n'.join([
                    f"Title: {result['title']}",
                    f"Link: {result['link']}",
                    f"Date: {date}",
                    f"Snippet: {result['snippet']}",
                    "\n-----------------"
                ]))
            except KeyError:
                continue
        
        return '\n'.join(string)

# import json
# import os
# import requests
# from langchain.tools import tool

# class SearchTools():

#     @tool("Search the internet")
#     def search_internet(self, query: str): # <-- Add 'self' here
#         """Useful to search the internet
#         about a a given topic and return relevant results"""
#         print("Searching the internet...")
#         top_result_to_return = 5
#         url = "https://google.serper.dev/search"
#         payload = json.dumps(
#             {"q": query, "num": top_result_to_return, "tbm": "nws"})
#         headers = {
#             'X-API-KEY': os.environ['SERPER_API_KEY'],
#             'content-type': 'application/json'
#         }
#         response = requests.request("POST", url, headers=headers, data=payload)
        
#         # Check if there is an organic key
#         if 'organic' not in response.json():
#             return "Sorry, I couldn't find anything about that, there could be an error with your serper api key."
#         else:
#             results = response.json()['organic']
#             string = []
#             print("Results:", results[:top_result_to_return])
#             for result in results[:top_result_to_return]:
#                 try:
#                     date = result.get('date', 'Date not available')
#                     string.append('\n'.join([
#                         f"Title: {result['title']}",
#                         f"Link: {result['link']}",
#                         f"Date: {date}",
#                         f"Snippet: {result['snippet']}",
#                         "\n-----------------"
#                     ]))
#                 except KeyError:
#                     continue  # Using 'continue' is more explicit than 'next'

#             return '\n'.join(string)