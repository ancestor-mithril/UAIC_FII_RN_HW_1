from datetime import datetime

start_time = datetime.now()
exec(open("python_script.py").read())
time_1 = datetime.now() - start_time
start_time = datetime.now()
exec(open("numpy_script.py").read())
time_2 = datetime.now() - start_time
print("Python script: ", time_1)
print("Numpy script: ", time_2)
