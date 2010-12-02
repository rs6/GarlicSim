import nose.tools

import garlicsim
from garlicsim.asynchronous_crunching.crunchers import PiCloudCruncher

def test_pi_cloud_cruncher():
    
    nose.tools.raises(NotImplementedError, PiCloudCruncher)
    
    from test_garlicsim.test_misc.test_simpack_grokker.sample_simpacks import \
         simpack
    simpack_grokker = garlicsim.misc.SimpackGrokker(simpack)
    
    availability = \
        PiCloudCruncher.can_be_used_with_simpack_grokker(simpack_grokker)
    assert availability == False