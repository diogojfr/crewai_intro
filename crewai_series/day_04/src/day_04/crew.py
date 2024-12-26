from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from tools.custom_tool import CustomSerperDevTool

@CrewBase
class Day04Crew:
	"""Day04 crew"""

	# ollama_1b = LLM(model="ollama/llama3.2:1b", base_url="http://localhost:11434")
	mistral = LLM(model="ollama/mistral:latest", base_url="http://localhost:11434")
	

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[CustomSerperDevTool(), ScrapeWebsiteTool()], 
			verbose=True,
			llm=self.mistral
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True,
			llm=self.mistral
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Day04 crew"""
		return Crew(
			agents=self.agents, 
			tasks=self.tasks, 
			process=Process.sequential,
			verbose=True,
		)