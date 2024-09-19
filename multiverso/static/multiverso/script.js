document.addEventListener("DOMContentLoaded", function() {
    const nodos = document.querySelectorAll('.nodo'); // Seleccionar todos los nodos
    let currentIndex = 0; // Índice del nodo actual

    // Mostrar solo el primer nodo inicialmente
    nodos[currentIndex].classList.add('active');

    // Actualizar el índice en la página
    function updateCurrentIndexDisplay() {
        document.getElementById('currentIndexDisplay').textContent = `Índice actual: ${currentIndex}`;
    }

    // Mostrar el índice actual al cargar la página
    updateCurrentIndexDisplay();

    // Acción para el botón "Siguiente"
    document.getElementById('nextButton').addEventListener('click', function() {
        // Esconder el nodo actual
        nodos[currentIndex].classList.remove('active');

        // Actualizar el índice al siguiente nodo
        currentIndex = (currentIndex + 1) % nodos.length; // Volver al inicio después del último nodo

        // Mostrar el nuevo nodo
        nodos[currentIndex].classList.add('active');
        // Mostrar el índice actual al cargar la página
        updateCurrentIndexDisplay();
    });
});

function mostrarModal(nombre, descripcion, imagen1, imagen2) {
    // Mostrar el modal
    const modal = document.getElementById('modal');
    modal.style.display = 'block';

    // Insertar el contenido dinámico
    document.getElementById('modal-nombre').textContent = nombre;
    document.getElementById('modal-descripcion').textContent = descripcion;
    document.getElementById('modal-imagen1').src = imagen1;
    document.getElementById('modal-imagen2').src = imagen2;
}

// Cerrar el modal al hacer clic en la "X"
document.getElementById('closeModal').onclick = function() {
    document.getElementById('modal').style.display = 'none';
}

// Cerrar el modal si se hace clic fuera de la ventana
window.onclick = function(event) {
    const modal = document.getElementById('modal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('.nodo-link');
    
    links.forEach(link => {
        link.addEventListener('click', (event) => {
            event.preventDefault(); // Previene el comportamiento predeterminado del enlace
            alert(`Enlace con índice ${link.dataset.index} ha sido clicado. El bucle se detendrá.`);

            // Aquí puedes agregar la lógica para romper el bucle
            // Por ejemplo, deshabilitar el botón "Siguiente" o cualquier otra acción.
            document.getElementById('nextButton').disabled = true;
        });
    });
});


