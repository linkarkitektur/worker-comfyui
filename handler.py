from websocket_server import WebsocketServer
import runpod
import os


shutdown_flag = False  # Flag to track when to stop the server

def handler(event):
    """RunPod job handler that runs the WebSocket server"""

    public_ip = os.environ.get('RUNPOD_PUBLIC_IP', 'localhost')   # COMPYT_HOST_PUBLIC_IP
    tcp_port = int(os.environ.get('RUNPOD_TCP_PORT_8188', '8188')) #COMPYT_HOST_TCP_PORT
    
    print(f"Public IP: {public_ip}")  
    print(f"TCP Port: {tcp_port}")  

    runpod.serverless.progress_update(event, f"Public IP: {public_ip}, TCP Port: {tcp_port}")

    return {
        "public_ip": public_ip,
        "tcp_port": tcp_port
    }

if __name__ == '__main__':
    runpod.serverless.start({'handler': handler})
