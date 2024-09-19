var modal = document.getElementById("modal-register");

    // Mostrar el modal al cargar la página si hay un parámetro `next`
    window.onload = function() {
        const params = new URLSearchParams(window.location.search);
        if (params.has('next')) {
            modal.style.display = "block";
        }
    }

    // Obtener el <span> que cierra el modal
    var span = document.getElementsByClassName("close")[0];

    // Cuando el usuario hace clic en <span> (x), cerrar el modal
   

    // Cuando el usuario hace clic en cualquier lugar fuera del modal, cerrarlo
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }

    // Manejar el envío del formulario
    document.getElementById('loginForm').onsubmit = async function(event) {
        event.preventDefault();

        let formData = new FormData(this);
        let response = await fetch("{% url 'login' %}", {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        });
        let result = await response.json();

        if (result.success) {
            const params = new URLSearchParams(window.location.search);
            const nextUrl = params.get('next') || "{% url 'home' %}";
            window.location.href = nextUrl;
        } else {
            document.getElementById('error').innerText = result.error;
        }
    };