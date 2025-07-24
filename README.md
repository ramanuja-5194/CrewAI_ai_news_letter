# CrewAI AI News Letter Generator

This project leverages the CrewAI framework to autonomously fetch, analyze, and generate a daily AI-focused newsletter. It orchestrates a crew of specialized AI agents to collaborate on different aspects of news aggregation and content creation, ensuring a comprehensive and engaging output.

## Features

* **Automated News Fetching:** Automatically gathers top AI news stories from the past 24 hours from the internet.
* **Intelligent News Analysis:** Filters, prioritizes, and categorizes fetched news stories based on relevance and importance.
* **Hierarchical Agent Collaboration:** Utilizes a structured crew of agents (Editor, NewsFetcher, and ContentWriter) to streamline the newsletter generation process.
* **Dynamic Content Creation:** Generates engaging and informative content for the newsletter, including headlines, summaries, and deep dives into selected topics.
* **Markdown Output:** Saves the generated newsletter content in a clean and readable Markdown format, ready for publication.
* **Search Capabilities:** Integrates a custom tool for internet searching to gather up-to-date information.

## How It Works

The AI News Letter Generator operates with a crew of three distinct AI agents, each with specific roles and responsibilities to ensure efficient and high-quality newsletter production.

### Agents

* **Editor Agent**
    * **Role:** Oversees the entire newsletter creation process.
    * **Goal:** To ensure the newsletter is informative, engaging, and inspiring.
    * **Backstory:** A meticulous editor with a passion for storytelling, dedicated to delivering high-quality content.
    * **Delegation:** Can delegate tasks to other agents.

* **News Fetcher Agent**
    * **Role:** Specializes in finding the latest AI news.
    * **Goal:** To fetch the most relevant and breaking AI news from various online sources.
    * **Backstory:** A swift and efficient news scout, always on the lookout for fresh AI developments.
    * **Tools:** Utilizes the "Search the internet" tool.

* **Content Writer Agent**
    * **Role:** Crafts compelling and informative articles.
    * **Goal:** To write engaging content based on the fetched and analyzed news.
    * **Backstory:** A skilled writer capable of transforming raw information into captivating narratives.
    * **Tools:** Utilizes the "Search the internet" tool.

### Tasks

The agents collaborate through a series of well-defined tasks:

* **Fetch News Task:** The `News Fetcher Agent` retrieves top AI news stories from the past 24 hours, including titles, URLs, and brief summaries.
* **Analyze News Task:** The `Editor Agent` analyzes the fetched news stories to prioritize them, ensuring at least 5 relevant stories are selected and categorized as "Breaking News," "Feature Story," or "Quick Hit."
* **Write News Story Task:** For each selected news story, the `Content Writer Agent` drafts a concise and engaging article (maximum 3 paragraphs).
* **Review Newsletter Task:** The `Editor Agent` reviews the complete newsletter content for clarity, coherence, grammar, and overall quality, suggesting improvements if necessary.
* **Compile Newsletter Task:** The `Content Writer Agent` compiles all the approved news stories into a final, formatted newsletter.

### Tools

The project utilizes a custom tool to enhance the agents' capabilities:

* **Search the internet** (`SearchTool`): This tool is specifically designed to search the internet for news articles. It fetches and returns relevant results, including titles, URLs, and snippets. This tool requires a `SERPER_API_KEY`.

## Project Structure

* `agents.py`: Defines the AI agents, their roles, goals, backstories, and the tools they can use.
* `tasks.py`: Defines the tasks that the agents will perform, including their descriptions and expected outputs.
* `tools/search_tools.py`: Contains the implementation of the custom `SearchTool` used for internet searches.
* `file_io.py`: Provides utility functions for saving the generated markdown content to a file.
* `main.py`: The main script that orchestrates the CrewAI process, initializes agents and tasks, and runs the crew.
* `pyproject.toml`: Poetry project configuration and dependencies.
* `poetry.lock`: Poetry lock file, ensuring reproducible environments.
* `.gitignore`: Specifies files and directories to be ignored by Git.
* `README.md`: This README file.

## Technologies Used

* Python 3.10+
* [CrewAI](https://docs.crewai.com/)
* [CrewAI-Tools](https://github.com/joaomdmoura/crewai-tools)
* `python-dotenv`
* `requests`
* `beautifulsoup4`
* `duckduckgo-search`
* `litellm`
* `os` (for environment variables and file operations)

## Setup

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/ramanuja-5194/crewai_ai_news_letter.git](https://github.com/ramanuja-5194/crewai_ai_news_letter.git)
    cd crewai_ai_news_letter
    ```

2.  **Install dependencies using Poetry:**

    If you don't have Poetry installed, follow the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

    ```bash
    poetry install
    ```

3.  **Set up environment variables:**

    Create a `.env` file in the root directory of the project. This project uses `gemini/gemini-1.5-flash` model and `Serper API` for internet searches. You will need to add your API keys to this file:

    ```
    SERPER_API_KEY="your_serper_api_key_here"
    GEMINI_API_KEY="your_gemini_api_key_here"
    ```

    * You can get your Serper API Key from [Serper.dev](https://serper.dev/).
    * You can get your Google Gemini API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## How to Run

1.  **Activate the Poetry shell:**

    ```bash
    poetry shell
    ```

2.  **Run the main script:**

    ```bash
    python main.py
    ```

    The script will execute the AI agents to fetch, analyze, and compile the AI news letter. The final newsletter content will be saved as a Markdown file with a timestamp in the `output` folder.

## Example Output

The output will be a Markdown file (e.g., `ai_newsletter_YYYY-MM-DD.md`) in the `output` directory containing the compiled news stories, structured as a newsletter.
