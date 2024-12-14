function toggleLike(button) {
    const obraId = button.getAttribute("data-obra-id");
    const likeIcon = document.getElementById(`like-icon-${obraId}`);
    const likeCount = document.getElementById(`like-count-${obraId}`);

    const url = `/api/like/${obraId}/`;

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
    })
        .then(response => {
            if (response.status === 401) {
                // Si no está autenticado, redirigir al login
                window.location.href = '/';
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // Actualiza el contador de "Me gusta"
                likeCount.textContent = `Me gusta: ${data.num_meGustas}`;

                // Cambia el ícono del corazón
                likeIcon.src = data.is_liked
                    ? data.redHeartUrl
                    : data.defaultHeartUrl;
            } else {
                console.error("Error al actualizar el 'Me gusta':", data.error);
            }
        })
        .catch(error => console.error("Error:", error));
}

function toggleLikeArtist(button) {
    const artistaId = button.getAttribute("data-artista-id");
    const likeIcon = document.getElementById(`like-icon-${artistaId}`);

    const url = `/api/like/artista/${artistaId}/`;  // URL para manejar el like del artista

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCSRFToken(),
        },
    })
    .then(response => {
        if (response.status === 401) {
            // Si no está autenticado, redirigir al login
            window.location.href = '/';
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // Cambiar el ícono del corazón
            likeIcon.src = data.is_liked
                ? data.redHeartUrl
                : data.defaultHeartUrl;
        } else {
            console.error("Error al actualizar el 'Me gusta':", data.error);
        }
    })
    .catch(error => console.error("Error:", error));
}
// Función para obtener el token CSRF
function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}