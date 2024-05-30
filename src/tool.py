from crewai_tools import BaseTool
from driver import Driver


# Tool class to execute Cypher queries on the Neo4j database
class Neo4jQueryTool(BaseTool):
    name:str="Neo4j Quering Tool"
    description:str="The input to this tool is a cypher query string to execute on neo4j database. This tool executes the query and returns the result"
    # Get the Neo4j driver and execute the query   
    def _run(self,query):
        driver = Driver.get_driver()
        with driver.session() as session:
            print("::: TOOL:: query :::", query)
            result = session.run(query)
            records = list(result)  
        return records