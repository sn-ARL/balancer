# __Balancer__

Файл client.sh - это файл с настройками доступа к API из ЛК в облаке с заполненным полем C2_PROJECT.
Файлы client.sh, main.py, start.sh должны быть исполняемыми (_chmod +x filename_)

В файле /lib/systemd/system/loadbalancer.service необходимо изменить путь до директории balancer
После этого необходимо перенести файл в директорию, согласно его названию.
Далее ввести следующие команды:
* _sudo systemctl daemon-reload_
* _sudo systemctl enable loadbalancer.service_
* _sudo systemctl start loadbalancer.service_


Перед запуском скрипта необходимо изменить данные в конфигурационном файле cfg.py. 
* publicIP - публичный IP-адрес, который выдало облакож;
* mainInterface - идентификатор внешнего сетевого интерфейса первой ноды;
* additionalInterface - идентификтор внешнего сетевого интерфейса второй ноды;
* freacuency - частота запуска скрипта в секундах;
* mainIP - IP-адрес первой ноды, в подсети балансировщика. 

>_Для корректной работы скрипта необходимо проверить наличие утилит curl, openssl.
Если Python находится не по следующему пути: /usr/bin/python3.6, то необходимо изменить путь в файле main.py_
