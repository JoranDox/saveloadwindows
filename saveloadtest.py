#! python

import subprocess
import pandas as pd
import sys

import sys
sys.path.append("~/Desktop") # ugly leftover from when the python files were just on my desktop

from savewindows import getwindows, savewindows
from loadwindows import loadwindows, putwindows

loc = "~/Desktop/saveloadtest.csv"

df = getwindows()
putwindows(df)
df2 = getwindows()

print(df)
print(df2)
print(df2.X.astype(int) - df.X.astype(int))
print(df2.Y.astype(int) - df.Y.astype(int))
print(df2.width.astype(int) - df.width.astype(int))
print(df2.height.astype(int) - df.height.astype(int))