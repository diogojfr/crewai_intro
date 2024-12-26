from crewai_tools import BaseTool
import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv()

class CustomSerperDevTool(BaseTool):
    name: str = "Custom Serper Dev Tool"
    """Input schema for MyCustomTool."""

    description: str = "Search the internet for news."
    
    def _run(self, query: str) -> str:
        """
        Search the internet for news.
        """

        url = "https://google.serper.dev/news"

        payload = json.dumps({
            "q": query,
            "num":10,
            "autocorrect": False,
            "tbs": "qdr:d"
        })
        headers = {
        'X-API-KEY': os.getenv('SERPER_API_KEY'),
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        response_data = response.json()

        news_data = response_data.get('news', [])

        return json.dumps(news_data, indent=2)
        # return "This is a test"
