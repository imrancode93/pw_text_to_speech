from text_to_speech.exception import TTSException
from text_to_speech.logger import logger
from text_to_speech.entity.config_entity import TTSConfig
import sys, os
from text_to_speech.constants import TEXT_FILE_NAME, CURRENT_TIME_STAMP
from gtts import gTTS
import base64
import tempfile
import io

# It takes in a text and an accent, and returns a base64 encoded string of the audio file
class TTSapplication():
    def __init__(self, app_config=TTSConfig()) -> None:
        try:
            self.app_config = app_config
            self.artifact_dir = app_config.artifact_dir
            self.audio_dir = app_config.audio_dir
            self.text_dir = app_config.text_dir
        except Exception as e:
            raise TTSException(e, sys)
    
    def text2speech(self, text, accent):
        """
        It takes in a text and an accent, and returns a base64 encoded string of the audio file
        
        Args:
          text: The text that you want to convert to speech.
          accent: The accent of the voice.
        
        Returns:
          The audio file in base64 format.
        """
        try:
            # Create object for gtts
            tts = gTTS(text=text, lang='en', tld=accent, slow=False)

            # Use temporary file that works in read-only environments
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_file:
                # Save TTS to temporary file
                tts.save(temp_file.name)
                
                # Read the file and encode to base64
                with open(temp_file.name, "rb") as audio_file:
                    my_string = base64.b64encode(audio_file.read())
                
                # Clean up temporary file
                try:
                    os.unlink(temp_file.name)
                except:
                    pass  # Ignore cleanup errors
                    
            return my_string
        except Exception as e:
            raise TTSException(e, sys)
