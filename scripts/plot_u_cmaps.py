from skimage.io import imread, imsave
from skimage.color import rgb2gray
from skimage.transform import resize
from skimage import img_as_ubyte
import matplotlib.pyplot as plt
import numpy as np

u = imread('images/dortmunder_u_rgb.jpg')
u_small = resize(u, (24, 24), anti_aliasing=True)
u_sw = rgb2gray(u_small)
u_sw = img_as_ubyte(u_sw)


rows, cols = u_sw.shape

with open('build/img.tex', 'w') as f:
    f.write(r'\begin{tabular}{' + r'@{} r @{\hspace{0.5em}}' * cols + '@{}}\n')

    for row in u_sw:
        f.write('  ' + ' & '.join(row.astype(str)) + r'\\' + '\n')
    f.write(r'\end{tabular}' + '\n')

height = plt.rcParams['figure.figsize'][1]


imsave('build/plots/u_sw.png', u_sw)

fig, axs = plt.subplots(2, 2, figsize=(0.95  * height, height))

axs = axs.flatten()

for i, cmap in enumerate(('gray', 'jet', 'hot', 'viridis')):

    axs[i].imshow(u_sw, cmap=cmap)
    axs[i].set_title(cmap)
    axs[i].set_axis_off()
    axs[i].set_xticks([])
    axs[i].set_yticks([])

fig.tight_layout(pad=0.4, h_pad=1.2)

fig.savefig('build/plots/u_cmaps.pdf')


gradient = np.linspace(0, 255, 256)
img = np.vstack([gradient, gradient])
fig = plt.figure(figsize=(2, 0.3))
ax = fig.add_subplot(1, 1, 1)
ax.imshow(img, cmap='gray')
ax.set_aspect('auto')
ax.set_yticks([])
ax.set_xticks(np.arange(0, 257, 128))
ax.set_xlim(0, 256)
fig.tight_layout(pad=0)
fig.savefig('build/plots/u_cmap.pdf')
