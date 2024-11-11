# API.PY Documentation

This module defines a simple Flask web application with an endpoint to sort a list of numbers.

## Endpoints

### POST /sort

Sorts a list of numbers provided in the request body.

#### Request Body

The request body must be a JSON object containing a key `numbers` which is a list of numbers (integers or floats).

Example:

{
	"numbers": [1, 2, 6, 2, 8]
}

Return:

{
	"sorted_numbers": [ 1, 2, 2, 6, 8]
}