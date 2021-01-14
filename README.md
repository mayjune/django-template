# DjangoTemplate

## Prerequisites
```bash
# set alias in your ~/.bashrc or ~/.zshrc
alias dc='docker-compose'
alias rpm='dc exec web python manage.py'
alias rpmsh='dc exec web python manage.py shell_plus'
```

## Run
```bash
cd web
./build.sh
dc up -d
```

## Create Admin
```bash
rpm createsuperuser
```

## Set Server Env & Deployment Manual
[go manual](https://wiki.daumkakao.com/pages/viewpage.action?pageId=606796416)


## Deployment
```bash
python deploy.py --branch master
```
