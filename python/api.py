from aiohttp import web
import aiohttp_cors
from PIL import Image
import numpy as np
import tensorflow as tf

import os
import io

IMAGE_SIZE = 224
model = tf.keras.models.load_model(os.path.join('models', '20200821_1.h5'))


async def store_img_handler(request):
    reader = await request.multipart()
    # /!\ Don't forget to validate your inputs /!\
    # reader.next() will `yield` the fields of your form
    field = await reader.next()
    print(field.name)

    size = 0
    chunks = []
    while True:
        chunk = await field.read_chunk()  # 8192 bytes by default.
        if not chunk:
            break

        size += len(chunk)
        chunks.append(chunk)

    image_data = b''.join(chunks)
    img = Image.open(io.BytesIO(image_data))
    img = img.convert('RGB')
    img = img.resize((IMAGE_SIZE, IMAGE_SIZE))
    img = np.array(img)
    img = np.expand_dims(img, axis=0)

    print(img.shape)
    y_pred_prob = model.predict(img)
    print(y_pred_prob.shape)
    y_pred = int(np.argmax(y_pred_prob))

    return web.json_response({
        'size': size,
        'y_pred': y_pred,
        'y_pred_proba_0': float(y_pred_prob[0, 0]),
        'y_pred_proba_1': float(y_pred_prob[0, 1])
    })


app = web.Application()
cors = aiohttp_cors.setup(app, defaults={
    "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
        )
})

# Add all resources to `CorsConfig`.
resource = cors.add(app.router.add_resource('/upload'))
cors.add(resource.add_route('POST', store_img_handler))

if __name__ == '__main__':
    web.run_app(app, port=81)
