from neo4j import GraphDatabase , BoltDriver as bd
import os , yaml
from dotenv import load_dotenv
import logging , logging.config
from log import Logger

load_dotenv()

class Driver:
    driver = None
    logger = Logger.getlogger()

    @classmethod
    def initialize(cls):
        # Get Neo4j connection details from environment variables
        uri = os.getenv("NEO4J_URI")
        user = os.getenv("NEO4J_USER")
        password = os.getenv("NEO4J_PASSWORD")
        
        # Establish connection to Neo4j database
        cls.driver = GraphDatabase.driver(uri, auth=(user, password))
        cls.logger.info("Connecting to Neo4j...")

    @classmethod
    def close(cls):
        # Close the Neo4j driver connection
        if cls.driver:
            cls.driver.close()
            cls.driver = None
            cls.logger.info("Closing Neo4j connection.")
    
    @classmethod
    def get_driver(cls):
        # Return the Neo4j driver
        if cls.driver is None:
            cls.initialize()
        return cls.driver

if __name__ == "__main__":
    Driver.initialize()
    neo4j_driver = Driver.get_driver()


