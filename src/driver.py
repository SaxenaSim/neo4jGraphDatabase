from neo4j import GraphDatabase , BoltDriver as bd
import os , yaml
from dotenv import load_dotenv
import logging , logging.config

load_dotenv()

# Determine current and project root directories
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root_dir = os.path.dirname(current_dir)

# Path to the logging configuration file
config_logging_path = os.path.join(project_root_dir, "logging_config.yaml")
print(config_logging_path)

# Load logging configuration from the YAML file
with open(config_logging_path, 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

# Create the logger
logger = logging.getLogger(__name__)

class Driver:
    _driver = None

    @classmethod
    def initialize(cls):
        # Get Neo4j connection details from environment variables
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        
        # Establish connection to Neo4j database
        cls._driver = GraphDatabase.driver(uri, auth=(user, password))
        logger.info("Connecting to Neo4j...")

    @classmethod
    def close(cls):
        # Close the Neo4j driver connection
        if cls._driver:
            cls._driver.close()
            cls._driver = None
            logger.info("Closing Neo4j connection.")
    
    @classmethod
    def get_driver(cls) -> bd:
        # Return the Neo4j driver
        if cls._driver is None:
            cls.initialize()
        return cls._driver

if __name__ == "__main__":
    Driver.initialize()
    neo4j_driver = Driver.get_driver()

# class Driver:
#     def __init__(self) -> None:
        
#         # Get Neo4j connection details from environment variables
#         uri = os.getenv("NEO4J_URI")
#         user = os.getenv("NEO4J_USER")
#         password = os.getenv("NEO4J_PASSWORD")
        
#         # Establish connection to Neo4j database
#         self.driver = GraphDatabase.driver(uri,auth=(user,password))
#         logger.info("Connecting to Neo4j...")
        
#     def close(self) -> None:
        
#         # Close the Neo4j driver connection
#         if self.driver:
#             self.driver.close()
#             logger.info("Closing Neo4j connection.")
            
#     def get_driver(self) ->bd:
        
#         # Return the Neo4j driver
#         return self.driver
    
# if __name__ == "__main__":
    
#     obj = Driver()
#     neo4j_driver = obj.get_driver()


