from driver import Driver
from log import Logger

class DataPopulation:
    logger = Logger.createlogger()
    
    @classmethod
    def initialize(cls):
        # Initialize the Neo4j driver if it has not been initialized yet
        if not Driver.get_driver():
            Driver.initialize()
        cls.driver = Driver.get_driver()

    @classmethod
    def populate_data(cls):
        try:
            cls.initialize()
            # Open a session and run the Cypher query to retrieve and print data
            with cls.driver.session() as session:
                query = """
                MATCH (c:Consumer)-[r:HAS_BUSINESS_OF]->(b:Business)
                RETURN c, r, b
                """
                result = session.run(query)
                cls.logger.debug(result)
                
        except Exception as e:
            cls.logger.debug(f"An error occurred: {e}")
        finally:
            # Ensure the driver is closed
            Driver.close()

if __name__ == "__main__":
    DataPopulation.populate_data()