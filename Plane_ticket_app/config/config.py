class Config:
    # The Flask app secret key
    SECRET_KEY = 'your_flask_secret_key'  # Replace with a secure, random string

    # The JWT secret key
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # This is needed for encoding and decoding the JWT tokens

    # Optional: Set JWT algorithm (HS256 is the default)
    JWT_ALGORITHM = 'HS256'  # This is the default but can be specified explicitly