import yaml


filepath = "files/sample.yml"

with open(filepath, "r") as fp:
    try:
        content = yaml.safe_load(fp)
    except Exception as e:
        print(e)
    print(content)