# Desc: Constants for HTTP status codes and messages
CREATED = 200
SUCCESS = 201
ERROR = 400
UNAUTHORIZED = 401
FORBIDDEN = 403
NOT_FOUND = 404
CONFLICT = 409
INTERNAL_SERVER_ERROR = 500

# Desc: Messages for HTTP status codes
MESSAGE = {
    'success': 'success',
    'error': 'error',
    'created': 'created',
    'unauthorized': 'unauthorized',
    'not_found': 'not_found',
    'conflict': 'conflict',
    'internal_server_error': 'internal_server_error',
    'invalid_token': 'invalid_token',
    'expired_token': 'expired_token',
    'invalid_credentials': 'invalid_credentials',
    'invalid_request': 'invalid_request',
    'invalid_data': 'invalid_data',
    'invalid_input': 'invalid_input',
    'invalid_output': 'invalid_output',
    'invalid_operation': 'invalid_operation',
    'invalid_method': 'invalid_method'
}

ALLOWED_EXTENSIONS = set(
    ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'zip', 'csv', 'xls', 'xlsx', 'doc', 'docx', 'ppt', 'pptx',
     'yaml', 'yml', 'xml', 'svg', 'mp4', 'mp3', 'wav', 'ogg', 'flac', 'avi', 'mov', 'wmv', 'webm', 'mkv', 'm4v',
     'sql','dump', 'psd', 'ai', 'eps', 'ps', 'tiff', 'tif', 'bmp', 'ico', 'raw', 'cr2', 'nef', 'orf', 'sr2', 'jfif', 'aes'])

