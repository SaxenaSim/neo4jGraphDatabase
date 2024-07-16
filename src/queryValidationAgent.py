from log import Logger
from crewai import Task , Agent

class QueryValidationAgent:
    def __init__(self):

        self.logger = Logger.getlogger()
        self.logger.info("query validation agent initialized")
        
    def validateAgent(self):
        self.logger.info("Creating agents with schema")
        try:
            # Create agent for converting text to Cypher query
            validation_agent = Agent(
                role="Expert in Cypher Query Language Validation",
                goal="""
                    You are an expert in Cypher query language. 
                    Your goal is to validate Cypher queries based on user inputs , 
                    taking into account the context of previous queries. If the initial query is incorrect, 
                    call the previous agent again to regenerate the correct query this time according to the 
                    user input considering the context.
                    Previous conversation with the user:
                    {context}
                """,
                memory=True,
                backstory="""
                    You are responsible for ensuring the correctness of Cypher queries generated from user inputs. 
                    You consider the context of previous interactions to maintain continuity and accuracy.
                    Validate the query on the following parameters:
                    1. Query is syntactically correct.
                    2. The query is relevant to the input given, considering the context of previous queries.
                    3. If specific fields are mentioned in the input, ensure those fields are included in the query output.
                    4. For generic or simple requests like to list consumers, return the consumer IDs, names, ages, genders, emails, and business names.
                    If any of these parameters are not met, call the previous agent to regenerate the query.
                    
                """,
            )
        except Exception as e:
            self.logger.error(f"Failed to create agent {e}")
            raise
        return validation_agent

 
    def validateTask(self, validation_agent):
        self.logger.info("Creating tasks for agents")
        try:
            # Task for generating Cypher query from natural language text
            validation_task = Task(
                description="""
                    Your task is to validate the Cypher query generated based on the user's input 
                    and the context of previous interactions. Validate the query on the following parameters:
                    1. Query is syntactically correct.
                    2. The query is relevant to the input given, considering the context of previous queries.
                    3. If specific fields are mentioned in the input, ensure those fields are included in the query output.
                    4. For generic or simple requests to list consumers, always return the consumer IDs, names, ages, genders, emails, and business names.
                    If the query is incorrect on any of these parameters, call the previous agent again to regenerate the query, 
                    ensuring it accurately reflects the user's request and context.
                """,
                expected_output="A validated and correct Cypher query or a regenerated query if initial validation fails",
                agent=validation_agent,
                #human_input=True
            )
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        return validation_task


        
if __name__ =="__main__":
    obj = QueryValidationAgent()
    result = obj.validateAgent()
    #print(result)