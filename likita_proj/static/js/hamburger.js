let hamburger = document.querySelector('.hamburger')
let navLinks = document.querySelectorAll('.nav-link')
let menu = document.querySelector('.menu')

hamburger.addEventListener('click', ()=>{
    hamburger.classList.toggle('active')
    menu.classList.toggle('active')
    document.querySelector('.head-section').classList.toggle('active')
})

navLinks.forEach(link=>{
    link.addEventListener('click', ()=>{
        hamburger.classList.remove('active')
        menu.classList.remove('active')
        
    })
})



let topicHamburger = document.querySelector('.topic-hamburger')
topics = document.getElementById('topics')

topicHamburger.addEventListener('click', ()=>{
    topics.classList.toggle('active')
})


