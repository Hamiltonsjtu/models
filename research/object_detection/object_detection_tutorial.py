import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from distutils.version import StrictVersion
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from object_detection.utils import ops as utils_ops

print(tf.__version__)
# if StrictVersion(tf.__version__) < StrictVersion('1.12.0'):
#   raise ImportError('Please upgrade your TensorFlow installation to v1.12.*.')
saver = tf.train.imp