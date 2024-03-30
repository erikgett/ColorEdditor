from PIL import Image, ImageDraw

def is_color_near_white(color, threshold=200):
    # Проверяем, насколько близок цвет к белому
    return color[0] > 255 - threshold and color[1] > 255 - threshold and color[2] > 255 - threshold

def create_gradient_image_with_transparent_background(image, start_color = (146, 39, 143), end_color = (237, 28, 36)):
    # Открытие изображения
    # image = Image.open(image_path).convert("RGBA")
    width, height = image.size

    # Создание нового изображения для градиента с прозрачным фоном
    gradient_image = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(gradient_image)

    # Преобразование цветов из RGB в формат цветовой модели Pillow (R, G, B)
    start_color_pillow = (start_color[0], start_color[1], start_color[2], 255)  # Прозрачность 255 (непрозрачный)
    end_color_pillow = (end_color[0], end_color[1], end_color[2], 255)  # Прозрачность 255 (непрозрачный)

    # Создание градиента
    for y in range(height):
        for x in range(width):
            # Получение цвета текущего пикселя
            pixel_color = image.getpixel((x, y))

            # Если цвет текущего пикселя черный, устанавливаем альфа-канал в 0 (прозрачность)
            if pixel_color[3] < 50:  # цветное ли это
                draw.point((x, y), fill=(0, 0, 0, 0))  # Прозрачность 0 (прозрачный)
            else:
                # Если цвет не черный, заполняем его градиентом
                r = int(start_color_pillow[0] + (end_color_pillow[0] - start_color_pillow[0]) * y / height)
                g = int(start_color_pillow[1] + (end_color_pillow[1] - start_color_pillow[1]) * y / height)
                b = int(start_color_pillow[2] + (end_color_pillow[2] - start_color_pillow[2]) * y / height)
                draw.point((x, y), fill=(r, g, b, 255))  # Прозрачность 255 (непрозрачный)

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
