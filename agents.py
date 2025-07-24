from crewai import Agent
#Import the new SearchTool class
from tools.search_tools import SearchTool

#Instantiate the new tool class
search_tool = SearchTool()

class AINewsLetterAgents():
    def editor_agent(self,llm):
        return Agent(
            role='Editor',
            goal='Oversee the creation of the AI Newsletter',
            backstory="""With a keen eye for detail and a passion for storytelling, you ensure that the newsletter
            not only informs but also engages and inspires the readers. """,
            allow_delegation=True,
            verbose=True,
            llm = llm,
            max_iter=15
        )

    def news_fetcher_agent(self,llm):
        return Agent(
            role='NewsFetcher',
            goal='Fetch the top AI news stories for the day',
            backstory="""As a digital sleuth, you scour the internet for the latest and most impactful developments
            in the world of AI, ensuring that our readers are always in the know.""",
            # Pass the instantiated tool directly
            tools=[search_tool],
            verbose=True,
            allow_delegation=True,
            llm = llm,
        )

    def news_analyzer_agent(self,llm):
        return Agent(
            role='NewsAnalyzer',
            goal='Analyze each news story and generate a detailed markdown summary',
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful
            analyses of AI news stories, making them accessible and engaging for our audience.""",
            # Pass the instantiated tool directly
            tools=[search_tool],
            verbose=True,
            allow_delegation=True,
            llm = llm,
        )

    def newsletter_compiler_agent(self,llm):
        return Agent(
            role='NewsletterCompiler',
            goal='Compile the analyzed news stories into a final newsletter format',
            backstory="""As the final architect of the newsletter, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that captivates our readers. Make sure to follow
            newsletter format guidelines and maintain consistency throughout.""",
            verbose=True,
            llm = llm,
        )