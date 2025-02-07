from datetime import datetime
from pathlib import Path
from textwrap import dedent

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.python import PythonTools

agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key="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"),
    tools=[PythonTools()],show_tool_calls=True,
    description=dedent("""\
        You are an AI agent designed to analyze business metrics and identify relationships between them. 
        You will work with structured data across multiple domains, including sales, products, accounts, and campaigns. 
        Additionally, you will optimize graph queries and traverse paths to uncover hidden relationships and patterns 
        that can drive business decisions and marketing strategies. 
        Your objective is to provide a network-based understanding of the relationships between business 
        metrics and suggest areas for optimization or focus based on the results.\
    """),
    instructions=dedent("""\
        Your task is to analyze and identify relationships between various business metrics based on structured data from sales, 
        products, accounts, and campaigns. You will need to provide insights into how these metrics interact with each other.
                        
    1. **Analyze the provided data**: You will have access to datasets including sales, products, accounts, and campaigns. 
    Analyze these datasets to understand key metrics and their attributes.
   
    2. **Identify relationships**: Your primary goal is to identify how these metrics relate to each other. This includes:
        - Which metrics are influenced by others
        - How changes in one metric affect others wether positively or negatively.

    3. **Construct a Network**: Use NetworkX to create a relationship graph between the metrics. Each metric will be represented as a node, 
        and the edges will represent the relationships or influence between them. 
    - For example: "Customer Lifetime Value" might be influenced by "Repeat Purchase Rate" and "Average Order Value," 
    while "Campaign Conversion Rate" might be linked to "Customer Engagement Score" and "Campaign Channel Effectiveness."

    4. **Generate NetworkX Code**: Based on the identified relationships, provide Python code to generate a network graph using the NetworkX library.
    - Use nodes for each metric.
    - Define edges to represent correlations or influences.
    - Use visualizations using matplotlib where appropriate to showcase how these metrics are interrelated.\

    """),

    expected_output=dedent("""\
        Your analysis should include:
        - A detailed graph representation of the relationships between the metrics using NetworkX.
        - The graph visualization should be big with well spaced entities and edges.
    """)
)
if __name__ == "__main__":
    agent.print_response("Reltaionship between these metrics is metric_engagement_score, metric_clv, metric_product_affinity, metric_recent_purchase_recency, metric_aov, repeat_purchase_rate,metric_campaign_conversion, metric_customer_retention_rate,metric_engagement_channel_effectiveness, metric_churn_rate, metric_arpu", stream=True)