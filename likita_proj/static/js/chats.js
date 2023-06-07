function showChat() {
  document.querySelector(".chat").addEventListener("click", () => {
    document.querySelector("aside").classList.toggle("shows");
  });
}
showChat();
