import json
import subprocess

file = open("package.json", "r")
converted = json.loads(file.read())

# Loop modules and update
if "devDependencies" in converted:
	for key, val in converted['devDependencies'].items():
		subprocess.call(["npm", "i", "-D", key+"@latest"], shell=True)

print(file.read())