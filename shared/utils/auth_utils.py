from flask_jwt_extended import create_access_token
from datetime import timedelta

def generate_access_token(identity):
    """Generate a JWT token with an expiration."""
    expires = timedelta(hours=1)  # Set token expiry time
    return create_access_token(identity=identity, expires_delta=expires)