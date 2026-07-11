const slides = document.querySelectorAll(".slide");
let currentSlide = 0;
const next = document.querySelector("#next");
const prev = document.querySelector("#prev");
console.log(slides);
console.log(next);
console.log(prev);

function showSlide(index){
    slides.forEach(function(slide){
        slide.classList.remove("active");
    });
    slides[index].classList.add("active");
}
showSlide(currentSlide);
next.addEventListener("click", function(){
    nextSlide();
});
prev.addEventListener("click",function(){
    prevSlide();
});

setInterval(function(){
    nextSlide();
},4000);


function nextSlide(){
    currentSlide++;
    if(currentSlide >= slides.length){
        currentSlide = 0;
    }
    showSlide(currentSlide);
}

function prevSlide(){
    currentSlide--;
    if(currentSlide < 0){
        currentSlide = slides.length - 1;
    }
    showSlide(currentSlide);
}

