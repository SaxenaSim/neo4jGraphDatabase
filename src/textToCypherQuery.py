from crewai import Crew
from dotenv import load_dotenv
import os 
from driver import Driver
from log import Logger
from crewInstance import CrewInstance


load_dotenv()
open_api_key= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
    
# Main class to handle text to Cypher query conversion and execution
class TextToCypher:
    # crew_instance = None

    def __init__(self,text_input):
        #Define the schema for the Neo4j database
        self.input=text_input
        # Initialize logger
        self.logger = Logger.getlogger()
        self.logger.info("textToCypher initialized")
        #self.obj_qe = qe()
        #self.obj_qg = qg()
        
    def get_schema(self):
        schema = None
        try:
            self.logger.info("::Entering into get schema try::")
            schema =  """
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
            """
        except IOError as ioe:
            self.logger.error(f"Failed to get schema {ioe}")
            self.logger.info(schema)
            raise
        except Exception as ex:
            self.logger.error(ex)
            self.logger.info(schema)
        return schema
   
    # Method to run the tasks using agents and tools   
    def run(self):
        try:
            self.logger.info("Starting run method to get cypher query")
            # creation_agent = self.obj_qg.queryAgent()
            # creation_task = self.obj_qg.queryTask(creation_agent)
            # execution_agent = self.obj_qe.executionAgent()
            # execution_task = self.obj_qe.executionTask(execution_agent)

            self.logger.info("::: Creating Crew Object :::")
            # if TextToCypher.crew_instance is None:
            #     self.logger.info("Initializing Crew instance")
            #     TextToCypher.crew_instance = Crew(
            #         agents=[creation_agent, execution_agent],
            #         tasks=[creation_task, execution_task],
            #         memory=True
            #     )
            # else:
            #     self.logger.info("Using existing Crew instance")
    
            crew_obj = CrewInstance.get_crewInstance()
            # Create crew object with agents and tasks
            # crew = Crew(
            #     agents=[creation_agent, execution_agent],
            #     tasks=[creation_task, execution_task],
            #     memory=True
            #)
            self.logger.info("Kicking off the crew tasks")
            print("::: Crew tasks starting:::")
            print(crew_obj.id)
            schema = self.get_schema()
            # print(TextToCypher.crew_instance.id)
            # Execute the tasks and get results
            result = crew_obj.kickoff(inputs={"text_input":self.input,"schema":schema})
            self.logger.info("Crew tasks completed")
            print(" :: Metrics ::::",crew_obj.usage_metrics)
            self.logger.info(f"result:{result}")
            
        except IOError as ioe:
            self.logger.error(ioe)
            raise
        except Exception as ex:
            self.logger.error(ex)
            raise
        return result
        
if __name__ == "__main__":
    
    logger = Logger.getlogger()
    try:
                
        textInput = "Give me the list of consumers whose business name is Arlin Toomey"
        
        text_to_cypher = TextToCypher(textInput)
        text_to_cypher.run()

        # Close Neo4j connection
        Driver.close()  
    except IOError as e:
        logger.error(e)
        
    except Exception as e:
        logger.error(e)