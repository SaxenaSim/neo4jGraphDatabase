from crewai import Crew
from dotenv import load_dotenv
import os 
from driver import Driver
from log import Logger
from crewInstance import CrewInstance
import agentops


#api_key=os.environ["AGENTOPS_API_KEY"]
load_dotenv()
#agentops.init(api_key)
open_api_key= os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = 'gpt-3.5-turbo'
context=[]
    
# Main class to handle text to Cypher query conversion and execution
class TextToCypher:

    def __init__(self):
        self.crew_obj = CrewInstance.get_crewInstance()
        
        # Initialize logger
        self.logger = Logger.getlogger()
        self.logger.info("textToCypher initialized")
        
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
        print("::::::::::type of schema:::::::::",type(schema))
        return schema
        
    # Method to run the tasks using agents and tools   
    def run(self,text_input):
        #agentops.init(api_key="93ea5098-c6d6-490e-85a9-875581b2b790")
        
        if not text_input:
            raise ValueError("Input text should not be empty")
        try:
            global context
            self.input = text_input
            self.logger.info("Starting run method to get cypher query")    
            self.logger.info(f"crew instnace id created is {self.crew_obj.id}")
            self.logger.info("Kicking off the crew tasks")
            print("::: Crew tasks starting:::")
            print(self.crew_obj.id)
            
            schema = self.get_schema()
            
            self.logger.info(f"::context::{context}")
            
            # Execute the tasks and get results
            result = self.crew_obj.kickoff(inputs={"input_text":self.input,"schema":schema,"context":context})
            context.append(text_input)
            print("::::::::type of result:::::::::::",type(result))
            
            self.logger.info(f"::context::{context}")
            self.logger.info("Crew tasks completed")
            print(" :: Metrics ::::",self.crew_obj.usage_metrics)
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
                
        #textInput = "Give me the list of consumers whose business name is Arlin Toomey"
        
        text_to_cypher = TextToCypher()
        #text_to_cypher.run()

        # Close Neo4j connection
        Driver.close()
        
    except IOError as e:
        logger.error(e)
        
    except Exception as e:
        logger.error(e)