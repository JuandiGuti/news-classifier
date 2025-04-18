document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("formulario");
    const input = document.getElementById("texto");
    const resultado = document.getElementById("resultado");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const texto = input.value;

        const response = await fetch("http://127.0.0.1:8000/get-text-news", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ texto }),
        });

        const data = await response.json();
        resultado.textContent = `Categoría: ${data.category}`;
    });
});
