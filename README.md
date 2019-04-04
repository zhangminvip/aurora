![avatar](https://github.com/zhangminvip/aurora/blob/iss1/archi/Aurora_Web_Architecture.png)


python manage.py test  polls  --settings backend.local

dev:
--settings  local
sh run_dep_server.sh


deploy:
use uwsgi so use setting.py

change docker-compose.yml  8080:80(local dev) ->  80:80(deploy)

docker exec -it backend bash -> python manage.py migrate 



