from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "highest_building"
    FUNCTION_NAMES = {
        "python_3": "highest_building",
        "js_node": "highestBuilding"
    }
    ENV_COVERCODE = {
        
    }