// Top menu scripts
let navbar = document.querySelector(".navbar");
window.addEventListener("scroll", function (e) {
  if (window.scrollY > 200) {
    navbar.classList.add("afix");
  } else {
    navbar.classList.remove("afix");
  }
});
