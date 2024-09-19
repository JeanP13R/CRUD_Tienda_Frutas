document.addEventListener("DOMContentLoaded", () => {
    // Selecciona todos los elementos con la clase "info"
    const verProductos = document.querySelectorAll(".info");

    if (verProductos.length > 0) {
        verProductos.forEach((verProducto) => {
            verProducto.addEventListener("click", () => {
                alert("verProducto")
            });
        });
    } else {
        console.error("No se encontraron elementos con la clase 'info'.");
    }
});

// productos.js

document.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('.delete-form');

    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault(); // Previene el envío inmediato del formulario

            const confirmDelete = Swal.fire({
                title: '¿Estás seguro?',
                text: "No podrás revertir esto!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, eliminarlo!',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Si el usuario confirma, envía el formulario
                    form.submit();
                }
            });
        });
    });
});



