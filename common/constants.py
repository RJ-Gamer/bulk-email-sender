"""
Constants for projects
"""
# ========================== ERRORS ==============================
ERR_MISSING_CREDENTIALS = "Please provide both username and password"
ERR_ACCOUNT_INACTIVE = "Your account is inactive. Please contact your administrator"
ERR_INVALID_LOGIN = "Provided username and password are invalid"
ERR_INVALID_FILE_TYPE = (
    "Provided file type is not supported. Only CSV/XLS/XLSX files are allowed"
)
ERR_INVALID_INPUT = "Please provide a valid {}"
# ============================== LOGGING ===========================
LOG_LOGIN_SUCCESS = "{} logged in successfully"
LOG_OBJ_CREATED = "{} created successfully"
LOG_OBJ_UPDATED = "{} updated successfully"
LOG_OBJ_DELETED = "{} deleted successfully"
LOG_EMAIL_NOT_SENT = "Error sending email to {}: {}"
LOG_EMAIL_SENT = "Email sent successfully to {}"

# ============================== MESSAGES ===========================
MSG_SUCCESS = "{} completed successfully"
MSG_CREATE_SUCCESS = "{} created successfully"
MSG_UPDATE_SUCCESS = "{} updated successfully"
MSG_DELETE_SUCCESS = "{} deleted successfully"

# ============================== FILE TYPES ============================
EXCEL_FILE_TYPES = [".xls", ".xlsx"]
CSV_FILE_TYPES = [".csv"]
EMAIL_SENT = "Email Sent"
EMAIL_FAILED = "Email Failed"
# ============================== OTHERS ============================
MAX_THREAD_WORKERS = 10
