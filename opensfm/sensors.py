# -*- coding: utf-8 -*-

import string
import json

from opensfm import context

with open(context.SENSOR,'rb') as f:
    sensor_data = json.loads(f.read())

# Convert model types to lower cases for easier query
sensor_data = dict(zip(map(lambda x:x.lower(),sensor_data.keys()),sensor_data.values()))
