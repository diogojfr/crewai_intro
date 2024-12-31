from crewai_tools import BaseTool
import os 
from datetime import datetime
from dotenv import load_dotenv


class CustomFileWriterTool(BaseTool):
    name: str = "Custom File Writer Tool"
    description: str = "Write content to a file."

    def _run(self, content: str, filename: str) -> str:
        """
        Write content to a file.
        """
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{filename}_{timestamp}"

        if not filename.endswith(".md"):
            filename = f"{filename}.md"

        output_dir = "ainews"
        os.makedirs(output_dir, exist_ok=True)

        file_path = os.path.join(output_dir, filename)

        try:
            with open(file_path, "w") as file:
                file.write(content)

            return f"Content written to file: {file_path}"
        except Exception as e:
            return f"Error writing content to file: {str(e)}"


