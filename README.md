# EcoCoin_Back

API for EcoCoin 

##Run locally 
### Venv 

first create a python virtual environment and activate it: 

```bash
$ python -m venv venv
$ source venv/bin/activate
```

###Install requirements : 
```bash 
$ python -m pip install  -r requirements.txt
```

###Set up db:

1. Create a PostgreSQL database (default name is **db_formulix**)
2. Change the `app/config/config.py` file and add the following variable: <br/>
   DATABASE_URL=postgresql://`USER`:`PASSWORD`@`HOST`:`PORT`/`db_name`