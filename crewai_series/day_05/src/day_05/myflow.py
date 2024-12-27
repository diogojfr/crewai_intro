import asyncio

from crewai.flow.flow import Flow, listen, start, or_, and_ 
from litellm import completion
from dotenv import load_dotenv
import os
from crew import Day05Crew
from pydantic import BaseModel

load_dotenv()

class News(BaseModel):
    news: str = ""

class NewsFlow(Flow[News]):
    model = "ollama/mistral:latest"

    @start()
    def generate_news_topic(self):
        print("Starting flow... generating news topic")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": """Return a topic within the ai world that is trending.
                    This should be 1 - 4 words long.""",
                },
            ],
            api_base = "http://localhost:11434"
        )

        news_topic = response["choices"][0]["message"]["content"]

        print(f"News Topic: {news_topic}")

        return news_topic
    
    @listen(generate_news_topic)
    def generate_news(self, news_topic):
        print(f"Generating news for topic: {news_topic}")

        inputs = {
            'topic': news_topic
        }
        result = Day05Crew().crew().kickoff(inputs=inputs)

        # get raw output then save to state
        output = result.raw
        self.state.news = output

        return output
    
    @listen(generate_news)
    def save_news(self, news):
        print("Saving news to file...")

        # create the news directory if it doesn't exist
        news_dir = os.path.join(os.path.dirname(__file__), "..", "..", "news")
        os.makedirs(news_dir, exist_ok=True)

        # save the news in the news directory
        news_file_path = os.path.join(news_dir, "news_day5.md")
        with open(news_file_path, "w") as f:
            f.write(news)

        print(f"News saved to {news_file_path}")


    @listen(generate_news)
    def generate_best_news(self, input):
        print("Generating best news...")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Choose the most important news from the following and return it: {input}",
                },
            ],
            api_base = "http://localhost:11434"
        )

        important_news = response["choices"][0]["message"]["content"]
        return important_news
    
    
    @listen(and_(generate_news_topic, generate_news, save_news, generate_best_news))
    def logger(self, result):
        print(f"Logger: {result}")
        print("*" * 100)
        print("Now you can find the news in the news directory!")



# async def main():
#     flow = NewsFlow()
#     flow.plot("my_flow_plot")

#     await flow.kickoff()

# asyncio.run(main())

def main():
    flow = NewsFlow()
    flow.plot("my_flow_plot")

    flow.kickoff()

if __name__ == "__main__":
    main()