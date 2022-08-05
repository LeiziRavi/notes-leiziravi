1. To start aerospike server
```bash
sudo service aerospike start
```
or 
```shell
systemctl start aerospike
```

2. To check status of aerospike server
```shell
sudo service aerospike status
```
or
```shell
systemctl status aerospike
```

```shell
leiziravi@leiziravi:~/aerospike-tools-7.0.5-ubuntu20.04$ sudo service aerospike status
● aerospike.service - Aerospike Server
     Loaded: loaded (/lib/systemd/system/aerospike.service; disabled; vendor preset: enabled)
    Drop-In: /etc/systemd/system/aerospike.service.d
             └─aerospike.conf
     Active: active (running) since Tue 2022-07-05 00:15:46 IST; 8s ago
    Process: 142098 ExecStartPre=/usr/bin/asd-systemd-helper (code=exited, status=0/SUCCESS)
    Process: 142104 ExecStartPre=/bin/systemctl start aerospike_telemetry (code=exited, status=0/SUCCESS)
   Main PID: 142106 (asd)
      Tasks: 117 (limit: 8791)
     Memory: 125.8M
     CGroup: /system.slice/aerospike.service
             └─142106 /usr/bin/asd --config-file /etc/aerospike/aerospike.conf --fgdaemon

```

> 
> The status command doesn't inform you when the service port is ready, instead use the **STATUS** info command which will return "OK" when ready:
> 

```shell
asinfo -v STATUS
```

## Restart Aerospike Server

The `restart` command is equivalent to running `stop` followed by `start`:
```shell
systemctl restart aerospike
```

## Stop Aerospike Server

To shut down the Aerospike Server use the `stop` command:

```
systemctl stop aerospike
```

> __==NOTE==:__
> Aerospike flushes the data in the buffers to the disk (if data is configured to be persisted on device) when Aerospike is stopped gracefully. However, in other situations (unexpected loss of power, process crash), the data present in the buffer may not make it to the device. Single node crashes with a replication-factor of 2 will not cause any data loss, though. For multiple nodes crashing simultaneously, different configurations can be used to avoid any data loss, including, for example, [rack aware](https://docs.aerospike.com/server/operations/configure/network/rack-aware) and [`commit-to-device`](https://docs.aerospike.com/reference/configuration#commit-to-device) (available on [strong-consistency](https://docs.aerospike.com/reference/configuration#strong-consistency) namespaces in versions 4.0 and above).
> 