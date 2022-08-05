```yaml
api:
	build: ./backend
	ports:
		- 3001:3001
	environment:
		DB_URL: mongodb://db/vidly
	volumes:
		- ./backend:/app
```