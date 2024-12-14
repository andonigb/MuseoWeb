document.getElementById("ticketForm").addEventListener("submit", function(event) {
    const nombre = document.getElementById("nombre").value.trim();
    const email = document.getElementById("email").value.trim();
    const fecha = document.getElementById("fecha").value;
    const hora = document.getElementById("hora").value;
    const tarjeta = document.getElementById("tarjeta").value.trim();

    let errores = [];

    if (nombre === "") {
        errores.push("El nombre y apellidos son obligatorios.");
    }

    if (email === "" || !/^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(email)) {
        errores.push("Introduce un correo electrónico válido.");
    }

    if (fecha === "") {
        errores.push("La fecha de visita es obligatoria.");
    } else {
        const fechaHoy = new Date().toISOString().split("T")[0]; 
        if (fecha < fechaHoy) {
            errores.push("La fecha de visita debe ser hoy o una fecha posterior.");
        }
    }

    if (hora === "") {
        errores.push("La hora de visita es obligatoria.");
    }

    if (!/^[0-9]{16}$/.test(tarjeta)) {
        errores.push("Introduce un número de tarjeta válido de 16 dígitos.");
    }

    if (errores.length > 0) {
        alert(errores.join("\n"));
        event.preventDefault(); 
    } else {
        // Si no hay errores, se muestra la ventana emergente
        document.getElementById("compraExito").style.display = "flex";
        
        // Cerrar la ventana emergente después de 3 segundos
        setTimeout(function() {
            document.getElementById("compraExito").style.display = "none";
        }, 3000);

        // Cerrar la ventana emergente al hacer clic en el botón de cerrar
        document.getElementById("cerrarPopup").addEventListener("click", function() {
            document.getElementById("compraExito").style.display = "none";
        });
    }
});
