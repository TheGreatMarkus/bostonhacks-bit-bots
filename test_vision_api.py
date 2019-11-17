from google.cloud import vision
import io

path = "./download.jpeg"
client = vision.ImageAnnotatorClient()

with io.open(path, 'rb') as image_file:
        content = image_file.read()

image = vision.types.Image(content=content)

response = client.face_detection(image=image)
faces = response.face_annotations

likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

print('Faces:')
for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))