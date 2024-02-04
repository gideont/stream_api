#/bin/bash

#uvicorn main:app --reload --host 0.0.0.0 --port 3009
uvicorn main:app --host 0.0.0.0 --port 3009 --workers 2 &
