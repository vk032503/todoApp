#!/usr/bin/env python3
"""
Test script to verify the login endpoint is working
"""

import requests
import json

def test_login():
    """Test the login endpoint"""
    url = "http://localhost:8000/auth/login"
    credentials = {
        "username": "VK25",
        "password": "Ready2g@"
    }
    
    try:
        print("🔐 Testing login endpoint...")
        print(f"URL: {url}")
        print(f"Credentials: {credentials}")
        
        response = requests.post(url, json=credentials)
        
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Login successful!")
            print(f"Response: {json.dumps(data, indent=2)}")
            
            # Test the /auth/me endpoint
            token = data.get('access_token')
            if token:
                print("\n👤 Testing user profile endpoint...")
                headers = {"Authorization": f"Bearer {token}"}
                me_response = requests.get("http://localhost:8000/auth/me", headers=headers)
                print(f"Profile Status: {me_response.status_code}")
                if me_response.status_code == 200:
                    print(f"Profile Data: {json.dumps(me_response.json(), indent=2)}")
                else:
                    print(f"Profile Error: {me_response.text}")
        else:
            print("❌ Login failed!")
            print(f"Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Connection error: {e}")

if __name__ == "__main__":
    test_login()
