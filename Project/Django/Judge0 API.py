import requests, json
from os import system

testcases = {
    'Layout_test': {'stdin': 'str', 'expected_output': 'str', 'description': 'comment_result'},
    1: {'stdin': '4\n16\n', 'expected_output': '20', 'description': 'comment_result'},
    2: {'stdin': '300000\n100000\n', 'expected_output': '400000', 'description': 'comment_result'},
    3: {'stdin': '600\n100000\n', 'expected_output': '10060', 'description': 'comment_result'}
}

languages = [
  {"id": 1,"name": "Bash (4.4)"},
  {"id": 2,"name": "Bash (4.0)"},
  {"id": 3,"name": "Basic (fbc 1.05.0)"},
  {"id": 4,"name": "C (gcc 7.2.0)"},
  {"id": 5,"name": "C (gcc 6.4.0)"},
  {"id": 6,"name": "C (gcc 6.3.0)"},
  {"id": 7,"name": "C (gcc 5.4.0)"},
  {"id": 8,"name": "C (gcc 4.9.4)"},
  {"id": 9,"name": "C (gcc 4.8.5)"},
  {"id": 10,"name": "C++ (g++ 7.2.0)"},
  {"id": 11,"name": "C++ (g++ 6.4.0)"},
  {"id": 12,"name": "C++ (g++ 6.3.0)"},
  {"id": 13,"name": "C++ (g++ 5.4.0)"},
  {"id": 14,"name": "C++ (g++ 4.9.4)"},
  {"id": 15,"name": "C++ (g++ 4.8.5)"},
  {"id": 16,"name": "C# (mono 5.4.0.167)"},
  {"id": 17,"name": "C# (mono 5.2.0.224)"},
  {"id": 18,"name": "Clojure (1.8.0)"},
  {"id": 19,"name": "Crystal (0.23.1)"},
  {"id": 20,"name": "Elixir (1.5.1)"},
  {"id": 21,"name": "Erlang (OTP 20.0)"},
  {"id": 22,"name": "Go (1.9)"},
  {"id": 23,"name": "Haskell (ghc 8.2.1)"},
  {"id": 24,"name": "Haskell (ghc 8.0.2)"},
  {"id": 25,"name": "Insect (5.0.0)"},
  {"id": 26,"name": "Java (OpenJDK 9 with Eclipse OpenJ9)"},
  {"id": 27,"name": "Java (OpenJDK 8)"},
  {"id": 28,"name": "Java (OpenJDK 7)"},
  {"id": 29,"name": "JavaScript (nodejs 8.5.0)"},
  {"id": 30,"name": "JavaScript (nodejs 7.10.1)"},
  {"id": 31,"name": "OCaml (4.05.0)"},
  {"id": 32,"name": "Octave (4.2.0)"},
  {"id": 33,"name": "Pascal (fpc 3.0.0)"},
  {"id": 34,"name": "Python (3.6.0)"},
  {"id": 35,"name": "Python (3.5.3)"},
  {"id": 36,"name": "Python (2.7.9)"},
  {"id": 37,"name": "Python (2.6.9)"},
  {"id": 38,"name": "Ruby (2.4.0)"},
  {"id": 39,"name": "Ruby (2.3.3)"},
  {"id": 40,"name": "Ruby (2.2.6)"},
  {"id": 41,"name": "Ruby (2.1.9)"},
  {"id": 42,"name": "Rust (1.20.0)"},
  {"id": 43,"name": "Text (plain text)"}
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
for x in languages:
    print('{}: {}'.format(x['id'], x['name']))
lang_choice = input('Choose amoung following languages: ')
system('clear')
print('SUM OF TWO INTEGERS: Take 2 integers as input and print their sum.')
print('Enter your code:-')
with open('/Users/pranavjain/Github/Python/Sample.txt', 'w') as f:
    while True:
        s = input()
        if s == '': break
        f.write(s)
        f.write('\n')
with open('/Users/pranavjain/Github/Python/Sample.txt', 'r') as f:
    data_s = f.read()
data["source_code"] = str(data_s)
data["language_id"] = str(lang_choice)

system('clear')
print('::::: TESTCASES :::::')
for x in range(1, 4):
    data["expected_output"] = testcases[x]['expected_output']
    data["stdin"] = testcases[x]['stdin']
    token = requests.post('https://api.judge0.com/submissions', data).json()
    #system('clear')
    print(f'\nTestcase {x}')
    print('Processing...')
    while True:
        rg = requests.get('https://api.judge0.com/submissions/' + token['token'])
        rg = rg.json()
        if rg['time'] != None: break
    #system('clear')
    print(':stdin:')
    print(testcases[x]['stdin'])
    print('OUTPUT: ', end = '')
    print(rg['stdout'])
    print(rg)
    if rg['status']['description'] == 'Accepted': print('Success')
    else:
        print('Wrong Answer')
        print('Expected: ', testcases[x]['expected_output'])
