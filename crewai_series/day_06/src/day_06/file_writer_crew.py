from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from tools.custom_file_writer_tool import CustomFileWriterTool

@CrewBase
class FileWriterCrew:
    """File Writer Crew"""

    agents_config = "config/filewriter/agents.yml"
    tasks_config = "config/filewriter/tasks.yml"

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'],
            tools=[CustomFileWriterTool()], 
            verbose=True,
        )

    @task
    def file_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_writer_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the File Writer Crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )