import yaml


filepath = "files/sample1.yml"
dict_ = {'student_name' : 'aryansh',
'subject' : 'mathematics',
'marks' : 8,
'roll_no' : 46}

with open(filepath, "w") as fo:
    yaml.dump(dict_, fo)
    