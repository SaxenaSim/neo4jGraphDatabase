from driver import Driver

class DataPopulation:
    
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
                print(result)
                for record in result:
                    #print(record)
                    consumer = record['c']
                    relationship = record['r']
                    business = record['b']
                    print(f"Consumer: {consumer['name']}, Age: {consumer['age']}")
                    print(f"Relationship: {relationship.type}")
                    print(f"Business: {business['name']}, Industry: {business['industry']}")
                    print('-' * 20)
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Ensure the driver is closed
            Driver.close()

if __name__ == "__main__":
    DataPopulation.populate_data()