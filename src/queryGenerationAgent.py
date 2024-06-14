from log import Logger
from crewai import Task , Agent

class queryGenerationAgent:
    def __init__(self):

        self.logger = Logger.getlogger()
        self.logger.info("query generation agent initialized")
        
    def queryAgent(self):
        self.logger.info("Creating agents with schema")
        try:
            # Create agent for converting text to Cypher query
            creation_agent = Agent(
                role="Expert in Cypher Query Conversion",
                goal="""
                    You are an expert in Cypher query language. 
                    Your goal is to convert the given text in the task to a correct and efficient Cypher query for a Neo4j database.
                    Ensure the query adheres to the schema and relationships provided.
                    Text : {input_text}
                """,
                memory=True,
                backstory="""
                    You create queries for input text provided by the user and also update queries based on changes asked by the user.
                    The Neo4j database schema you are working with is as follows:
                    - Consumers: (consumer_id, name, gender, email, age, business_id)
                    - Businesses: (business_id, name, domain_purchased)
                    - Relationship: Consumers are related to Businesses with a relationship HAS_BUSINESS_OF (consumer_id -> business_id).
                    Previous conversation with the user:
                    {context}

                    Use the context of previous queries to ensure continuity and relevance. Consider the schema and relationships while constructing the Cypher queries.
                """,
            )
        except Exception as e:
            self.logger.error(f"Failed to create agent {e}")
            raise
        return creation_agent

        
    # Method to create agents for task execution
#     def queryAgent(self):
        
#         self.logger.info("Creating agents with schema")
#         try:
#             # Create agent for converting text to Cypher query
#             creation_agent = Agent(
#                 role="Conversion of Text to Cypher.",
#                 goal="""
#                     You are an expert in Cypher query language. 
#                     Your goal is to convert the given text in the task to a Cypher query.
                    
#                     Text: {input_text}
#                 """,
#                 memory=True,
#                 backstory="""
#                     You create queries for input text provided by the user and also update queries based on changes asked by the user.
#                     The Neo4j database schema you are working with is as follows: {schema}.
#                     Previous conversation with the user is: 
#                     {context}
#                 """
# )

#         except Exception as e:
#             self.logger.error(f"Failed to create agent {e}")
#             raise
#         return creation_agent
    def queryTask(self, creation_agent):
        self.logger.info("Creating tasks for agents")
        try:
            # Task for generating Cypher query from natural language text
            creation_task = Task(
                description="""
                    Convert the following natural language input into a correct Cypher query for a Neo4j database.
                    Schema:
                    - Consumers: (consumer_id, name, gender, email, age, business_id)
                    - Businesses: (business_id, name, domain_purchased)
                    - Relationship: Consumers are related to Businesses with a relationship HAS_BUSINESS_OF (consumer_id -> business_id).

                    Ensure the query is accurate, follows the schema, and incorporates context from previous queries if provided.
                    Refer to the context of previous queries to maintain continuity.
                """,
                expected_output="A correct and context-aware Cypher query",
                agent=creation_agent,
            )
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        return creation_task

        
#     def queryTask(self,creation_agent):
        
#         self.logger.info("Creating tasks for agents")
#         try:
#             # Task for generating Cypher query from natural language text
#             creation_task =  Task(
#                 description="""
#                     Convert natural language into a Cypher query for a Neo4j database.
#                     Schema: Consumers (consumer_id, name, gender, email, age, business_id), Businesses (business_id, name, domain_purchased).
#                     Consumers are related to Businesses with a relationship HAS_BUSINESS_OF.
#                     Also, refer to the previous queries in context if needed.
#                 """,
#                 expected_output="A correct Cypher query",
#                 agent=creation_agent,
# )
            
#         except Exception as e:
#             self.logger.error(f"Failed to create task {e}")
#             raise
#         return creation_task
        
if __name__ =="__main__":
    obj = queryGenerationAgent()
    result = obj.queryAgent()
    #print(result)