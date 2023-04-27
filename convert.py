import imageio
import os

for item in os.listdir('static/videos/'):
    try:
        video = imageio.mimread('static/videos/{}'.format(item), memtest=False)
    # import ipdb;ipdb.set_trace()
        imageio.mimwrite('static/videos1/{}'.format(item), video, fps=6, quality=8)
    except:
        print(item)
    # break
