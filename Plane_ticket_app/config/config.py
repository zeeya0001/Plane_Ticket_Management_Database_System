class Config:
    # The Flask app secret key
    SECRET_KEY = 'secret'  # Replace with a secure, random string

    # The JWT secret key
    JWT_SECRET_KEY = 'secret'  # This is needed for encoding and decoding the JWT tokens

    # Optional: Set JWT algorithm (HS256 is the default)
    JWT_ALGORITHM = 'HS256'  # This is the default but can be specified explicitly