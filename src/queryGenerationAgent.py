from log import Logger
from crewai import Task , Agent

class queryGenerationAgent:
    def __init__(self):
        #Define the schema for the Neo4j database
        # self.schema = """
        # {
        #     "nodes": {
        #         "Consumers": {
        #             "properties": ["consumer_id", "name", "email", "age", "gender", "business_id"]
        #         },
        #         "Businesses": {
        #             "properties": ["business_id", "name", "domain_purchased"]
        #         }
        #     },
        #     "relationships": {
        #         "HAS_BUSINESS_OF": {
        #             "description": "Connects consumers to businesses where business_id matches",
        #             "from": "Consumers",
        #             "to": "Businesses"
        #         }
        #     }
        # }
        # """,
        #self.input=text_input
        # Initialize logger
        self.logger = Logger.getlogger()
        self.logger.info("query generation agent initialized")
        
    # Method to create agents for task execution
    def queryAgent(self):
        
        self.logger.info("Creating agents with schema")
        
        # Create agent for converting text to Cypher query
        creation_agent = Agent(
            role="Conversion of Text to Cypher",
            goal="""
                    Convert the given text input into a cypher query of Neo4j 
                    that exactly matches with the names and spelling of the nodes and 
                    relationships of the schema
                 """,
            backstory="You are working on a Neo4j database with the following schema:{schema}",
            allow_delegation=True
            
        )
        
        self.logger.info("Creating tasks for agents")

        # Task for generating Cypher query from natural language text
        creation_task = Task(
            description =("""
                You are an expert in Cypher query language. Please translate the following
                natural language request into a Cypher query for a Neo4j database, considering 
                the provided schema:{text_input}.Ensure all node and relationship names match 
                the provided schema exactly.
                """),
            expected_output="""
            A Cypher query generated in context to the given text input with 
            exact node and relationship names from the schema
            """,
            agent=creation_agent,
        )
        
        return creation_agent , creation_task