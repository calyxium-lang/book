document.addEventListener("DOMContentLoaded", () => {
    const title = document.querySelector("h1.menu-title");
    if (title) {
        const link = document.createElement("a");
        link.href = "https://calyxium-lang.github.io/";
        link.innerHTML = title.innerHTML;
        link.style.color = "inherit";
        link.style.textDecoration = "none";
        link.style.font = "inherit";
        link.style.display = "inline-block";
        link.style.width = "100%";
        title.innerHTML = "";
        title.appendChild(link);
    }
});