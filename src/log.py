import os , yaml
import logging , logging.config

class Logger:
    _logger = None
    
    @classmethod
    def createlogger(cls):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root_dir = os.path.dirname(current_dir)

        config_logging_path = os.path.join(project_root_dir, "logging_config.yaml")
        print(config_logging_path)

        with open(config_logging_path, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        cls._logger = logging.getLogger(__name__)

    @classmethod
    def getlogger(cls):
        if cls._logger is None:
            cls.createlogger()
        return cls._logger
        