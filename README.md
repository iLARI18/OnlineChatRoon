# Python Chat Server and Client

This project is a simple Python-based chat server and client that allows multiple clients to connect to a server and broadcast messages to all connected clients.

## Features

- Clients can send messages to the server.
- Server broadcasts messages to all connected clients.
- Clients can disconnect by typing `disconnect`.

## Requirements

- Python 3.x

## Setup and Running

### Server

1. Clone this repository.
2. Navigate to the server directory.
3. Run the server using the following command:

    ```bash
    python server.py
    ```

### Client

1. Clone this repository on another machine or terminal.
2. Navigate to the client directory.
3. Connect to the server by running:

    ```bash
    python client.py
    ```

4. Enter your message, and it will be broadcast to all connected clients.

## Configuration

- **Port**: The server uses port `5050` by default. You can change it in the `server.py` and `client.py` files if necessary.
- **Server IP**: In the client code, replace the `SERVER` variable with the actual IP address of the machine running the server.

## Usage

- Start the server first, then run the client on one or more machines.
- Type your message in the client to broadcast it to all other clients.
- Type `disconnect` to exit the chat.

## Troubleshooting

- Ensure that the server IP is correctly set in the client file.
- Ensure that your firewall or router is not blocking the port.
- Both the server and client must be on the same local network or use port forwarding for external connections.

