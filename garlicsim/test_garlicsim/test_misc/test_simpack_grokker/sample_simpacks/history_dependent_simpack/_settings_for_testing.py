import garlicsim

from .state import State

HISTORY_DEPENDENT = True
N_STEP_FUNCTIONS = 1
DEFAULT_STEP_FUNCTION = State.history_step
DEFAULT_STEP_FUNCTION_TYPE = \
    garlicsim.misc.simpack_grokker.step_types.HistoryStep
CRUNCHERS_LIST = [garlicsim.asynchronous_crunching.crunchers.ThreadCruncher]