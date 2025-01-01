#!/usr/bin/env python
import sys
from crew import Day07Crew
from datetime import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'meta ai',
    }
    Day07Crew().crew().kickoff(inputs=inputs)

run()
