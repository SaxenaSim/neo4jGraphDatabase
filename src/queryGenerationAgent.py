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

                    Use the context of previous queries to ensure continuity and relevance.Recognize refrences to previous outputs, such as 'from the above output','from same business', and similar phrases.Extract the relevant details from the previous queries to construct accurate and context-aware Cypher queries. Consider the schema and relationships while constructing the Cypher queries.
                    
                    Examples of how to handle references to previous outputs:
                    1. Previous query: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="XYZ" RETURN c"
                    Follow-up query: "From the above output, I only want the consumer IDs and names."
                    Output: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="XYZ" RETURN c.consumer_id, c.name"
                
                    2. Previous query: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name = "ABC" RETURN c"
                    Follow-up query: "List the email addresses of consumers from the same business."
                    Output: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="ABC" RETURN c.email"
                    
                """,
            )
        except Exception as e:
            self.logger.error(f"Failed to create agent {e}")
            raise
        return creation_agent

 
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
                    
                    Recognize and handle references to previous outputs. For example:
                    - "From the above output": Use the results of the previous query.
                    - "From the same business": Extract the relevant business information from previous context.
                
                    Examples of how to handle references to previous outputs:
                    1. Previous query: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="XYZ" RETURN c"
                    Follow-up query: "From the above output, I only want the consumer IDs and names."
                    Output: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="XYZ" RETURN c.consumer_id, c.name"
                
                    2. Previous query: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name = "ABC" RETURN c"
                    Follow-up query: "List the email addresses of consumers from the same business."
                    Output: "MATCH (c:Consumers)-[:HAS_BUSINESS_OF]->(b:Businesses) WHERE b.name="ABC" RETURN c.email"
                    
                """,
                expected_output="A correct and context-aware Cypher query",
                agent=creation_agent,
                #human_input=True
            )
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        return creation_task


        
if __name__ =="__main__":
    obj = queryGenerationAgent()
    result = obj.queryAgent()
    #print(result)