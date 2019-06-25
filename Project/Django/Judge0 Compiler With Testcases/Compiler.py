import CompilerModule as core

URL = 'https://api.judge0.com/submissions/'
languages = [
  {"id": 1,"name": "C (gcc 7.2.0)"},
  {"id": 2,"name": "C++ (g++ 7.2.0)"},
  {"id": 3,"name": "C# (mono 5.4.0.167)"},
  {"id": 4,"name": "Java (OpenJDK 9 with Eclipse OpenJ9)"},
  {"id": 5,"name": "JavaScript (nodejs 8.5.0)"},
  {"id": 6,"name": "Python (3.6.0)"},
]
data = {
    "source_code": None,
    "language_id": None,
    "number_of_runs": "1",
    "stdin": None,
    "expected_output": None,
    "cpu_time_limit": "2",
    "cpu_extra_time": "0.5",
    "wall_time_limit": "5",
    "memory_limit": "128000",
    "stack_limit": "64000",
    "max_processes_and_or_threads": "30",
    "enable_per_process_and_thread_time_limit": False,
    "enable_per_process_and_thread_memory_limit": True,
    "max_file_size": "1024"
}

core.system('clear')
core.initialize(URL, languages, data)
s_dict = core.prep_submissionDict()
token = core.generate_token(s_dict)
response = core.fetch_server(token)
core.display_output(response)
