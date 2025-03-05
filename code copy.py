import cv2
import numpy as np
import matplotlib.pyplot as plt

#LINK VIDEO  https://youtu.be/BBCXYp0oOLs


# Carregar duas imagens
image1 = cv2.imread('/home/joao/Downloads/test1.jpg')
image2 = cv2.imread('/home/joao/Downloads/teste2.jpg')

# Redimensionar as imagens para o mesmo tamanho (se necessário)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Definir o valor de alpha (transparência)
alpha = 0.5  # 50% de cada imagem

# Criar a máscara diagonal de 45 graus
height, width, _ = image1.shape

mask = np.zeros((height, width), dtype=np.uint8)

# A linha que define a diagonal de 45 graus
for i in range(height):
    for j in range(width):
        if j >= i: 
            mask[i, j] = 255

mask_colored = cv2.merge([mask, mask, mask])

image1_with_mask = cv2.bitwise_and(image1, image1, mask=mask)
image2_with_mask = cv2.bitwise_and(image2, image2, mask=mask)

blended_image = cv2.addWeighted(image1_with_mask, 1 - alpha, image2_with_mask, alpha, 0)

# Exibir as imagens
plt.figure(figsize=(15, 5))

# Exibir imagem 1
plt.subplot(1, 3, 1)
plt.title('Imagem 1 (Teste 1)')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

# Exibir imagem 2
plt.subplot(1, 3, 2)
plt.title('Imagem 2 (Teste 2)')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

# Exibir a imagem sobreposta
plt.subplot(1, 3, 3)
plt.title(f'Sobreposição (α = {alpha})')
plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))

# Mostrar o resultado
plt.show()
