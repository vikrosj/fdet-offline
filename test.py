from fdet import io, MTCNN

detector = MTCNN()
image = io.read_as_rgb('g.jpg')

detections = detector.detect(image)
print(detections)