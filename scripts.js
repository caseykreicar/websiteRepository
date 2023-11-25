/*dark mode toggle*/
const switchElement = document.querySelector('.switch')

switchElement.addEventListener('click', () => {
  document.body.classList.toggle('dark')
})

/*fade in animation1 my photo*/
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

/*fade in animation2 squirrel*/
const squirrel = document.querySelectorAll(".squirrel")

const observer2 = new IntersectionObserver(entries => { 
  entries.forEach(entry => {
    entry.target.classList.toggle("show", entry.isIntersecting)
    if (entry.isIntersecting) observer2.unobserve(entry.target)
  })
},
{
    threshold: .1,
}
)
squirrel.forEach(squirrel => {
  observer.observe(squirrel)
})

/*fade in animation3 speech bubble*/
const speechBubble = document.querySelectorAll(".speechBubble")

const observer3 = new IntersectionObserver(entries => { 
  entries.forEach(entry => {
    entry.target.classList.toggle("show", entry.isIntersecting)
    if (entry.isIntersecting) observer2.unobserve(entry.target)
  })
},
{
    threshold: .1,
}
)
speechBubble.forEach(speechBubble => {
  observer.observe(speechBubble)
})