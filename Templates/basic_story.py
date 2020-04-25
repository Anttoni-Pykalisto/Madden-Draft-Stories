print('creating test story')

import json

story_name = "egregious_growth_spurt.json"
path = "../Stories/" + story_name

name = ""
base_story_report = ""
applies_to = ""
effect = ""

story = {
    "story": {
        "name": "Egregious Growth Spurt",
        "base story report": "[Player] has had an egregious growth spurt in the year leading to the draft, he has growing to an insane 7 feet",
        "applies to": ["ALL"],
        "effect": "Selected player's height changed to 7 feet"
    }
}

with open(path, "w") as write_file:
    json.dump(story, write_file)