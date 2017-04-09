# Import the relevant modules
from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Import CNTK related modules
import cntk as C
from cntk.device import try_set_default_device, gpu, cpu
from cntk.layers import default_options, Dense
from cntk.io import StreamConfiguration, StreamDef, StreamDefs, INFINITELY_REPEAT
from cntk.io import MinibatchSource, CTFDeserializer

# Hard-coding the use of CPU
# TODO: Make this dynamic.
C.device.try_set_default_device(C.device.gpu(0))
