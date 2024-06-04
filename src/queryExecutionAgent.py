from crewai import Agent ,Task
from tool import Neo4jQueryTool
from log import Logger

class queryExecutionAgent:
    def __init__(self):
        self.logger = Logger.getlogger()
        self.logger.info("queryExecution agent initialized")
        
    def executionAgent(self):
        try:
            # Create agent for executing the Cypher query       
            execution_agent = Agent(
                role="Execution of Cypher query",
                goal="""
                        Execute the cypher query generated from the input text in neo4j
                        database and get the output.
                    """,
                memory=True,
                backstory=("""
                            You have the access to the neo4j database 
                            and can execute queries to retrieve data.
                        """),
                allow_delegation=False
            )
            self.logger.info("execution agent created successfully")
        except Exception as e:
            self.logger.error(f"Failed to create agent {e}")
            raise
        return execution_agent
        
        
    def executionTask(self,execution_agent):
        try:
            # Create tool object for query execution
            tool_obj=Neo4jQueryTool()
            
            # Task for executing the Cypher query and retrieving results
            execution_task = Task(
                description=("""Execute the cypher query generated in the Neo4j database and 
                            return the output of that query in the console in json format having 
                            all the requested properties of consumer nodes
                            """),
                expected_output="The results of the executed cypher query.",
                tools=[tool_obj],
                agent=execution_agent
            )
            self.logger.info("execution task created successfully")
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        
        return execution_task
    
    
if __name__=="__main__":
    obj = queryExecutionAgent()
    agent = obj.executionAgent()
    print(type(obj.executionTask(agent)))