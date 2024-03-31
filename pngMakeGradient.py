from PIL import Image, ImageDraw

def is_color_near_white(color, threshold=200):
    # Проверяем, насколько близок цвет к белому
    return color[0] > 255 - threshold and color[1] > 255 - threshold and color[2] > 255 - threshold

def create_gradient_image_with_transparent_background(image, start_color = (146, 39, 143), end_color = (237, 28, 36)):
    # Открытие изображения
    width, height = image.size
    print(width, height)

    # Создание нового изображения для градиента с прозрачным фоном
    gradient_image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(gradient_image)

    # Преобразование цветов из RGB в формат цветовой модели Pillow (R, G, B)
    start_color_pillow = (start_color[0], start_color[1], start_color[2], 255)  # Прозрачность
    end_color_pillow = (end_color[0], end_color[1], end_color[2], 255)  # Прозрачность

    # Создание градиента
    for y in range(height):
        for x in range(width):
            pixel_color = image.getpixel((x, y))
            if isinstance(pixel_color, (int, float)):
                pixel_color = (0, 0, 0, 0)
            try:

                # Если цвет текущего пикселя черный, устанавливаем альфа-канал в 0 (прозрачность)
                if pixel_color[0] < 40 and pixel_color[1] < 40 and pixel_color[2] < 40:  # черный заполняем градиентом.
                    r = int(start_color_pillow[0] + (end_color_pillow[0] - start_color_pillow[0]) * y / height)
                    g = int(start_color_pillow[1] + (end_color_pillow[1] - start_color_pillow[1]) * y / height)
                    b = int(start_color_pillow[2] + (end_color_pillow[2] - start_color_pillow[2]) * y / height)
                    draw.point((x, y), fill=(r, g, b, pixel_color[3]))  # Прозрачность 255 (непрозрачный)
                elif pixel_color[0] > 200 and pixel_color[1] > 200 and pixel_color[2] > 200: # белые пиксели
                    draw.point((x, y), fill=(0, 0, 0, 0))  # Прозрачность 0 (прозрачный)
                else: # цветные оставляем
                    draw.point((x, y), fill=(pixel_color[0], pixel_color[1], pixel_color[2], pixel_color[3]))  # Прозрачность 0 (прозрачный)
            except:
                    draw.point((x, y), fill=(pixel_color[0], pixel_color[1], pixel_color[2], pixel_color[3]))

    return gradient_image

if __name__ == "main":
    # Путь к изображению
    image_path = "icons8-windows-500.png"

    # Цвета начала и конца градиента (RGB)
    start_color = (146, 39, 143)
    end_color = (237, 28, 36)

    # Создание изображения с градиентом и прозрачным фоном
    gradient_image = create_gradient_image_with_transparent_background(image_path, start_color, end_color)

    # Сохранение изображения
    gradient_image.save("output.png", format="PNG")

    print("Изображение с градиентом и прозрачным фоном сохранено.")
