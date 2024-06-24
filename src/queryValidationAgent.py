from log import Logger
from crewai import Task , Agent

class queryValidationAgent:
    def __init__(self):

        self.logger = Logger.getlogger()
        self.logger.info("query validation agent initialized")
        
    def ValidateAgent(self):
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
                    
                """,
            )
        except Exception as e:
            self.logger.error(f"Failed to create agent {e}")
            raise
        return validation_agent

 
    def ValidateTask(self, validation_agent):
        self.logger.info("Creating tasks for agents")
        try:
            # Task for generating Cypher query from natural language text
            validation_task = Task(
                description="""
                    Your task is to validate the Cypher query generated based on the user's input 
                    and the context of previous interactions. If the query is incorrect, call the
                    previous agent again to ensure it accurately reflects the user's request.
                """,
                expected_output="A correct and context-aware Cypher query",
                agent=validation_agent,
                #human_input=True
            )
        except Exception as e:
            self.logger.error(f"Failed to create task {e}")
            raise
        return validation_task


        
if __name__ =="__main__":
    obj = queryValidationAgent()
    result = obj.queryValidateAgent()
    #print(result)