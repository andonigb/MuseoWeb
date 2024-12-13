console.log("Estoy en el main.js");

const url = window.location.href;
const searchForm = document.getElementById('search-form');
const searchInput = document.getElementById('search-input');
const resultsBox = document.getElementById('results-box');

// Asegurémonos de que el CSRF token está disponible en el DOM
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
                data.forEach(obra => { // Toma solo los primeros 5 elementos
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
    // Verificamos si la tecla presionada es "Enter" (keyCode 13)
    if (e.key === 'Enter') {
        e.preventDefault();  // Prevenir el envío del formulario
        sendSearchData(searchInput.value);  // Llamar a la función para hacer la búsqueda
    }
});

