#!/usr/bin/env python
import sys
from crew import Day06Crew
from datetime import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'meta ai',
    }
    Day06Crew().crew().kickoff(inputs=inputs)

run()
