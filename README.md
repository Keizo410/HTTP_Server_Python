# Simple HTTP Server  

A simple HTTP server implemented in Python using the `socket` module. This server listens for incoming client connections, processes HTTP requests, and serves files from the `htdocs` directory.  

## Features  

- Handles basic HTTP GET requests.  
- Serves static files from the `htdocs` directory.  
- Returns a 404 response if the requested file is not found.  

## How It Works  

1. The server listens on all interfaces (`0.0.0.0`) and port `8000`.  
2. Upon receiving a client connection, it parses the HTTP request.  
3. If the requested file is `/`, it serves `index.html` from the `htdocs` directory.  
4. If the file exists, it returns a `200 OK` response with the file content.  
5. If the file does not exist, it returns a `404 NOT FOUND` response.  


## Requirements  

- Python 3.x  

## Usage  

1. Run the script using the following command:  

   ```bash
   python3 main.py
   ```
2. The server will start and listen on port 8000.

3. Open a web browser or use a tool like curl to send HTTP requests:
   - For example, access http://localhost:8000/ in your browser.
     
4. Logs for received requests will be displayed in the terminal.

## Limitations
Only supports HTTP GET requests.
No advanced features like HTTPS or request routing.
Assumes all files are stored in the htdocs directory.
