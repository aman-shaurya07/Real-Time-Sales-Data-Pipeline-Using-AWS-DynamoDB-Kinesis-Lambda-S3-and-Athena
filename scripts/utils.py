import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_dynamodb():
    """Initialize a DynamoDB resource."""
    try:
        dynamodb = boto3.resource('dynamodb')
        return dynamodb
    except (NoCredentialsError, PartialCredentialsError) as e:
        logger.error(f"AWS credentials not found: {e}")
        return None

def log_error(error_message):
    """Log an error message."""
    logger.error(error_message)

def validate_json(data):
    """Validate if the input is a valid JSON object."""
    try:
        json_data = json.loads(data)
        return True, json_data
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON: {e}")
        return False, None
