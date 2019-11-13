DATE=`date +%Y-%m-%d`

echo "criando mysqldump zabbix"
mysqldump -u root zabbix > /tmp/zabbix-$DATE.sql

echo "criando tar.bz2"
tar -cjvf /tmp/zabbix-$DATE.tar.bz2 /tmp/zabbix-$DATE.sql

echo "removendo sql"
rm -rf /tmp/zabbix-$DATE.sql

echo "transferindo remoto"
sshpass -p 'senha' scp /tmp/zabbix-2019-05-25.tar.bz2 root@localhost:/nfs/ZABBIX/

echo "fim"
