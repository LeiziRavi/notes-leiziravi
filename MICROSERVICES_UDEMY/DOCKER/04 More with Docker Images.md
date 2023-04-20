==If we try to run another image on the same port configuration as one already running==

```bash
docker run -p 5000:5000 in28min/hello-world-python:0.0.1.RELEASE
docker: Error response from daemon: driver failed programming external connectivity on endpoint sleepy_lamport (4e11334b32a1723ae7d9be53d19c5872c7fbb77c69ba6fab4b91671d71bf43f5): Bind for 0.0.0.0:5000 failed: port is already allocated.

```

==To run two application at once==
- Change the host port number

```bash
 leiziravi  ~ docker run -p 5001:5000 in28min/hello-world-python:0.0.1.RELEASE
 * Serving Flask app 'launch' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses (0.0.0.0)
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 127-048-204

```

==Run==
![[Running two containers at once on Host machine.png]]