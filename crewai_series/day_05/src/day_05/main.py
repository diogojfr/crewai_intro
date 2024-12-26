#!/usr/bin/env python
import sys
from crew import Day05Crew
from datetime import datetime

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'meta ai',
    }
    Day05Crew().crew().kickoff(inputs=inputs)

run()
