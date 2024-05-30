from crewai import Task , Agent , Crew
from dotenv import load_dotenv
import os 
from crewai_tools import BaseTool
from driver import Driver
from log import Logger
from tool import Neo4jQueryTool
from queryExecutionAgent import queryExecutionAgent as qe
from queryGenerationAgent import queryGenerationAgent as qg


load_dotenv()
open_api_key= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'

# Tool class to execute Cypher queries on the Neo4j database
# class Neo4jQueryTool(BaseTool):
#     name:str="Neo4j Quering Tool"
#     description:str="The input to this tool is a cypher query string to execute on neo4j database. This tool executes the query and returns the result."
#     # Get the Neo4j driver and execute the query   
#     def _run(self,query):
#         driver = Driver.get_driver()
#         with driver.session() as session:
#             result = session.run(query)
#             records = list(result)  
#         return records
    
# Main class to handle text to Cypher query conversion and execution
class textToCypher:
    def __init__(self,text_input):
        #Define the schema for the Neo4j database
        self.schema = """
        {
            "nodes": {
                "Consumers": {
                    "properties": ["consumer_id", "name", "email", "age", "gender", "business_id"]
                },
                "Businesses": {
                    "properties": ["business_id", "name", "domain_purchased"]
                }
            },
            "relationships": {
                "HAS_BUSINESS_OF": {
                    "description": "Connects consumers to businesses where business_id matches",
                    "from": "Consumers",
                    "to": "Businesses"
                }
            }
        }
        """,
        self.input=text_input
        # Initialize logger
        self.logger = Logger.getlogger()
        self.logger.info("textToCypher initialized")
        self.obj_qe = qe()
        self.obj_qg = qg()
        
    # Method to create agents for task execution
    # def createAgents(self):
        
    #     self.logger.info("Creating agents with schema")
        
    #     # Create agent for converting text to Cypher query
    #     creation_agent = Agent(
    #         role="Conversion of Text to Cypher",
    #         goal="""
    #                 Convert the given text input into a cypher query of Neo4j 
    #                 that exactly matches with the names and spelling of the nodes and 
    #                 relationships of the schema
    #              """,
    #         backstory="You are working on a Neo4j database with the following schema:{schema}",
    #         allow_delegation=True
            
    #     )
    #     # Create agent for executing the Cypher query       
    #     execution_agent = Agent(
    #         role="Execution of Cypher query",
    #         goal="""
    #                 Execute the cypher query generated from the input text in neo4j
    #                 database and get the output.
    #              """,
    #         backstory=("""
    #                     You have the access to the neo4j database 
    #                     and can execute queries to retrieve data.
    #                    """),
    #     )
    #     self.logger.info("Agents created successfully")
    #     return creation_agent , execution_agent
    
    # # Method to create tasks for agents
    # def createTasks(self,creation_agent,execution_agent):
    #     self.logger.info("Creating tasks for agents")
    #     # Create tool object for query execution
    #     tool_obj=Neo4jQueryTool()
    #     # Task for generating Cypher query from natural language text
    #     creation_task = Task(
    #         description =("""
    #             You are an expert in Cypher query language. Please translate the following
    #             natural language request into a Cypher query for a Neo4j database, considering 
    #             the provided schema:{text_input}.Ensure all node and relationship names match 
    #             the provided schema exactly.
    #             """),
    #         expected_output="""
    #         A Cypher query generated in context to the given text input with 
    #         exact node and relationship names from the schema
    #         """,
    #         agent=creation_agent,
    #     )
        
    #     # Task for executing the Cypher query and retrieving results
    #     execution_task = Task(
    #         description=("""Execute the cypher query generated in the Neo4j database and 
    #                      return the output of that query in the console in json format having 
    #                      all the properties of consumer nodes
    #                      """),
    #         expected_output="The results of the executed cypher query.",
    #         tools=[tool_obj],
    #         agent=execution_agent
    #     )
    #     self.logger.info("Tasks created successfully")
    #     return creation_task , execution_task
     
    # Method to run the tasks using agents and tools   
    def run(self):
        self.logger.info("Starting run method to get cypher query")
        execution_agent, execution_task = self.obj_qe.executionSetup()
        creation_agent, creation_task = self.obj_qg.queryAgent()
        self.logger.info("::: Creating Crew Object :::")        
        
        # Create crew object with agents and tasks
        crew = Crew(
            agents=[creation_agent, execution_agent],
            tasks=[creation_task, execution_task],
        )
        self.logger.info("Kicking off the crew tasks")
        print("::: Crew tasks starting:::")
        
        # Execute the tasks and get results
        result = crew.kickoff(inputs={"text_input":self.input,"schema":self.schema})
        self.logger.info("Crew tasks completed")
        print(" :: Metrics ::::",crew.usage_metrics)
        self.logger.info(f"result:{result}")
        
if __name__ == "__main__":
            
    textInput = "Give me the list of consumers whose business is Arlin Toomey"
    
    text_to_cypher = textToCypher(textInput)
    text_to_cypher.run()

    # Close Neo4j connection
    Driver.close()
    
 