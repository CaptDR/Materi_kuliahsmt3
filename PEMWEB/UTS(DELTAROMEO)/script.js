// Animasi hover untuk tombol Explore
document.querySelector('.explore-btn').addEventListener('mouseover', function () {
    this.style.transform = 'scale(1.1)';
    this.style.backgroundColor = '#ff8533';
});

document.querySelector('.explore-btn').addEventListener('mouseleave', function () {
    this.style.transform = 'scale(1)';
    this.style.backgroundColor = '#ff6200';
});

// Animasi hover untuk elemen layanan
const serviceItems = document.querySelectorAll('.service-item');
serviceItems.forEach(item => {
    item.addEventListener('mouseover', () => {
        item.style.transform = 'scale(1.05)';
        item.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    });
    item.addEventListener('mouseleave', () => {
        item.style.transform = 'scale(1)';
        item.style.boxShadow = 'none';
    });
});
