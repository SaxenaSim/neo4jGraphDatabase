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
                role="Database Query Executor",
                goal="Fetch the output of the Cypher query from the Neo4j database",
                memory=True,
                backstory="You have access to a Neo4j database with the following schema: {schema}"
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
                description="Execute the generated Cypher query in the Neo4j database, fetch the output, and print it to the console.",
                expected_output="The result of the Cypher query should be printed in the console.",
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