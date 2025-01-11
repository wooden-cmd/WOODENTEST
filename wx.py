import pandas as pd
import numpy as np
from uiautomation import *

wx=WindowControl(searchDepth=5,Name='微信')
button=wx.ButtonControl(searchDepth=2,Name='通讯录')
button.Click()