from driver import Driver
from dotenv import load_dotenv
import os , yaml
import logging, logging.config
from log import Logger

load_dotenv()

class CSVLoader:

    @staticmethod
    def load_csv_data(tx) -> None:
        logger = Logger.getlogger()
        logger.debug("entering into loader method")
        # Loading consumers data
        query = """
        LOAD CSV WITH HEADERS FROM 'file:///home/user1/Desktop/neo4jGraphDatabase/data/consumers.csv' AS row
        MERGE (c:Consumers {consumer_id: toInteger(row.consumer_id)})
        ON CREATE SET c.name = row.name, c.age = toInteger(row.age), c.email = row.email, c.gender = row.gender , c.business_id = toInteger(row.business_id);
        """
        logger.debug("query")
        results = tx.run(query)
        logger.info(f"Executed Consumer query {results}")
        # Loading business data
        query = """
        LOAD CSV WITH HEADERS FROM 'file:///home/user1/Desktop/neo4jGraphDatabase/data/businesses.csv' AS row
        MERGE (b:Businesses {business_id: toInteger(row.business_id)})
        ON CREATE SET b.name = row.name, b.domain_purchased = row.domain_purchased;
        """
        tx.run(query)
        logger.info("Executed Business query")
        # Creating relationships between consumers and businesses
        query = """
        MATCH (c:Consumers), (b:Businesses)
        WHERE c.business_id = toInteger(b.business_id)
        MERGE (c)-[:HAS_BUSINESS_OF]->(b);
        """
        tx.run(query)
        logger.info("Executed relationship between query")
        
if __name__ == "__main__":
    try:
        print("entering into try method")
        # Initialize the Neo4j driver
        if not Driver.get_driver():
            Driver.initialize()
        
        # Get the Neo4j driver instance
        driver = Driver.get_driver()
        
        # Open a session and execute the CSV loading queries within a transaction
        with driver.session() as session:
            print("session opened")
            session.execute_write(CSVLoader.load_csv_data)
            print("method called")
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the driver is closed
        Driver.close()
