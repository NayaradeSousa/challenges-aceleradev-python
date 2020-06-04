"""
################################ Challenge 04 Aceleradev Python #######################################################
Complete the functions to revert a json web token, generated using the HS256 algorithm, which contains the following
information {“language”: “Python”}, with the secret word speeds up, complete the function to decipher the information
treating the exception when signature is invalid and should return the following dictionary {“error”: 2}. If there is
no error, return the deciphered information.
#######################################################################################################################
"""
import jwt


def create_token(data, secret):
    """
    This method create a token for data transmission securely between
    two parties.
    :param data: data for encryption
    :param secret: Data encryption key
    :return: Token in Json generated from the HS256 algorithm
    """
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    """
    This method validates the token from secret key.
    :param token: Encoded data
    :return: Payload data decoded
    """
    secret = 'acelera'
    try:
        return jwt.decode(token, secret, algorithms='HS256')
    except jwt.InvalidSignatureError:
        return {"error": 2}


if __name__ == '__main__':
    # variables declared here to facilitate if they need to be modified
    secret_key = 'acelera'
    payload_data = {"language": "Python"}

    encode_jwt = create_token(payload_data, secret_key)
    print(f"Your Token is: {encode_jwt}.")
    print(verify_signature(encode_jwt))
