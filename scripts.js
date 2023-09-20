/*dark mode toggle*/
const switchElement = document.querySelector('.switch')

switchElement.addEventListener('click', () => {
  document.body.classList.toggle('dark')
})

/*fade in animation*/
const images = document.querySelectorAll(".image")

const observer = new IntersectionObserver(entries => { 
  entries.forEach(entry => {
    entry.target.classList.toggle("show", entry.isIntersecting)
    if (entry.isIntersecting) observer.unobserve(entry.target)
  })
},
{
    threshold: .1,
}
)
images.forEach(image => {
  observer.observe(image)
})