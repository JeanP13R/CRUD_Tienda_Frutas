document.addEventListener("DOMContentLoaded", function() {
    const btnSalir = document.getElementById("btn-salir");
    if (btnSalir) {
        btnSalir.addEventListener("click", function(event) {
            event.preventDefault(); // Prevenir la acción predeterminada de navegación
            Swal.fire({
                title: "¿Seguro que deseas salir?",
                showCancelButton: true,
                confirmButtonText: "Sí, salir",
                cancelButtonText: "Cancelar"
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = btnSalir.querySelector("a").href; // Redireccionar a la URL de salida
                }
            });
        });
    }

});