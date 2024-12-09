from langchain_openai import ChatOpenAI
from src.queryGenerationAgent import QueryGenerationAgent
from crewai import Agent
from src.queryExecutionAgent import QueryExecutionAgent
from src.queryValidationAgent import QueryValidationAgent

def test_agent_default_values():
    agent = Agent(role="test_role",goal="test_goal",backstory="test_backstory")
    assert isinstance(agent.llm, ChatOpenAI)
    assert agent.llm.model_name == "gpt-4"
    assert agent.llm.temperature == 0.7
    assert agent.llm.verbose is False
    assert agent.allow_delegation is True


def test_queryGenerationAgent():
    obj = QueryGenerationAgent()
    agent = obj.queryAgent()
    assert agent.role == "Expert in Cypher Query Conversion"
    assert agent.goal == """
                    You are an expert in Cypher query language. 
                    Your goal is to convert the given text in the task to a correct and efficient Cypher query for a Neo4j database.
                    Ensure the query adheres to the schema and relationships provided.
                    Text : {input_text}
                """
    assert agent.backstory == """
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
                    
                """
                
def test_queryExecutionAgent():
    obj = QueryExecutionAgent()
    agent = obj.executionAgent()
    
    assert agent.role == "Database Query Executor"
    assert agent.goal == "Fetch the output of the Cypher query from the Neo4j database"
    assert agent.backstory == "You have access to a Neo4j database with the following schema: {schema}"


def test_queryValidationAgent():
    obj = QueryValidationAgent()
    agent = obj.validateAgent()
    
    assert agent.role == "Expert in Cypher Query Language Validation"
    assert agent.goal == """
                    You are an expert in Cypher query language. 
                    Your goal is to validate Cypher queries based on user inputs , 
                    taking into account the context of previous queries. If the initial query is incorrect, 
                    call the previous agent again to regenerate the correct query this time according to the 
                    user input considering the context.
                    Previous conversation with the user:
                    {context}
                """
    assert agent.backstory == """
                    You are responsible for ensuring the correctness of Cypher queries generated from user inputs. 
                    You consider the context of previous interactions to maintain continuity and accuracy.
                    
                """