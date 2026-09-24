# CodeAlpha-SecureCodingReview
## Vulnerabilities Found and Fixed

1. **Hardcoded Credentials** - Password and API key were written directly in code. Fixed by using environment variables.
2. **SQL Injection** - User input was directly inserted into SQL query. Fixed using parameterized queries.
3. **Command Injection** - User input passed directly to system command. Fixed with input validation.
4. **Path Traversal** - Filename not sanitized. Fixed using os.path.basename().

## Tool Used
Manual code review
