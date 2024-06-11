import pytest
from crewai import Agent, Task
from src.queryExecutionAgent import queryExecutionAgent

@pytest.fixture
def agent_instance():
    return queryExecutionAgent()

class TestQueryExecutionAgent:
    
    def test_executionAgent_success(self, agent_instance):
        # Act
        result = agent_instance.executionAgent()
        # Assert
        assert isinstance(result, Agent)
        
    def test_executionAgent_notNull(self,agent_instance):
        result = agent_instance.executionAgent()
        assert result is not None


    def test_executionTask_success(self, agent_instance):
        # Arrange
        creation_agent = agent_instance.executionAgent() 
        # Act
        result = agent_instance.executionTask(creation_agent)
        # Assert
        assert isinstance(result, Task)
        
        
    def test_executionTask_notNull(self,agent_instance):
        creation_agent = agent_instance.executionAgent()
        result = agent_instance.executionTask(creation_agent)
        assert result is not None






















# import pytest
# from crewai import Agent, Task
# from src.queryGenerationAgent import queryGenerationAgent 


# class TestQueryGenerationAgent:
#     def __init__(self):
#         self.obj = queryGenerationAgent()
    
#     # # Define the fixture
#     # @pytest.fixture
#     # def agent_instance(self):
#     #     return queryGenerationAgent()


#     def test_queryAgent_success(self):
#         print("entering test_queryAgent_success")
#         # Act
#         result = self.obj.queryAgent()
#         print("getting the result")
#         # Assert
#         assert isinstance(result, Agent), "The result should be an instance of Agent"

#     def test_queryAgent_failure(self):
#         print("entering test_queryAgent_success")

#         # Act & Assert
#         with pytest.raises(Exception):
#             self.obj.queryAgent()

#     def test_queryTask_success(self):
#         print("entering test_queryAgent_success")

#         # Arrange
#         creation_agent = self.obj.queryAgent()  # Assuming queryAgent works fine

#         # Act
#         result = self.obj.queryTask(creation_agent)
        
#         # Assert
#         assert isinstance(result, Task), "The result should be an instance of Task"

#     def test_queryTask_failure(self):
#         print("entering test_queryAgent_success")

#         # Act & Assert
#         with pytest.raises(Exception):
#             self.obj.queryTask(None)  # Passing None to simulate failure
