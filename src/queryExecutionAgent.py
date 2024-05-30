from crewai import Agent ,Task
from tool import Neo4jQueryTool
from log import Logger

class queryExecutionAgent:
    def __init__(self):
        self.logger = Logger.getlogger()
        self.logger.info("queryExecution agent initialized")
        
    def executionSetup(self):
        # Create agent for executing the Cypher query       
        execution_agent = Agent(
            role="Execution of Cypher query",
            goal="""
                    Execute the cypher query generated from the input text in neo4j
                    database and get the output.
                 """,
            backstory=("""
                        You have the access to the neo4j database 
                        and can execute queries to retrieve data.
                       """),
        )
        self.logger.info("execution agent created successfully")
        
        # Create tool object for query execution
        tool_obj=Neo4jQueryTool()
        
        # Task for executing the Cypher query and retrieving results
        execution_task = Task(
            description=("""Execute the cypher query generated in the Neo4j database and 
                         return the output of that query in the console in json format having 
                         all the properties of consumer nodes
                         """),
            expected_output="The results of the executed cypher query.",
            tools=[tool_obj],
            agent=execution_agent
        )
        self.logger.info("execution task created successfully")
        
        return execution_agent , execution_task