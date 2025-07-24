# main.py
from crewai import Crew, Process
from agents import AINewsLetterAgents
from tasks import AINewsLetterTasks
from litellm import completion
from file_io import save_markdown
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the agents and tasks
agents = AINewsLetterAgents()
tasks = AINewsLetterTasks()

model = "gemini/gemini-1.5-flash"

# Instantiate the agents
editor = agents.editor_agent(llm = model)
news_fetcher = agents.news_fetcher_agent(llm = model)
news_analyzer = agents.news_analyzer_agent(llm = model)
newsletter_compiler = agents.newsletter_compiler_agent(llm = model)

# Instantiate the tasks
fetch_news_task = tasks.fetch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fetch_news_task])
compile_newsletter_task = tasks.compile_newsletter_task(
    newsletter_compiler, [analyze_news_task], save_markdown)

# Form the crew
crew = Crew(
    agents=[editor, news_fetcher, news_analyzer, newsletter_compiler],
    tasks=[fetch_news_task, analyze_news_task, compile_newsletter_task],
    process=Process.sequential,
    manager_llm=model,
    verbose=True
)

# Kick off the crew's work
results = crew.kickoff()

# Print the results
print("Crew Work Results:")
print(results)