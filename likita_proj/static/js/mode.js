// day and night modes

let day = document.querySelector(".fa-sun");
let night = document.querySelector(".fa-moon");
let mode = document.querySelector(".mode");

function darkMode() {
  document.body.classList.add("dark-mode");
  localStorage.setItem("mode", "dark");
}
function noDark() {
  document.body.classList.remove("dark-mode");
  localStorage.setItem("mode", "");
}
if (localStorage.getItem("mode") === "dark") {
  darkMode();
} else {
  noDark();
}

mode.addEventListener("click", (e) => {
  document.body.classList.toggle("dark-mode");
  if (document.body.classList.contains("dark-mode")) {
    darkMode();
    night.style.display = "block";
    day.style.display = "none";
  } else {
    noDark();
    day.style.display = "block";
    night.style.display = "none";
  }
});

