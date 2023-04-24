# Django Interview Question

In this task you will write a small Django API from which numerical data read from sensors placed on a Wind Turbine can be retrieved or stored. Please carry the task out as though this was a task you had been asked to complete in your day-to-day role. We don't expect that the task should take more than an hour.

The requirements are:

* Create a model and API (at `/api/sensor/`) to represent a "sensor". You should be able to create sensors at the end point with a payload like `'{"name": "Main Bearing Temperature", "unit": "Celsius"}'`. Sensor names should be unique. You should be able to retrieve information about a specific sensor at `/api/sensor/<sensor_id>/` and a list of all of the sensors at `/api/sensor/`.
* Create an API endpoint to store data records at `/api/data/` which you can store and retrieve floating point numerical measurements from sensors. You should be able to POST at the end point and create records. The payload for such a request should look like `{"date": "2022-04-27 12:13", "sensor": "Main Bearing Temperature", "value": 12.0"}`. You can assume that all values are floating point numbers. You should be able to retrieve information about a specific data record at `/api/data/<record_id>/` and a list of all of the records at `/api/data/`. You should add filtering to this endpoint so that, using query parameters, it is possible to retrieve records with filters relating to a particular sensor, for specific date ranges, and when values are above or below a specified threshold.
* Please ensure that your API endpoints are documented using OpenAPI and are visible when running your server through a web UI like Swagger or Redoc. You might find it easiest to use a tool like drf_spectacular to do this.
