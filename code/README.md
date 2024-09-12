# Instructions

## Running Defense Mechanism Scenarios

To run a scenario using a specific defense mechanism, follow these steps:

1. **Go to the defense system's subdirectory**: Each defense mechanism is located in its respective subdirectory under `defenses/`. For example, to run a scenario using the DINAR defense system, you would navigate to the following directory:
```bash
   cd defenses/dinar
``` 
2. **Execute the `run.py` file with Python**
```bash
   python run.py
``` 
## Experimental Parameters

The experimental parameters for each defense mechanism are located in the corresponding subdirectory and are handled by the associated `parser.py` file. For instance, the parameters for DINAR are found in:

```defenses/dinar/parser.py```

Make sure to review or adjust these parameters in the `parser.py` file before running the scenarios to fit your experimental setup.
