from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import cv2
import numpy as np
import base64
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

model = YOLO("yolov8n.pt")

@socketio.on('image')
def handle_image(data):
    # Decode the base64 image
    image_data = base64.b64decode(data.split(',')[1])
    image = cv2.imdecode(np.frombuffer(image_data, np.uint8), cv2.IMREAD_COLOR)

    results = model(image)
    
    for result in results:
        boxes = result.boxes.xyxy.cpu().numpy()
        classes = result.boxes.cls.cpu().numpy()
        for box, cls in zip(boxes, classes):
            x1, y1, x2, y2 = map(int, box[:4])
            label = model.names[int(cls)]
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    _, buffer = cv2.imencode('.jpg', image)
    processed_image = base64.b64encode(buffer).decode('utf-8')

    emit('processed_image', processed_image)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
