import sys


if __name__ == "__main__":
    is_prod = False
    if len(sys.argv) == 2 and sys.argv[1] == 'prod':
        is_prod = True

    if is_prod:
        dockerfile = '''FROM mdock.daumkakao.io/python:3.6

ENV HTTP_PROXY http://proxy.daumkakao.io:3128
ENV HTTPS_PROXY http://proxy.daumkakao.io:3128
ENV http_proxy http://proxy.daumkakao.io:3128
ENV https_proxy http://proxy.daumkakao.io:3128

'''
    else:
        dockerfile = 'FROM python:3.6\n\n'

    dockerfile +='RUN pip install --upgrade pip\n'
    for l in open('requirements.txt'):
        l = l.strip()
        if not l or l.startswith('#'):
            continue
        dockerfile += "RUN pip install {}\n".format(l)

    if is_prod:
        dockerfile += '''
ENV HTTP_PROXY=
ENV HTTPS_PROXY=
ENV http_proxy=
ENV https_proxy=
'''
    dockerfile += '\nWORKDIR /app\n'
    with open('Dockerfile', 'w') as file :
        file.write(dockerfile)
