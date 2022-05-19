#! python

import subprocess
import pandas as pd
import sys

default_diff = (0, -29, 0, 0) # system borders
knowndiffs = {
    "brave-browser.Brave-browser": (0, 0, 0, 0), # I've got system borders turned off for brave
}
ignoreprograms = {
    "plasmashell.plasmashell" # this one automatically get set correctly and I don't want to mess with it
}


def putwindows(df, verbose=True):

    for line in df.itertuples():
        if line.program not in ignoreprograms:
            diffx, diffy, diffw, diffh = knowndiffs.get(line.program, default_diff)
            if verbose:
                print(f"setting {line.program}: {line.title} back")

            r = subprocess.run(
                [
                    "wmctrl",
                    "-i",
                    "-r",
                    line.id,
                    "-e",
                    ",".join(
                        str(x)
                        for x in [
                            line.gravity,
                            int(line.X) + diffx,
                            int(line.Y) + diffy,
                            int(line.width) + diffw,
                            int(line.height) + diffh,
                        ]
                    ),
                ],
                check=True,
                capture_output=True,
            )
            if verbose:
                print("output:")
                print(r)


def loadwindows(loc=f"~/Desktop/savedwindows.csv", verbose=True):

    df = pd.read_csv(loc)
    if verbose:
        print(df)
    return df


if __name__ == "__main__":
    if len(sys.argv) > 1:
        part = sys.argv[-1]
    else:
        part = ""
    loc = f"~/Desktop/savedwindows{part}.csv"
    putwindows(loadwindows(loc = loc))
    print(f"got from {loc}")
