import cv2
import matplotlib.pyplot as plt

# Carregar duas imagens
image1 = cv2.imread('/home/joao/Downloads/test1.jpg')
image2 = cv2.imread('/home/joao/Downloads/teste2.jpg')

# Redimensionar as imagens para o mesmo tamanho (se necessário)
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Definir o valor de alpha (transparência)
alpha = 0.5  # 50% de cada imagem

# Aplicar a sobreposição
blended_image = cv2.addWeighted(image1, 1 - alpha, image2, alpha, 0)

# Exibir as imagens
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.title('Imagem 1 (Lena)')
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 2)
plt.title('Imagem 2 (Tux)')
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(1, 3, 3)
plt.title(f'Sobreposição (α = {alpha})')
plt.imshow(cv2.cvtColor(blended_image, cv2.COLOR_BGR2RGB))
plt.show()