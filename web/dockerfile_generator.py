if __name__ == "__main__":
    dockerfile = 'FROM python:3.6\n\n'
    dockerfile +='RUN pip install --upgrade pip\n'
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile += "RUN pip install {}\n".format(l)

    dockerfile += '\nWORKDIR /app\n'
    with open('Dockerfile', 'w') as file :
        file.write(dockerfile)
