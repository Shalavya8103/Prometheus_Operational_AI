from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from textwrap import dedent
from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.python import PythonTools

# Define the agent that will create the metric tree using anytree
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile", api_key="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"),
    tools=[PythonTools()],
    description=dedent("""\
        You are an AI agent designed to analyze business metrics and organize them into a hierarchical tree structure.
        Your task is to create a metric tree structure from a mix of metrics that shows how some business metrics build upto some business goal (called north star metric).
        Metric trees introduce business semantics and enable data-driven decision-making by providing a clear view of how different metrics are related.
        These metrics will be arranged in a tree where each branch leads to more specific performance metrics.
        """),
    instructions=dedent("""\
        Your task is to 
        1 **Analyze the Provided Metrics**: You have a set of business metrics, such as Customer Engagement Score, CLV, Average Order Value, 
            Repeat Purchase Rate, etc.
            - Analyze these metrics to understand their use and importance in the business context.
                        
        2. **Analyze the Provided Domain**: Understand the domain and metrics to identify business objective of the domain. 
            Invent some north star metric that represents the primary business goal.
            For example, if the domain is sales and few relevent metrics from the pool are metrics like 'Customer Lifetime Value', 'Engagement Score', etc
            the root could be something like 'Adoption Rate'.
            Analyze the north star metric and identify the metrics that are important to track and analyze in order to achieve the business goal.
            - Identify which metrics are key for determining the north star metric and which are supporting metrics.
            - Analyze and invent any other metrics that are necessary to achieve the business goal.

        2. **Organize the Metrics into a Tree**: 
            - Identify how these metrics are related and arrange them in a tree structure where the metrics which can be derived from another metric are added lower 
            in the tree untill we reach the lowest level of data collection.

        3. **Generate Python Code**: Based on the relationships you identify, generate Python code that represents the tree structure.
            - Use the `anytree` library to create and visualize this structure.
            - The tree should be well-structured, and each node should be properly labeled with the corresponding metric name.

        4. **Output the Metric Tree**: Your output should include:
            - A Python code snippet that constructs the metric tree using `anytree`.
            - A visualization of the tree structure that shows how the metrics are interconnected.
    """),
    expected_output=dedent("""\
        Your analysis should include:
        - A detailed hierarchical tree of metrics.
        - The tree should show relationships and dependencies between metrics in a business context.
        - The generated Python code should build this tree and visualize it, using `anytree` for the visualization.
    """)
)

if __name__ == "__main__":
    agent.print_response("The domain is Marekting and the metrics are- metric_engagement_score, metric_clv, metric_product_affinity, metric_recent_purchase_recency, metric_aov, repeat_purchase_rate, metric_campaign_conversion, metric_customer_retention_rate, metric_engagement_channel_effectiveness, metric_churn_rate, metric_arpu", stream=True)