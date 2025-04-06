import os
import matplotlib.pyplot as plt
import imageio

def save_gif(states, filename):
    os.makedirs("gifs", exist_ok=True)
    images = []

    for state in states:
        fig, ax = plt.subplots()
        x, y = zip(*state)
        x += (x[0],)
        y += (y[0],)
        ax.plot(x, y, marker='o')
        ax.set_title("TSP Progress")
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        fig.canvas.draw()

        image_path = f"gifs/tmp_{len(images)}.png"
        fig.savefig(image_path)
        plt.close(fig)
        images.append(imageio.v2.imread(image_path))

    gif_path = f"gifs/{filename}.gif"
    imageio.mimsave(gif_path, images, duration=0.3)

    for image in os.listdir("gifs"):
        if image.startswith("tmp_"):
            os.remove(os.path.join("gifs", image))

    print(f"🎞️ GIF saved to {gif_path}")
