from queryExecutionAgent import queryExecutionAgent as qe
from queryGenerationAgent import queryGenerationAgent as qg
from crewai import Crew


class CrewInstance:

    crew_instance = None
        
    @classmethod
    def initialize(cls):
        obj_qe = qe()
        obj_qg = qg()
        creation_agent = obj_qg.queryAgent()
        creation_task = obj_qg.queryTask(creation_agent)
        execution_agent = obj_qe.executionAgent()
        execution_task = obj_qe.executionTask(execution_agent)
        
        cls.crew_instance = Crew(
                    agents=[creation_agent, execution_agent],
                    tasks=[creation_task, execution_task],
                    verbose=True,
                    memory=True,
                )
        
    @classmethod   
    def get_crewInstance(cls):
        if cls.crew_instance is None:
            cls.initialize()
        return cls.crew_instance