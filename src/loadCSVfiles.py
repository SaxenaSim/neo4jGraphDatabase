from driver import Driver
from dotenv import load_dotenv
import os , yaml
import logging, logging.config

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

class CSVLoader:

    @staticmethod
    def load_csv_data(tx) -> None:
        # Loading consumers data
        query = """
        LOAD CSV WITH HEADERS FROM 'file:///home/user1/Desktop/neo4jGraphDatabase/data/consumers.csv' AS row
        MERGE (c:Consumer {consumer_id: toInteger(row.consumer_id)})
        ON CREATE SET c.name = row.name, c.age = toInteger(row.age);
        """
        tx.run(query)
        logger.info("Executed Consumer query")
        # Loading business data
        query = """
        LOAD CSV WITH HEADERS FROM 'file:///home/user1/Desktop/neo4jGraphDatabase/data/business.csv' AS row
        MERGE (b:Business {business_id: toInteger(row.business_id)})
        ON CREATE SET b.name = row.name, b.industry = row.industry;
        """
        tx.run(query)
        logger.info("Executed Business query")
        # Creating relationships between consumers and businesses
        query = """
        MATCH (c:Consumer), (b:Business)
        WHERE c.consumer_id = toInteger(b.business_id)
        MERGE (c)-[:HAS_BUSINESS_OF]->(b);
        """
        tx.run(query)
        logger.info("Executed relationship between query")
        
if __name__ == "__main__":
    try:
        # Initialize the Neo4j driver
        if not Driver.get_driver():
            Driver.initialize()
        
        # Get the Neo4j driver instance
        driver = Driver.get_driver()
        
        # Open a session and execute the CSV loading queries within a transaction
        with driver.session() as session:
            logger.info("Before loading files")
            session.execute_write(CSVLoader.load_csv_data)
            
    except Exception as e:
        logger.debug(f"An error occurred: {e}")
    finally:
        # Ensure the driver is closed
        Driver.close()
