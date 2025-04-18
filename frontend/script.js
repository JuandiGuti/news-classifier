document.getElementById("btn-clasificar").addEventListener("click", () => {
    const texto = document.getElementById("texto").value;
    const resultadoDiv = document.getElementById("resultado");

    if (texto.trim() === "") {
        resultadoDiv.textContent = "Por favor, escribe una noticia.";
        return;
    }

    // Simulamos categoría (esto se conectará al backend después)
    let categoria = "General";
    if (texto.toLowerCase().includes("messi") || texto.toLowerCase().includes("fútbol")) {
        categoria = "Deportes";
    } else if (texto.toLowerCase().includes("dólar") || texto.toLowerCase().includes("bitcoin")) {
        categoria = "Economía";
    }

    resultadoDiv.textContent = `Categoría: ${categoria}`;

    // Crear item completo
    const lista = document.getElementById("lista-noticias");
    const item = document.createElement("li");

    item.innerHTML = `
        <strong>Noticia:</strong> ${texto}<br>
        <strong>Categoría:</strong> ${categoria}
    `;
    lista.appendChild(item);

    // Limpiar textarea
    document.getElementById("texto").value = "";

    // Eliminar mensaje de vacío si existe
    const vacio = document.querySelector("#lista-noticias li:first-child");
    if (vacio && vacio.textContent.includes("Vacío")) {
        vacio.remove();
    }
});
