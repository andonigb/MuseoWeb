const PAGES = {
    Artistas: "/artistas/",  
    Obras: "/obras/",        
    Museos: "/museos/",      
    Movimientos: "/movimientos/"
};

let selectInfo = document.getElementById('info-type');

selectInfo.addEventListener('change', event => {
    let selectedValue = event.target.value;
    if (PAGES[selectedValue]) {
        window.location.href = PAGES[selectedValue];
    } else {
        console.error("La opción seleccionada no está disponible en este momento.");
    }
});
