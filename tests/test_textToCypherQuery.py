import pytest
from crewai import Agent, Task
from src.textToCypherQuery import TextToCypher


@pytest.fixture
def class_instance():
    return TextToCypher()


class TestTextToCypher:
    
    def test_getSchema(self,class_instance):
        schema = class_instance.get_schema()
        assert schema is not None
        assert type(schema) == str
        
        
     
    def test_run_with_empty_input(self,class_instance):
        with pytest.raises(ValueError, match="Input text should not be empty"):
            string=""
            class_instance.run(string)
            
            
    def test_run_with_delete_query(self,class_instance):
        text1 = "give me the count of all the nodes in the graph and returns this count as 'nodeCount'"
        
        initial_nodes = class_instance.run(text1)
        
        text2 = "give me the count of relationships labeled 'HAS_BUSINESS_OF' between Consumers and Businesses nodes where the relationship is from Consumers to Businesses in the graph and returns it as 'edgeCount'"
         
        initial_edges = class_instance.run(text2)
         
        example_query = "give me the list of consumers whose business name is Arlin Toomey"
         
        class_instance.run(example_query)
         
        final_nodes = class_instance.run(text1)
        
        final_edges = class_instance.run(text2)
        
        assert "130" in initial_nodes
        assert "130" in final_nodes
        
        assert "100" in initial_edges
        assert "100" in final_edges
        
        # assert initial_nodes==final_nodes
        # assert initial_edges==final_edges
        
        
    def test_run_with_sampleQuery(self,class_instance):
        example_query = "give me the list of consumers whose business name is Arlin Toomey"
        
        result = class_instance.run(example_query)
        
        assert "Putnam Nelmes" in result
        assert "Alberto Kief" in result
        assert "Dermot Pactat" in result
         