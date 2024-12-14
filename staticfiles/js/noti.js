

const notificationIcon = document.getElementById('notification-icon');
const notificationBox = document.getElementById('notification-box');
const notificationTitle = document.getElementById('notification-title');
const notificationInfo = document.getElementById('notification-info');
const notificationImg = document.getElementById('notification-img');


const getCuriosity = () => {
    $.ajax({
        method: "GET",
        url: '/notification/',  
        success: (res) => {
            if (res.data) {
                const curiosity = res.data;
                notificationTitle.innerHTML = curiosity.nombre_obra;  
                
      
                const link = `<a href="/obra/${curiosity.id_obra}/" id="more-info">Saber más</a>`;
                notificationInfo.innerHTML = link;  

      
                notificationImg.classList.add('new-notification');
            }
        },
        error: (err) => {
            console.log('Error al obtener curiosidad:', err);
        }
    });
};

// Mostrar la curiosidad cuando el usuario hace clic en el ícono de notificación
notificationIcon.addEventListener('click', () => {
    // Mostrar la notificación
    notificationBox.classList.toggle('not-visible');
    // Eliminar el efecto amarillo (quitar la clase)
    notificationImg.classList.remove('new-notification');
});



setInterval(getCuriosity, 60000);
