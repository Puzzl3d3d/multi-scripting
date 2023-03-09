from script import script

script1 = open("script1")
script2 = open("script2")

script1 = script().parse_file(script1)
script2 = script().parse_file(script2)

print(script.get_scripts())

script.start_all_scripts()