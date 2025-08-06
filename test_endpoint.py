#!/usr/bin/env python3
"""
Test script for the Flask predict endpoint
"""
import requests
import json

# Test data
test_data = {
    "data": "Hello, this is a test message",
    "accent": "Indian"
}

def test_local_endpoint():
    """Test the predict endpoint locally"""
    try:
        # Test POST request
        response = requests.post(
            'http://localhost:5000/predict',
            json=test_data,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("✓ Endpoint test successful!")
        else:
            print("✗ Endpoint test failed!")
            
    except Exception as e:
        print(f"✗ Test failed with error: {e}")

if __name__ == "__main__":
    print("Testing Flask predict endpoint...")
    test_local_endpoint()