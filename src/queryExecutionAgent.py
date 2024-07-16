from crewai import Agent ,Task
from tool import Neo4jQueryTool
from log import Logger

class QueryExecutionAgent:
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
                backstory="You have access to a Neo4j database with the following schema: {schema}",
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
                description="Execute the generated Cypher query in the Neo4j database, fetch the output,if there is no output then return empty list and print it to the console.",
                expected_output="""The result of the Cypher query should be returned in the json format with the specified keys
                For example - 
                (
                    'results': [
                                    (
                                        "consumer_id": <integer>,
                                        "name": <string>,
                                        "age": <integer>,
                                        "gender": <string>,
                                        "email": <string>,
                                        "business_name": <string>
                                    ),
                                ]
                )
                """,
                # expected_output="""The result of the Cypher query should be printed in the following format which is the list of json objects - 
                # [
                #     {
                #     "consumer_id": <integer>,
                #     "name": <string>,
                #     "age": <integer>,
                #     "gender": <string>,
                #     "email": <string>,
                #     "business_id": <integer>,
                #     "business_name": <string>
                #     },
                #     ...
                # ]
                # """,
                tools=[tool_obj],
                agent=execution_agent
)
            self.logger.info("execution task created successfully")
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        
        return execution_task
    
    
if __name__=="__main__":
    obj = QueryExecutionAgent()
    agent = obj.executionAgent()
    print(agent)
    print(agent.role , agent.goal , agent.backstory , agent.llm.temperature)
    #print(type(obj.executionTask(agent)))