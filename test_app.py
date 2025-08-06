#!/usr/bin/env python3
"""
Simple test script to verify Flask app functionality
"""

try:
    from text_to_speech.exception import TTSException
    print("✓ TTSException imported successfully")
except Exception as e:
    print(f"✗ TTSException import failed: {e}")

try:
    from text_to_speech.components.get_accent import get_accent_tld, get_accent_message
    print("✓ get_accent module imported successfully")
    accent_list = get_accent_message()
    print(f"✓ Accent list: {accent_list}")
except Exception as e:
    print(f"✗ get_accent import failed: {e}")

try:
    from text_to_speech.components.textTospeech import TTSapplication
    print("✓ TTSapplication imported successfully")
except Exception as e:
    print(f"✗ TTSapplication import failed: {e}")

try:
    from flask import Flask
    print("✓ Flask imported successfully")
except Exception as e:
    print(f"✗ Flask import failed: {e}")

print("\nAll imports completed!") 