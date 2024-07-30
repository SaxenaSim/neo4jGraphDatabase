from src.tool import Neo4jQueryTool
from src.queryExecutionAgent import QueryExecutionAgent

def test_task_tool():
    obj = QueryExecutionAgent()
    agent = obj.executionAgent()
    task = obj.executionTask(agent)
    
    assert task.tools == [Neo4jQueryTool]