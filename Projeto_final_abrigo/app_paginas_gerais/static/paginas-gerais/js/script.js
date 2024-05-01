let currentIndex = 0;
const carouselItems = document.querySelectorAll('.carousel-item');

function showSlide(index) {
    if (carouselItems.length === 0) {
        return; // Não há itens no carrossel
    }

    // Garante que o índice esteja dentro dos limites do array
    index = (index + carouselItems.length) % carouselItems.length;

    carouselItems.forEach(item => {
        item.style.display = 'none';
    });

    carouselItems[index].style.display = 'block';
    currentIndex = index;
}

function nextSlide() {
    showSlide(currentIndex + 1);
}

function prevSlide() {
    showSlide(currentIndex - 1);
}

showSlide(currentIndex);
