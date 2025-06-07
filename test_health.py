#!/usr/bin/env python3
import requests

try:
    print("Testing health endpoint...")
    r = requests.get('http://localhost:8000/health')
    print(f"Status: {r.status_code}")
    print(f"Response: {r.text}")
except Exception as e:
    print(f"Error: {e}")
