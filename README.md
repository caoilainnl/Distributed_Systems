- **Azure SQL Server**: `dist_systems.database.windows.net`
- **Azure SQL Database**: `dist_systems`

```
Distributed_Systems/
│
├── simulated_data/
│   ├── host.json
│   ├── local.settings.json
│   ├── function/
│       ├── __init__.py
│       ├── function.json
│
├── data_statistics/
│   ├── host.json
│   ├── local.settings.json
│   ├── function/
│       ├── __init__.py
│       ├── function.json
│
└── automated_processing/
    ├── host.json
    ├── requirements.txt
    ├── .funcignore
    ├── local.settings.json
    ├── timer_trigger/
    │       ├── __init__.py
    │       ├── function.json
    ├── sql_trigger/
            ├── __init__.py
            ├── function.json
```