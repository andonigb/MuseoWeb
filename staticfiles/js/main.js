console.log("Estoy en el main.js");

const url = window.location.href;
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');


const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;


const sendSearchData = (obra) => {
    $.ajax({
        method: "POST",
        url: '/search/', 
        data: {
            'csrfmiddlewaretoken': csrf,
            'obra': obra
        },
        success: (res) => {
            console.log(res.data);
            const data = res.data;
            if(Array.isArray(data)){
                resultsBox.innerHTML = "";
                data.forEach(obra => { 
                    resultsBox.innerHTML += `<a href="/obra/${obra.id_obra}/" class="result-item">
                        <div class="result-info">
                            <h4>${obra.nombre}</h4>
                        </div>
                    </a>`;
                })
            }else{
                if(searchInput.value.length > 0){
                    resultsBox.innerHTML = `<h2 id="no-results-message">${data}</h1>`
                }else{
                    resultsBox.classList.add('not-visible');
                }   
        }
        },
        error: (err) => {
            console.log(err);   
        }
        
    })
}


searchInput.addEventListener('keyup', e=>{
    console.log(e.target.value);

    if (resultsBox.classList.contains('not-visible')) {
        resultsBox.classList.remove('not-visible');
    }

    sendSearchData(e.target.value);
})

searchForm.addEventListener('keydown', function(e) {

    if (e.key === 'Enter') {
        e.preventDefault();  
        sendSearchData(searchInput.value);  
    }
});

document.addEventListener('DOMContentLoaded', () => { 
    // Selecciona todos los contenedores de carrusel
    const carousels = document.querySelectorAll('.carousel-container');

    carousels.forEach(carousel => {
        const items = Array.from(carousel.children); // Aseguramos que todos los elementos estén en un array

        let itemWidth; // Declarar la variable para el ancho de los elementos
        let totalItems; // Declarar el total de ítems

        // Esperar a que todas las imágenes se carguen
        const checkImagesLoaded = () => {
            const allImagesLoaded = items.every(item => {
                const img = item.querySelector('img');
                return !img || img.complete;
            });

            if (allImagesLoaded) {
                initializeCarousel(); // Inicializar el carrusel una vez cargadas las imágenes
            } else {
                setTimeout(checkImagesLoaded, 50); // Volver a comprobar si no se han cargado todas las imágenes
            }
        };

        const initializeCarousel = () => {
            totalItems = items.length;

            // Si solo hay una imagen, no hacer nada con el carrusel
            if (totalItems <= 1) {
                carousel.style.display = 'block'; // Aseguramos que la imagen se vea sin movimiento
                return;
            }

            itemWidth = items[0].offsetWidth; // Ancho de cada elemento

            // Clona los elementos para crear el efecto infinito
            items.forEach(item => {
                const clone = item.cloneNode(true);
                carousel.appendChild(clone);
            });

            // Ajustar el ancho del contenedor para que sea suficiente para todas las imágenes (originales + clones)
            carousel.style.width = `${itemWidth * totalItems * 2}px`; // El contenedor ahora tiene el doble de ancho

            let currentOffset = 0;

            // Detectar cuando el ratón está sobre el carrusel
            carousel.addEventListener('mouseenter', () => {
                cancelAnimationFrame(carousel.animationId);
            });

            // Detectar cuando el ratón sale del carrusel
            carousel.addEventListener('mouseleave', () => {
                moveCarousel();
            });

            // Configuración inicial para mantener el contenedor estático
            carousel.style.display = 'flex';
            carousel.style.overflow = 'hidden';
            carousel.parentElement.style.overflow = 'hidden'; // Asegura que el contenedor padre también esté oculto

            // Función para mover las imágenes dentro del contenedor
            const moveCarousel = () => {
                // Incremento basado en el tiempo para una velocidad constante
                const speed = 0.5; // Velocidad constante
                currentOffset += speed; // Aumentar el desplazamiento con cada fotograma

                // Cuando el carrusel llega al final de las imágenes (originales + clones), reseteamos la posición para hacerlo infinito
                if (currentOffset >= itemWidth * totalItems) {
                    currentOffset = 0; // Reinicia el desplazamiento
                }

                carousel.style.transform = `translateX(-${currentOffset}px)`; // Mueve el carrusel

                carousel.animationId = requestAnimationFrame(moveCarousel); // Mantén el movimiento
            };

            moveCarousel(); // Inicia el movimiento del carrusel
        };

        checkImagesLoaded();
        
    });
});