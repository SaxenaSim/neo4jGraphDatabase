import pytest
from dotenv import load_dotenv
from src.driver import Driver

class TestDriver:
    # @pytest.fixture
    # def setup(self):
    #     load_dotenv()
    #     return Driver()

    def test_get_driver(self):
        neo4j_driver = Driver.get_driver()
        assert neo4j_driver is not None

