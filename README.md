# Django Interview Question

In this task you will write a small Django API from which numerical data read from sensors placed on a Wind Turbine can be retrieved or stored. Please carry the task out as though this was a task you had been asked to complete in your day-to-day role. We don't expect that the task should take more than an hour.

The requirements are:

* Create a model and API (at `/api/sensor/`) to represent a "sensor". You should be able to create sensors at the end point with a payload like `'{"name": "Main Bearing Temperature", "unit": "Celsius"}'`. Sensor names should be unique. You should be able to retrieve information about a specific sensor at `/api/sensor/<sensor_id>/` and a list of all of the sensors at `/api/sensor/`.
* Create an API endpoint to store data records at `/api/data/` which you can store and retrieve floating point numerical measurements from sensors. You should be able to POST at the end point and create records. The payload for such a request should look like `{"date": "2022-04-27 12:13", "sensor": "Main Bearing Temperature", "value": 12.0"}`. You can assume that all values are floating point numbers. You should be able to retrieve information about a specific data record at `/api/data/<record_id>/` and a list of all of the records at `/api/data/`. You should add filtering to this endpoint so that, using query parameters, it is possible to retrieve records with filters relating to a particular sensor, for specific date ranges, and when values are above or below a specified threshold.
* Please ensure that your API endpoints are documented using OpenAPI and are visible when running your server through a web UI like Swagger or Redoc. You might find it easiest to use a tool like drf_spectacular to do this.


# Specific Implementation

## Requirements

### Python Environment

- [Install Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- Ensure `conda` is in your `PATH`

Create a Conda environment…
```commandline
conda create -n interview_question python=3.10
```

Activate the created Conda environment…
```commandline
conda activate interview_question
```

Navigate to the base directory of this repository and install requirements…
```commandline
cd arron-paul
pip install -r requirements.txt
```

### Database & Environment Variables

Ensure that you have a database such as Postgres available locally. SQLite is used as a fallback option.

Modify `.env`…
- The entries in `.env` are commented out by default. Once uncommented, they will override variables defined in `settings.py`
- Provide a `DATABASE_URL` in `.env` that points to a valid database. `DATABASE_URL` is a URI-formatted connection string.
- Additional entries can be uncommented to suit your environment.
- Alternatively, if you don’t wish to use `.env`, ensure that all relevant variables are defined before running the app.

### Initial Data

- Migrate the database…
```commandline
python manage.py migrate
```

- Create a Superuser…
```commandline
python manage.py createsuperuser
```

- Populate `Sensors` and `SensorRecords` _(optional)_…
```commandline
python manage.py populate
```

### Run the App
```commandline
python manage.py runserver
```

## API

```commandline
HTTP GET /api/data/?date_from=2020-01-01T00:00:00Z&date_to=2021-01-01T00:00:00Z
```

```commandline
HTTP GET /api/data/?sensor=Front%20Temperature%20Sensor
```

```commandline
HTTP GET /api/data/?value_min=10&value_max=50
```