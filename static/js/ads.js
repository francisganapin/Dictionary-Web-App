const images = [
    '/static/ads/addidas.png',
    '/static/ads/colgate.png',
    '/static/ads/cocacola.png',
];

function changeAdImage() {
    const adImage = document.getElementById('ad-placeholder-img');
    const randomIndex = Math.floor(Math.random() * images.length);
    adImage.src = images[randomIndex];
}

document.addEventListener('DOMContentLoaded', changeAdImage);
