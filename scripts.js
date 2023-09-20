/*dark mode toggle*/
const switchElement = document.querySelector('.switch')

switchElement.addEventListener('click', () => {
  document.body.classList.toggle('dark')
})

/*fade in animation*/
const observer = new IntersectionObserver(entries => { 
  entries.forEach(entry => {
    if(entry.isIntersection){
      document.querySelectorAll("card-container")[0].classList.add("card");
    }
  })
})

observer.observe(document.querySelector(".card"));