const title = document.querySelector('#title');

const clickedClass = "clicked"

function handleClick(){
    title.classList.toggle(clickedClass)
}
function init() {
    title.addEventListener("mouseenter", handleClick);
}
init();