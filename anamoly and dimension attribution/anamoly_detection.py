import pandas as pd
import numpy as np
from scipy import stats
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.pandas import PandasTools
from datetime import datetime
import os

file_path = "monthly_data.csv"

if os.path.exists(file_path):   
    print(f"Reading data from '{file_path}'")
    monthly_data_df = pd.read_csv(file_path)

    agent = Agent(
        model=Groq(id="llama-3.3-70b-versatile", api_key="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"),
        tools=[PandasTools()],
        description="""\
            You are an AI agent responsible for detecting drastic changes in metrics on a monthly basis.
            Read the monthly_data in the dataframe(Month, metric, and metric_value, Z_score)
            You have to provide me with the metrics that have changes signifiancty\
            """,
        instructions="""\
            1. **Analyze monthly_data Dataframe**: It has Month, metric, and metric_value, Z_score.
            2. ** Analyse any drastic changes in any metric over the month based on its value the previous month*- Your task is to analyze these metrics over its value the previous month or 
            quarter, and report any metric which has significantly changed, which indicates an anomaly.\
            3. **Provide the name and details of the metrics that have shown drastic changes, and the percentage of increase or decrease.**\
            4. **Make a small summary of the changes that have occured**: For example-
             This month "Returns" decreased by 15 percent compared to last month. Thic could be attributed to changes in data quality
            """,
        expected_output= """\
            Provide the name and details of the metrics that have shown drastic changes and the percentage of increase or decrease.
            Summary\
            """
    )

    response = agent.print_response(""" 
                                    Analyze the dataframe to detect any significant changes in the monthly metrics.
                                    Show only those whi have significant changes
                                     """,
        stream=True,
        dataframes={"monthly_data": monthly_data_df}
    )

else:
    print(f"Error: File '{file_path}' not found.")

