const images = [
    '',
    '',
    '',
];

function changeAdImage() {
    const adImage = document.getElementById('ad-placeholder-img');
    const randomIndex = Math.floor(Math.random() * images.length);
    adImage.src = images[randomIndex];
}

document.addEventListener('DOMContentLoaded', changeAdImage);
