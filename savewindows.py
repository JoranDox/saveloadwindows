#! python

import subprocess
import pandas as pd
import sys

def getwindows(verbose=True):
    r = subprocess.run(
        ["wmctrl", "-lGxp"],
        check=True,
        capture_output=True,
    )


    df = pd.DataFrame.from_records(
        list(s.split(maxsplit=9) for s in r.stdout.decode().split("\n") if s),
        columns=["id", "idk", "gravity", "X", "Y", "width", "height", "program", "desktopmaybe", "title"]
    )
    if verbose:
        print(df)
    return df

def savewindows(loc="~/Desktop/savedwindows.csv", verbose=True):
    df = getwindows(verbose=verbose)
    df.to_csv(loc)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        part = sys.argv[-1]
    else:
        part = ""
    loc = f"~/Desktop/savedwindows{part}.csv"

    savewindows(loc)
    print(f"saved to {loc}")