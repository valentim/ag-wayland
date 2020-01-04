# AG CFD Saver
The AG CFD Saver is a microservice responsible for Cumulative Flow Diagram generation. It was written 100% in python and uses AIOHTTP client/server framework in the base.

## Install
```bash
pip install -r requirements.txt
```

## Usage
There are two ways to start the server:
1 - Enter into the cfd directory and execute the command below:
`python server.py`

2 - Enter into the cfd directory and use the devtools:
`adev runserver --port 8080`

The main difference between these two ways is that the second is better to the development because it has resources like debug mode and live reload.

There is a simple endpoint that generates the CFD.
### Endpoint
`[POST] - /diagrams`
### Request
```json
{
	"data": [
		{
			"column": "Done",
			"values": [{
				"x": 1570417200,
				"y": 2
			}]
		},
		{
			"column": "WIP",
			"values": [{
				"x": 1570417200,
				"y": 1
			}]
		},
		{
			"column": "Backlog",
			"values": [{
				"x": 1570417200,
				"y": 1
			}]
		}
	]
}
```
### Response
`200`
```json
{
    "success": true
}
```

### CFD
![](/example/cfd.png?raw=true)

## License

GNU © [AG CFD Saver](https://github.com/valentim/ag-cfd-saver)