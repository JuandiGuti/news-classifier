document.addEventListener("DOMContentLoaded", () => {
    const boton = document.getElementById("btn-clasificar");
    const input = document.getElementById("texto");
    const resultado = document.getElementById("resultado");
    const listaNoticias = document.getElementById("lista-noticias");

    boton.addEventListener("click", async () => {
        const texto = input.value.trim();

        if (texto === "") {
            resultado.textContent = "Por favor escribe una noticia.";
            return;
        }

        try {
            const response = await fetch("http://127.0.0.1:8000/get-text-news", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ texto }),
            });

            const data = await response.json();
            resultado.textContent = `Category: ${data.category}`;

            // Quitar el mensaje por defecto si aún existe
            const mensajeVacio = listaNoticias.querySelector("li");
            if (mensajeVacio && mensajeVacio.textContent.includes("Empty")) {
                listaNoticias.innerHTML = "";
            }

            // Agregar la noticia al historial con formato personalizado
            const nuevoItem = document.createElement("li");
            nuevoItem.innerHTML = `<strong>News:</strong> ${texto}<br><strong>Category:</strong> ${data.category}`;
            listaNoticias.appendChild(nuevoItem);
        } catch (error) {
            resultado.textContent = "Error al conectar con la API.";
            console.error(error);
        }
    });
});
