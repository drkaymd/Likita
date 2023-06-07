editBtn = document.querySelectorAll(".edit-delete-menu");
edits = document.querySelectorAll(".edit-delete");

function editDelete() {
  editBtn.forEach((btn) => {
    edits.forEach((edit) => {
      btn.addEventListener("click", () => {
        edit.classList.toggle("shows");
      });
    });
  });
}
editDelete();

let caret = document.querySelector(".fa-caret-down");
let hide = document.querySelector(".hide-wrapper");

function caretDown() {
  caret.addEventListener("click", () => {
    hide.classList.toggle("drops");
  });
}
caretDown();


// close messages-box
close = document.querySelector(".close");
messages = document.querySelector(".messages");

function closeMessages() {
  close.addEventListener("click", () => {
    messages.style.display = "none";
  });
}
closeMessages()


// minimize post image

// function minimizeImage(){
//   image = document.querySelectorAll('.posts .image-box img')
//   minimize = document.querySelectorAll('.minimize')
//   minimize.addEventListener('click', ()=>{
//     image.style.display = "none"
//   })
// }