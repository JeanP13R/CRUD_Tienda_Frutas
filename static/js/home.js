document.addEventListener("DOMContentLoaded", () => {
    // Selecciona todos los elementos con la clase "info"
    const verProductos = document.querySelectorAll(".info");

    if (verProductos.length > 0) {
        verProductos.forEach((verProducto) => {
            verProducto.addEventListener("click", (event) => {
                // Encontrar el contenedor del producto más cercano
                const producto = event.target.closest('.producto');
                // Encontrar el modal dentro de ese contenedor del producto
                const modal_container = producto.querySelector('.modal-container');

                if (modal_container) {
                    // Agrega la clase 'show' para mostrar el modal
                    modal_container.classList.add('show');
                } else {
                    console.error("No se encontró el contenedor del modal para el producto:", producto);
                }
            });
        });

        // Agrega el event listener para cerrar el modal
        const closeButtons = document.querySelectorAll(".close");
        closeButtons.forEach((closeButton) => {
            closeButton.addEventListener("click", (event) => {
                // Encuentra el modal-container más cercano al botón de cierre
                const modal_container = event.target.closest('.modal-container');

                if (modal_container) {
                    // Remueve la clase 'show' para ocultar el modal
                    modal_container.classList.remove('show');
                } else {
                    console.error("No se encontró el contenedor del modal para cerrar.");
                }
            });
        });

    } else {
        console.error("No se encontraron elementos con la clase 'info'.");
    }
});
