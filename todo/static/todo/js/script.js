const body = document.querySelector("body");
const navbar = document.querySelector("nav");
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

if (prefersDarkScheme.matches) {
    body.setAttribute("data-bs-theme", "dark");
    navbar.classList.replace("bg-warning", "bg-body-tertiary");
} else {
    body.setAttribute("data-bs-theme", "light");
    navbar.classList.replace("bg-body-tertiary", "bg-warning");
}