import os
from datetime import datetime

base_link = "https://github.com/joebost/aoc/blob/main/src/"


def parse(e):
    name = e.replace(".py", "")
    # name = " ".join(name.split("_")[1:])
    return f"[{name}]({base_link}{e})"


solutions = filter(lambda x: ".py" in x and "init" not in x, os.listdir("src"))

readme_content = f"""# Advent of code {datetime.now().year}
[Leaderboard](https://adventofcode.com/2022/leaderboard/private/view/1686733)

### Problems list:
"""

tmp = [f"{i+1}. {parse(e)}" for i, e in enumerate(sorted(solutions))]
readme_content += "\n".join(tmp)

with open("README.md", "w") as f:
    f.write(
        readme_content
    )
