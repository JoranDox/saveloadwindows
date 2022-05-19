# saveloadwindows

Working on a laptop, from home, from the office with several different (and different-sized) external screens (or none), my windows move around like crazy, and it's a pain to put them back in the initial configuration so I wrote a little python script to help me.
It's messy, and could probably do without pandas, but it's provided here in case it's useful to someone.

## How it works

**savewindows.py**

- Uses [wmctrl](https://linux.die.net/man/1/wmctrl) to get & set the window settings (most importantly **"id", "gravity", "X", "Y", "width", "height"**).
- Uses a [pandas](https://pandas.pydata.org/) DataFrame to keep the window settings in memory.
- Saves the window settings to a csv ("~/Desktop/savedwindows.csv" if no command line parameters, otherwise it formats the string like this: f"~/Desktop/savedwindows{part}.csv")

**loadwindows.py**

- Loads the csv saved by savewindows.py with the same interpolation rules.
- Uses a pandas DataFrame again to keep the window settings in memory.
- For each window, uses wmctrl again to set the settings back
  - As wmctrl has some issues in putting the right x/y settings back when using system borders, I've put a workaround in: in my configuration system borders change (x,y,w,h) by (0,29,0,0), so I've set the default to (0,-29,0,0) to compensate. In my case, my browser doesn't use system borders so I've put in an override list. Also if there are programs you don't want to change, there's an ignorelist too (I use it for my system bar).

**saveloadtest.py**

This script is used to get the right configuration for the system borders if wmctrl is using the wrong numbers, it should print the differences between getting the window locations before and after "restoring" them. If it's all 0, it should be fine, otherwise you should probably change one or more of the ignorelist, the known diffs, or the default diff in loadwindows.py.
