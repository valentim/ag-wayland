# AG CFD Saver
The AG CFD Saver is a microservice responsible for Cumulative Flow Diagram generation. It was written 100% in python and uses AIOHTTP client/server framework in the base.

## Usage
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
![](https://github.com/valentim/ag-cfd-saver/example/cfd.png)

## License

GNU © [AG CFD Saver](https://github.com/valentim/ag-cfd-saver)