document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const searchResults = document.getElementById("search-results");

    searchInput.addEventListener("input", async (event) => {
        const query = event.target.value.trim();
        if (query.length === 0) {
            searchResults.innerHTML = "";
            return;
        }
        
        try {  
            const response = await fetch(`/api/artistas/?search=${encodeURIComponent(query)}`);
            if (!response.ok) throw new Error("Error al buscar artistas");

            const artistas = await response.json();
            displayResults(artistas);
        } catch (error) {
            console.error("Error:", error);
        }
    });

    function displayResults(artistas) {
        searchResults.innerHTML = "";
        if (artistas.length === 0) {
            searchResults.innerHTML = "<div>No se encontraron resultados</div>";
            return;
        }

        artistas.forEach((artista) => {
            const resultItem = document.createElement("div");
            resultItem.textContent = artista.nombre;
            resultItem.addEventListener("click", () => {
                window.location.href = `/artistas/${artista.id}/`;
            });
            searchResults.appendChild(resultItem);
        });
    }
});
