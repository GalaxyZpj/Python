from os import system
from base64 import b64decode
import requests, json

# Global
URL = ''
language_d = {}
data_d = {}
result = None
use_base64 = False

# Functions
def initialize(url, language, data, testcases=None):
    global URL
    global language_d
    global data_d
    URL = url
    language_d = language
    data_d = data

def code_string():
    print('Enter your code:-')
    with open('Sample.txt', 'w') as f:
        while True:
            s = input()
            if s == '': break
            f.write(s)
            f.write('\n')
    with open('Sample.txt', 'r') as f:
        data_s = f.read()
    return data_s

def language_id(l):
    global use_base64
    for x in l:
        print('{}: {}'.format(x['id'], x['name']))
    i = int(input('Choose amoung following languages: '))
    if i == 1: s = str(4)
    elif i == 2: s = str(10)
    elif i == 3: s = str(16)
    elif i == 4: s = str(26)
    elif i == 5: s = str(29)
    elif i == 6: s = str(34)
    else: s = str(i)
    if s == '4' or s == '10' or s == '16' or s == '26': use_base64 = True
    return s

def prep_submissionDict():
    data_d["language_id"] = language_id(language_d)
    system('clear')
    data_d["source_code"] = code_string()
    return data_d

def generate_token(data):
    r = requests.post(URL, data)
    if r.status_code == 201: return r.json()
    elif r.status_code == 401:
        print('Authentication Failed')
        quit()
    elif r.status_code == 422:
        print('Language ID invalid')
        quit()

def fetch_server(token):
    while True:
        system('clear')
        print('OUTPUT:-')
        print('Processing...')
        if use_base64 == True: useb64 = 'true'
        else: useb64 = 'false'
        r = requests.get(URL + token['token'] + '?base64_encoded=' + useb64)
        if r.status_code != 200: break
        else:
            r = r.json()
            if r['status']['id'] == 1 or r['status']['id'] == 2: continue
            else:
                if use_base64 == True:
                    if r['stdout'] != None: r['stdout'] = decrypt(r['stdout'])
                    if r['compile_output'] != None: r['compile_output'] = decrypt(r['compile_output'])
                    if r['message'] != None: r['message'] = decrypt(r['message'])
                    if r['stderr'] != None: r['stderr'] = decrypt(r['stderr'])
                    #print(r)
                return [1, r]
    x = r.status_code
    if x == 401: return [0, {'error': 'Authentication Failed', 'exception': 'Unknown'}]
    elif x == 500:
        return

def display_output(o):
    if o[0] == 1:
        """if o[1]['status']['id'] == 3 or o[1]['status']['id'] == 4:
            print('STDOUT: ', o[1]['stdout'])
            print('Description: ', o[1]['status']['description'])
        else:
            print(o[1]['status']['description'], o[1]['stderr'])"""
        print('::: ',o[1]['status']['description'].upper(),' :::')
        if o[1]['stdout'] != None: print('STDOUT:\n', o[1]['stdout'])
        if o[1]['time'] != None: print('TIME:\n', o[1]['time'])
        if o[1]['stderr'] != None: print('STDERR:\n', o[1]['stderr'])
        if o[1]['compile_output'] != None: print('COMPILE OUTPUT:\n', o[1]['compile_output'])
        if o[1]['message'] != None: print('MESSAGE:\n', o[1]['message'])
    elif o[0] == 0:
        print('\nError: ', o[1]['error'])
        print('Exception: ',o[1]['exception'])

def decrypt(s):
    return b64decode(s).decode()
